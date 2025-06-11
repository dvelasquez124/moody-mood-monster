import os
import pandas as pd

# Dynamically get the path to mood_log.csv
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, '..', 'mood_log.csv')

# Try to load the mood log
try:
    df = pd.read_csv(CSV_PATH)
    print("✅ mood_log.csv loaded successfully!")
except FileNotFoundError:
    print("❌ mood_log.csv not found. Make sure it's in the root folder.")
    exit()

# Preview the first few rows
print("\n📋 First 5 entries:")
print(df.head())

# Check the structure and column types
print("\n📊 Data summary:")
print(df.info())

import matplotlib.pyplot as plt

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date']).dt.date

# Group by date and mood
daily_moods = df.groupby(['date', 'mood']).size().unstack(fill_value=0)

# fill in missing days with 0s
full_index = pd.date_range(start=df['date'].min(), end=df['date'].max())
daily_moods.index = pd.to_datetime(daily_moods.index)
daily_moods = daily_moods.reindex(full_index, fill_value=0)


# Plot mood trends over time
daily_moods.plot(figsize=(10, 6), marker='o', linewidth=2, alpha=0.7)
plt.title('Mood Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Mood Count')
plt.legend(title="Mood")
plt.grid(True)
plt.tight_layout()
plt.show()



# Count each mood
mood_counts = df['mood'].value_counts()

# Plot as a bar chart
plt.figure(figsize=(8, 5))
mood_counts.plot(kind='bar')
plt.title("Mood Frequency")
plt.xlabel('Mood')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()