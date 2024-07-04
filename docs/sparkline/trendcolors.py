import dash_mantine_components as dmc
from dash import html

positive_trend = [10, 20, 40, 20, 40, 10, 50]
negative_trend = [50, 40, 20, 40, 20, 40, 10]
neutral_trend = [10, 20, 40, 20, 40, 10, 50, 5, 10]


def make_sparkline(trend):
    return dmc.Sparkline(
        w=200,
        h=60,
        data=trend,
        trendColors={"positive": "teal.6", "negative": "red.6", "neutral": "gray.5"},
        fillOpacity=0.2,
    )


component = dmc.Stack(
    [
        dmc.Text("Positive Trend"),
        make_sparkline(positive_trend),
        dmc.Text("Negative Trend", mt="md"),
        make_sparkline(negative_trend),
        dmc.Text("Neutral Trend", mt="md"),
        make_sparkline(neutral_trend),
    ],
    gap="md",
)
