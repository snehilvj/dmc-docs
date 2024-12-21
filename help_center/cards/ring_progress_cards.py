

import dash_mantine_components as dmc
from dash import Dash, _dash_renderer
from dash_iconify import DashIconify
_dash_renderer._set_react_version("18.2.0")

app = Dash(external_stylesheets=dmc.styles.ALL)

icons = {
    'up': "tabler:arrow-up-right",
    'down': "tabler:arrow-down-right",
}

data = [
    {'label': 'Page views', 'stats': '456,578', 'progress': 65, 'color': 'teal', 'icon': 'up'},
    {'label': 'New users', 'stats': '2,550', 'progress': 72, 'color': 'blue', 'icon': 'up'},
    {'label': 'Orders', 'stats': '4,735', 'progress': 52, 'color': 'red', 'icon': 'down'},
]

def StatsRing():
    stats = []
    for stat in data:
        Icon = icons[stat['icon']]
        stats.append(
            dmc.Paper(
                children=[
                    dmc.Group(
                        children=[
                            dmc.RingProgress(
                                size=80,
                                roundCaps=True,
                                thickness=8,
                                sections=[{'value': stat['progress'], 'color': stat['color']}],
                                label=dmc.Center(
                                    DashIconify(icon=Icon, width=20, height=20)
                                )
                            ),
                            dmc.Box(
                                children=[
                                    dmc.Text(stat['label'], c="dimmed", size="xs", tt="uppercase", fw=700),
                                    dmc.Text(stat['stats'], fw=700, size="xl"),
                                ]
                            )
                        ]
                    )
                ],
                withBorder=True,
                radius="md",
                p="xs",
            )
        )

    return dmc.SimpleGrid(
        children=stats,
        cols={"base": 1, "sm": 3},
        p="lg"
    )


app.layout = dmc.MantineProvider(
    StatsRing()
)


if __name__ == "__main__":
    app.run_server(debug=True)