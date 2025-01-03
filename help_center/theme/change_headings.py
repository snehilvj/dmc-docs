import dash_mantine_components as dmc
from dash import Dash, _dash_renderer, Input, Output, State
_dash_renderer._set_react_version("18.2.0")

app = Dash(external_stylesheets=dmc.styles.ALL)

import dash_mantine_components as dmc

theme = {
    "components": {
        "Title": {
            "classNames": {
                "root": "change-heading-demo",
            },
        },
    },
}

app.layout = dmc.MantineProvider(
    theme=theme,
    children=[
        dmc.Title("Heading 1", order=1),
        dmc.Title("Heading 2", order=2),
        dmc.Title("Heading 3", order=3),
        dmc.Title("Heading 4", order=4),
        dmc.Title("Heading 5", order=5),
        dmc.Title("Heading 6", order=6),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)