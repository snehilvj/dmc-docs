import dash_mantine_components as dmc
from dash import Dash, _dash_renderer
_dash_renderer._set_react_version("18.2.0")

app = Dash(external_stylesheets=dmc.styles.ALL)

layout = dmc.Box([
    dmc.Title("Button  Custom Variants Demo"),
    dmc.Text("To add new Button variants, define a class in the .css file in /assets using the data-variant attribute. "),
    dmc.Text("Add the new variants to the `theme` so they available in all `Button` components in your app.", mb="md"),
    dmc.Group([

        dmc.Button(
            "Danger Variant",
            variant="danger",
        ),
        dmc.Button(
            "Pimary Variant",
            variant="primary",
        ),
    ])
])

app.layout = dmc.MantineProvider(
   children=layout,
    theme={
        "components": {
            "Button": {"classNames": {"root": "button-custom-variants"}}
        }
    }
)

if __name__ == "__main__":
    app.run(debug=True)