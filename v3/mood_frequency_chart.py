import pandas as pd
import plotly.express as px

# Load mood log
df = pd.read_csv("mood_log.csv", parse_dates=["date"])

# Count how often each mood appears 
mood_counts = df["mood"].value_counts().reset_index()
mood_counts.columns = ["mood", "count"]

# Create interactive bar chart
fig = px.bar(
   mood_counts,
   x="mood",
   y="count",
   title="Mood Frequency",
   labels={"mood": "Mood", "count": "Count"}
)

# Save as HTML file
fig.write_html("mood_frequency_plotly.html")
print("✅ Chart saved! Open mood_frequency_plotly.html in browser.")