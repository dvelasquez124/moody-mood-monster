import plotly.express as px

# Load example dataset
df = px.data.gapminder().query("year == 2007")

# Create interactive scatter plot
fig = px.scatter(
    df,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    title="Gapminder Test Chart (2007)"
)

# Save as HTML file
fig.write_html("test_plotly_chart.html")
print("Chart saved! Open test_plotly_chart.html in your browser.")