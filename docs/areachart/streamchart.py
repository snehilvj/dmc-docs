import dash_mantine_components as dmc

data = [
    {"month": "Jan", "Apples": 220, "Oranges": 140, "Tomatoes": 90, "Grapes": 60},
    {"month": "Feb", "Apples": 260, "Oranges": 180, "Tomatoes": 120, "Grapes": 90},
    {"month": "Mar", "Apples": 300, "Oranges": 240, "Tomatoes": 180, "Grapes": 140},
    {"month": "Apr", "Apples": 340, "Oranges": 320, "Tomatoes": 260, "Grapes": 200},
    {"month": "May", "Apples": 380, "Oranges": 420, "Tomatoes": 360, "Grapes": 280},
    {"month": "Jun", "Apples": 420, "Oranges": 520, "Tomatoes": 460, "Grapes": 360},
    {"month": "Jul", "Apples": 400, "Oranges": 560, "Tomatoes": 520, "Grapes": 420},
    {"month": "Aug", "Apples": 360, "Oranges": 520, "Tomatoes": 560, "Grapes": 460},
    {"month": "Sep", "Apples": 300, "Oranges": 440, "Tomatoes": 520, "Grapes": 420},
    {"month": "Oct", "Apples": 260, "Oranges": 340, "Tomatoes": 440, "Grapes": 360},
    {"month": "Nov", "Apples": 220, "Oranges": 260, "Tomatoes": 340, "Grapes": 280},
    {"month": "Dec", "Apples": 200, "Oranges": 200, "Tomatoes": 260, "Grapes": 200},
]

component = dmc.AreaChart(
    h=300,
    data=data,
    dataKey="month",
    type="stream",
    series=[
        {"name": "Apples", "color": "indigo.6"},
        {"name": "Oranges", "color": "blue.6"},
        {"name": "Tomatoes", "color": "teal.6"},
        {"name": "Grapes", "color": "grape.6"},
    ],
)