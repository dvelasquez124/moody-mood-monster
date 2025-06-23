import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import argparse


# User settings
USER_NAME = "Diana"

# Store today's date
today_str = date.today().isoformat()

# CLI argument parser
parser= argparse.ArgumentParser(description="Moody the Mood Monster - Mood Charts")
parser.add_argument("--top3", action="store_true", help="Generate Top 3 Mood Trends chart")
parser.add_argument("--bar", action="store_true", help="Generate Mood Frequency bar chart")
args = parser.parse_args()


# Dynamically get the path to mood_log.csv
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, '..', 'mood_log.csv')

# Define exports folder
EXPORTS_DIR = os.path.join(BASE_DIR, 'exports')

# If exports does not exist yet, create it
os.makedirs(EXPORTS_DIR, exist_ok=True)

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

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date']).dt.date

# Group by date and mood
daily_moods = df.groupby(['date', 'mood']).size().unstack(fill_value=0)

# fill missing dates
full_index = pd.date_range(start=df['date'].min(), end=df['date'].max())
daily_moods.index = pd.to_datetime(daily_moods.index)
daily_moods = daily_moods.reindex(full_index, fill_value=0)

# --- Top 3 Mood Trends Chart --- #
if args.top3 or (not args.top3 and not args.bar):
    print("📋 Running: Top 3 Mood Trends chart")


    # Find top 3 moods:
    top_moods = df['mood'].value_counts().nlargest(3).index

    # Filter trend data for top 3 moods:
    filtered = daily_moods[top_moods]

    # Plot top 3 mood trends
    ax = filtered.plot(figsize=(10, 6), marker='o', linewidth=2, alpha=0.7)

    plt.title(f'Top 3 Mood Trends Over Time for {USER_NAME}')
    plt.xlabel('Date')
    plt.ylabel('Mood Count')
    plt.legend(title="Mood")
    plt.grid(True)
    plt.tight_layout()

    # Save with date
    plt.savefig(os.path.join(EXPORTS_DIR, f'mood_trends_top3_{today_str}.png'))
    print(f"✅ Saved: mood_trends_top3_{today_str}.png")
    plt.show()
    
    print("🎉 All done! Charts saved to exports folder.")

# --- Mood Frequency Bar Chart ---
if args.bar or (not args.top3 and not args.bar):
    print("📋 Running: Mood Frequency bar chart")
 
    # Count each mood
    mood_counts = df['mood'].value_counts()

    # Plot as a bar chart
    plt.figure(figsize=(8, 5))
    mood_counts.plot(kind='bar')
    plt.title(f'Mood Frequency for {USER_NAME}')
    plt.xlabel('Mood')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save with date
    plt.savefig(os.path.join(EXPORTS_DIR, f'mood_frequency_{today_str}.png'))
    print(f"✅ Saved: mood_frequency_{today_str}.png")
    plt.show()
    
    print("🎉 All done! Charts saved to exports folder.")