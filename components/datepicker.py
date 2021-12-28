import dash_mantine_components as dmc
from dash import html

title = "DatePicker"
doc = dmc.DatePicker.__doc__

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
                                    dmc.DatePicker(
                                        id="datepicker-demo",
                                        date="1996-08-21",
                                        format="ddd DD MMM, YY",
                                        label="Datepicker",
                                    ),
                                    style={"height": 190},
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
                                                        id="dropdown-datepicker-demo",
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
                                                        id="format-datepicker-demo",
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
                                                        id="amount-datepicker-demo",
                                                        type="number",
                                                        value="1",
                                                    ),
                                                ],
                                            ),
                                            dmc.Group(
                                                position="apart",
                                                children=[
                                                    dmc.Text(
                                                        "Initial Level", size="sm"
                                                    ),
                                                    dmc.SegmentedControl(
                                                        id="initial-datepicker-demo",
                                                        value="date",
                                                        size="sm",
                                                        data=[
                                                            {
                                                                "value": "date",
                                                                "label": "Date",
                                                            },
                                                            {
                                                                "value": "month",
                                                                "label": "Month",
                                                            },
                                                            {
                                                                "value": "year",
                                                                "label": "Year",
                                                            },
                                                        ],
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
