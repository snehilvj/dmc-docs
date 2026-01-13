
import dash
from dash import Dash, html
import dash_mantine_components as dmc


app = Dash(use_pages=True, pages_folder="")


logo = "https://github.com/user-attachments/assets/c1ff143b-4365-4fd1-880f-3e97aab5c302"


def make_section(i, page):
    return dmc.Box(
        [
            dmc.Title(
                children=f"{page} Title {i}",
                id=str(i),
                order=3,
                mb=30,
                style={"scrollMarginTop": "60px"},
            ),
        ],
        p="lg",
    )


header = dmc.AppShellHeader(
    dmc.Group(
        [
            dmc.Image(src=logo, h=40, flex=0),
            dmc.Title("Demo App", c="blue"),
        ],
        h="100%",
        px="md",
    )
)

aside = dmc.AppShellAside(
    children=dmc.ScrollArea(
        dmc.Stack(
            [
                dmc.Title("Table of contents", order=5, mt=50),
                dmc.TableOfContents(
                    variant="filled",
                    color="blue",
                    size="sm",
                    radius="sm",
                    selector="#appshellmain :is( h2, h3, h4, h5, h6)",
                    offset=60,
                    id="toc",
                ),
            ]
        ),
        type="never",
    ),
    px="lg",
)

dash.register_page(
    "home",
    path="/",
    layout=html.Div([make_section(i, "home") for i in range(30)]),
)
dash.register_page(
    "page1",
    path="/page-1",
    layout=html.Div([make_section(i, "page1") for i in range(30)]),
)

app.layout = dmc.MantineProvider(
    children=dmc.AppShell(
        [
            header,
            dmc.AppShellNavbar(
                [
                    dmc.Title("Page Links", order=5),
                    dmc.NavLink(label="Home", href="/", id="home"),
                    dmc.NavLink(label="Page 1", href="/page-1", id="page-1"),
                ],
                p="md",
            ),
            dmc.AppShellMain(html.Div(dash.page_container, id="appshellmain")),
            aside,
        ],
        navbar={"width": 200},
        header={"height": 60},
    ),
)


if __name__ == "__main__":
    app.run(debug=True)
