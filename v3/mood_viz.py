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

# Chec the structure and column types
print("\n📊 Data summary:")
print(df.info())