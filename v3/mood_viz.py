import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date


# User settings
USER_NAME = "Diana"

# Store today's date
today_str = date.today().isoformat()

# Mood colors dictionary
MOOD_COLORS = {
    "happy": "#FFD700",    # gold/yellow
    "sad": "#1E90FF",      # dodger blue
    "tired": "#A9A9A9",    # dark gray
    "angry": "#FF4500",    # orange-red
    "anxious": "#8A2BE2",  # blue violet
    "calm": "#3CB371",     # medium sea green
    "excited": "#FF69B4",  # hot pink
    "mad": "#FF6347",      # tomato red
    "meh": "#808080",      # gray
    "confused": "#9370DB", # medium purple
    "okay": "#20B2AA"      # light sea green
}

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

# fill in missing days with 0s
full_index = pd.date_range(start=df['date'].min(), end=df['date'].max())
daily_moods.index = pd.to_datetime(daily_moods.index)
daily_moods = daily_moods.reindex(full_index, fill_value=0)

# Get mood columns that are in the color dict (ignore unknown moods for now)
mood_columns =[mood for mood in daily_moods.columns if mood in MOOD_COLORS]

# Build color list
colors = [MOOD_COLORS[mood] for mood in mood_columns]

# Plot mood trends over time (line chart)
ax = daily_moods[mood_columns].plot(figsize=(10, 6), marker='o', linewidth=2, alpha=0.7, color=colors)

plt.title(f'Mood Trends Over Time for {USER_NAME}')
plt.xlabel('Date')
plt.ylabel('Mood Count')
plt.legend(title="Mood")
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(EXPORTS_DIR, f'mood_trends_{today_str}.png'))
plt.show()



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
plt.savefig(os.path.join(EXPORTS_DIR, f'mood_frequency_{today_str}.png'))
plt.show()