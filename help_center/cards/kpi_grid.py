import dash_mantine_components as dmc
from dash import Dash, _dash_renderer, html
from dash_iconify import DashIconify

_dash_renderer._set_react_version("18.2.0")

app = Dash(external_stylesheets=dmc.styles.ALL)

icons = {
    'user': "tabler:user-plus",
    'discount': "tabler:discount-2",
    'receipt': "tabler:receipt-2",
    'coin': "tabler:coin",
}

data = [
    {'title': 'Revenue', 'icon': 'receipt', 'value': '13,456', 'diff': 34},
    {'title': 'Profit', 'icon': 'coin', 'value': '4,145', 'diff': -13},
    {'title': 'Coupons usage', 'icon': 'discount', 'value': '745', 'diff': 18},
    {'title': 'New customers', 'icon': 'user', 'value': '188', 'diff': -30},
]

def StatsGrid():
    stats = []
    for stat in data:
        Icon = icons[stat['icon']]
        DiffIcon = "tabler:arrow-up-right" if stat['diff'] > 0 else "tabler:arrow-down-right"

        stats.append(
            dmc.Paper(
                children=[
                    dmc.Group(
                        children=[
                            dmc.Text(stat['title'], c="dimmed", tt="uppercase", fw=700),
                            DashIconify(icon=Icon)
                        ],
                        justify="space-between"
                    ),
                    dmc.Group(
                        children=[
                            dmc.Text(stat['value'], size="lg", fw=700),
                            dmc.Group(
                                [
                                    dmc.Text(f"{stat['diff']}%", size="xs"),
                                    DashIconify(icon=DiffIcon, height=16)
                                ],
                                c="teal" if stat['diff'] > 0 else "red",
                                fw=500,
                                gap=0,
                            )
                        ],
                        gap="xs",
                        mt=25
                    ),
                    dmc.Text("Compared to previous month", size="xs", c="dimmed", mt=7)
                ],
                withBorder=True,
                p="md",
                radius="md",
            )
        )

    return dmc.SimpleGrid(
        children=stats,
        cols={"base": 1, "xs": 2, "md": 4},
        m="xl"
    )


app.layout = dmc.MantineProvider(
    StatsGrid()
)

if __name__ == "__main__":
    app.run(debug=True)