import dash_mantine_components as dmc

colors = dmc.DEFAULT_THEME["colors"]

component= dmc.SimpleGrid([
    dmc.Card([
        dmc.Box(h=100, w=100, bg=f"{c}.{i}" ),
        dmc.Text(f"{c} {i}", size="sm"),
        dmc.Text(f"{colors[c][i]}", size="sm", c="dimmed")
    ])  for c in list(colors) for i in range(10)
], cols={ "base": 5,  "lg": 10 }, spacing="xs")

