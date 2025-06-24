import pandas as pd
import plotly.express as px

# Load mood log
df = pd.read_csv("mood_log.csv", parse_dates=["date"])

# Sort dates
df = df.sort_values(by="date")

# Simple line chart: mood score over time
fig = px.line(
    df,
    x="date",
    y="mood",
    title="Mood Score Over Time"
)

# Save HTML
fig.write_html("mood_test_plotly_chart.html")
print("Chart saved! Open mood_test_plotly_chart.html in browser")