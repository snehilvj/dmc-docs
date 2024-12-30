import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import Dash, _dash_renderer
_dash_renderer._set_react_version("18.2.0")

app = Dash(external_stylesheets=dmc.styles.ALL)

layout = dmc.Box([
    dmc.Title("ActionIcon Custom Variants Demo"),
    dmc.Text("To add new ActionIcon variants, define a class in the .css using the data-variant attribute. "),
    dmc.Text("Add the new variants to the `theme` so they available in all `ActionIcon` components in your app.", mb="md"),
    dmc.Group([

        dmc.ActionIcon(
            DashIconify(icon="tabler:heart", width=18, height=18),
            variant="danger",
        ),
        dmc.ActionIcon(
            DashIconify(icon="tabler:heart", width=18, height=18),
            variant="primary",
        ),
    ])
])

app.layout = dmc.MantineProvider(
   children=layout,
    theme={
        "components": {
            "ActionIcon": {"classNames": {"root": "ai-custom-variants"}}
        }
    }
)

if __name__ == "__main__":
    app.run(debug=True)