# mood_viz.py (Day 1 - Load CSV)

import pandas as pd

# Try to load the mood log
try:
    df = pd.read_csv('/Users/dianavelasquez/moody-mood-monster/mood_log.csv')
    print("✅ mood_log.csv loaded successfully!")
except FileNotFoundError:
    print("❌ mood_log.csv not found. Make sure it's in the root folder.")

# Preview the first few rows
print("\n📋 First 5 entries:")
print(df.head())

# Check the structure and column types
print("\n📊 Data summary:")
print(df.info())

import matplotlib.pyplot as plt

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