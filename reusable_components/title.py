import dash_mantine_components as dmc
from dash import html, dcc


def Title(s):
    return dmc.Title(s, order=5, class_name="space-below-10")


def SubText(s):
    return dmc.Text(s, color="gray", class_name="space-below-20")


def ComponentName(name):
    return dmc.Text(name, style={"fontSize": 40, "fontWeight": 300})


def ComponentDescription(desc):
    desc, link = desc.split("For more information, see: ")
    return dmc.Text(
        [
            desc,
            dcc.Link(
                [html.I(className="bi bi-box-arrow-up-right")],
                href=link.strip(),
                target="_blank",
            ),
        ],
        color="gray",
        class_name="space-below-20",
    )
