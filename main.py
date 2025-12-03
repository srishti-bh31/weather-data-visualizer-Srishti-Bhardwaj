#  WEATHER DATA VISUALIZER - MINI PROJECT
# --------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------- TASK 1: LOAD DATA -----------------

df = pd.read_csv("weather_data.csv")

print("HEAD:")
print(df.head())

print("\nINFO:")
print(df.info())

print("\nDESCRIBE:")
print(df.describe())


# -------- TASK 2: CLEANING -----------------

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Removing missing values
df = df.dropna(subset=['temperature', 'rainfall', 'humidity'])

# Keep only required columns
df = df[['date', 'temperature', 'rainfall', 'humidity']]

print("\nCLEANED DATA:")
print(df.head())


# -------- TASK 3: STATISTICS USING NUMPY --------

temps = df['temperature'].values

print("\nDAILY STATISTICS")
print("Mean temperature:", np.mean(temps))
print("Min temperature:", np.min(temps))
print("Max temperature:", np.max(temps))
print("Std deviation:", np.std(temps))

# Monthly stats
df['month'] = df['date'].dt.month
monthly_stats = df.groupby('month')['temperature'].agg(['mean', 'min', 'max', 'std'])
print("\nMONTHLY STATS:")
print(monthly_stats)


# -------- TASK 4: VISUALIZATIONS -----------------

# Line Plot (Daily Temperature)
plt.figure(figsize=(10,5))
plt.plot(df['date'], df['temperature'])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.savefig("plots/daily_temperature.png")
plt.show()

# Bar Plot (Monthly Rainfall)
monthly_rainfall = df.groupby("month")['rainfall'].sum()

plt.figure(figsize=(8,5))
plt.bar(monthly_rainfall.index, monthly_rainfall.values)
plt.title("Total Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.savefig("plots/monthly_rainfall.png")
plt.show()

# Scatter Plot (Humidity vs Temperature)
plt.figure(figsize=(7,5))
plt.scatter(df['temperature'], df['humidity'])
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.savefig("plots/humidity_vs_temp.png")
plt.show()

# Combined figure (2 subplots)
fig, ax = plt.subplots(1, 2, figsize=(12,5))

ax[0].plot(df['date'], df['temperature'])
ax[0].set_title("Daily Temperature")

ax[1].scatter(df['temperature'], df['humidity'])
ax[1].set_title("Humidity vs Temperature")

plt.savefig("plots/combined_plot.png")
plt.show()


# -------- TASK 5: GROUPING & AGGREGATION --------------

season_map = {
    12: "Winter", 1: "Winter", 2: "Winter",
    3: "Summer", 4: "Summer", 5: "Summer",
    6: "Monsoon", 7: "Monsoon", 8: "Monsoon",
    9: "Autumn", 10: "Autumn", 11: "Autumn"
}

df['season'] = df['month'].map(season_map)

season_stats = df.groupby("season")['temperature'].mean()
print("\nSEASON-WISE AVERAGE TEMPERATURE:")
print(season_stats)


# -------- TASK 6: EXPORT CLEANED FILE -----------------

df.to_csv("cleaned_weather.csv", index=False)

print("\nCLEANED DATA SAVED AS cleaned_weather.csv")
print("ALL PLOTS SAVED IN /plots FOLDER")