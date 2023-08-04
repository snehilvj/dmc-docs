import dash_mantine_components as dmc
from dash import html


def create_toc(data):
    children = []
    for url, name, _ in data:
        children.append(
            html.A(
                dmc.Text(name, color="dimmed", size="sm", variant="text"),
                style={"textTransform": "capitalize", "textDecoration": "none"},
                href=url,
            )
        )

    heading = dmc.Text("Table of Contents", mb=10, weight=500) if children else None

    ad = html.Div(
        **{
            "data-ea-publisher": "dash-mantine-componentscom",
            "data-ea-manual": True,
            "data-ea-type": "text",
        },
        className="flat",
        style={"marginBottom": 25, "marginLeft": -15}
    )

    toc = dmc.Stack([ad, heading, *children], spacing=4, px=25, mt=20)

    return dmc.Aside(
        position={"top": 70, "right": 0},
        fixed=True,
        id="toc-navbar",
        width={"base": 300},
        zIndex=10,
        children=toc,
        withBorder=False,
    )
