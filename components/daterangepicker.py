import dash_mantine_components as dmc
from dash import html

title = "DateRangePicker"
doc = dmc.DateRangePicker.__doc__

layout = html.Div(
    children=[
        dmc.Text("Interactive Demo", color="dimmed"),
        dmc.Space(h=10),
        dmc.Paper(
            withBorder=True,
            padding="md",
            children=[
                dmc.Grid(
                    align="stretch",
                    children=[
                        dmc.Col(
                            children=[
                                dmc.Center(
                                    dmc.DateRangePicker(
                                        id="daterangepicker-demo",
                                        dates=["2020-09-06", "2020-09-26"],
                                        format="ddd DD MMM, YY",
                                    ),
                                    style={"height": 140},
                                )
                            ],
                            span=7,
                        ),
                        dmc.Col(
                            children=[
                                dmc.Center(
                                    dmc.Group(
                                        direction="column",
                                        grow=True,
                                        children=[
                                            dmc.Group(
                                                position="apart",
                                                children=[
                                                    dmc.Text(
                                                        "Dropdown Type", size="sm"
                                                    ),
                                                    dmc.SegmentedControl(
                                                        id="dropdown-daterangepicker-demo",
                                                        value="popover",
                                                        size="sm",
                                                        data=[
                                                            {
                                                                "value": "popover",
                                                                "label": "Popover",
                                                            },
                                                            {
                                                                "value": "modal",
                                                                "label": "Modal",
                                                            },
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            dmc.Group(
                                                position="apart",
                                                children=[
                                                    dmc.Anchor(
                                                        "Date Format",
                                                        size="sm",
                                                        href="https://day.js.org/docs/en/display/format",
                                                        target="_blank",
                                                    ),
                                                    dmc.TextInput(
                                                        id="format-daterangepicker-demo",
                                                        value="ddd DD MMM, YY",
                                                    ),
                                                ],
                                            ),
                                            dmc.Group(
                                                position="apart",
                                                children=[
                                                    dmc.Text(
                                                        "Amount of Months", size="sm"
                                                    ),
                                                    dmc.TextInput(
                                                        id="amount-daterangepicker-demo",
                                                        type="number",
                                                        value="1",
                                                    ),
                                                ],
                                            ),
                                        ],
                                    )
                                )
                            ],
                            span=5,
                        ),
                    ],
                )
            ],
        ),
    ]
)
