from dash_iconify import DashIconify
import dash_mantine_components as dmc
from dash import callback, html, Input, Output

component = html.Div(
    [
        dmc.Text(id="menu-text", mb="md"),
        dmc.Menu(
            [
                dmc.MenuTarget(dmc.Button("Click for options!")),
                dmc.MenuDropdown(
                    [
                        dmc.MenuItem(
                            "External Link",
                            href="https://www.github.com/snehilvj",
                            target="_blank",
                            leftSection=DashIconify(icon="radix-icons:external-link"),
                        ),
                        dmc.MenuItem("Useless Button", id="useless-button", n_clicks=0),
                    ]
                ),
            ]
        ),
    ]
)


@callback(Output("menu-text", "children"), Input("useless-button", "n_clicks"))
def click_menu(n_clicks):
    return f"Clicked {n_clicks} times."
