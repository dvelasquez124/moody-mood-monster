import pandas as pd
import plotly.express as px

# Load mood log
df = pd.read_csv("mood_log.csv", parse_dates=["date"])

# Sort dates
df = df.sort_values(by="date")

# Get top 3 most frequent moods
top3 = df["mood"].value_counts().nlargest(3).index.to_list()

# Filter data to only include top 3 moods
df_top3 = df[df["mood"].isin(top3)]

print("Top 3 moods:" , top3)
print(df_top3.head())

fig = px.line(
    df_top3,
    x="date",
    y="mood",
    color="mood", # separate line per mood
    markers=True,
    title="Top 3 Mood Trends"
)

fig.write_html("top3_mood_trends.html")
print("✅ Chart saved! Open top3_mood_trends.html in browser.")