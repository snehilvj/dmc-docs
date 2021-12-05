from dash import html
from utils import create_component_title
import dash_mantine_components as dmc

paper = html.Div(
    [
        create_component_title("Paper"),
        dmc.Center(
            [
                html.Div(
                    style={"width": 340, "margin": "auto"},
                    children=[
                        dmc.Paper(
                            shadow="sm",
                            padding=20,
                            children=[
                                dmc.Image(
                                    src="https://images.unsplash.com/photo-1527004013197-933c4bb611b3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=720&q=80",
                                    height=160,
                                    width=340,
                                    alt="Norway",
                                    style={
                                        "marginTop": "-20px",
                                        "marginLeft": "-20px",
                                        "marginBottom": "20px",
                                    },
                                ),
                                dmc.Group(
                                    position="apart",
                                    style={"marginBottom": 5, "marginTop": 5},
                                    children=[
                                        dmc.Text("Norway Fjord Adventures", weight=500),
                                        dmc.Badge(
                                            "On Sale", color="pink", variant="light"
                                        ),
                                    ],
                                ),
                                dmc.Text(
                                    " With Fjord Tours you can explore more of the magical fjord landscapes with tours and activities on and around the fjords of Norway",
                                    size="sm",
                                    style={"lineHeight": 1.5},
                                ),
                                dmc.Button(
                                    "Book classic tour now",
                                    color="blue",
                                    variant="light",
                                    fullWidth=True,
                                    style={"marginTop": 14},
                                ),
                            ],
                        )
                    ],
                )
            ], style={"background": "#f8f9fa", "padding": 20}
        ),dmc.Space(h=30)
    ],
)