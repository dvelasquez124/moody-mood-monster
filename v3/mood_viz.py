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