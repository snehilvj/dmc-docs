import dash_mantine_components as dmc

component = dmc.Highlight(
    "You can change styles of highlighted part if you do not like default styles",
    ta="center",
    highlight=["highlighted", "default"],
    highlightStyles={
        "backgroundImage": "linear-gradient(45deg, var(--mantine-color-cyan-5), var(--mantine-color-indigo-5))",
        "fontWeight": 500,
        "WebkitBackgroundClip": "text",
        "WebkitTextFillColor": "transparent",
    },
)
