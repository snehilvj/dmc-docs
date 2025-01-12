import dash_mantine_components as dmc
from dash import Dash, _dash_renderer
_dash_renderer._set_react_version("18.2.0")

app = Dash(external_stylesheets=dmc.styles.ALL)

layout = dmc.Box([
    dmc.Title("Checkbox Add Custom Sizes Demo"),
    dmc.Text("To add custom sizes to Checkbox, define a class in the .css file in /assets using the data-size attribute. "),
    dmc.Text("Add the new sizes to the `theme` so they available in all Checkbox components in your app.", mb="md"),
    dmc.Box([
        dmc.Checkbox(
            label="Extra small checkbox",
            size="xxs",
        ),
        dmc.Checkbox(
            label="Extra extra large checkbox",
            size="xxl",
            mt="md"
        ),
    ])
], p="lg")

app.layout = dmc.MantineProvider(
   children=layout,
    theme={
        "components": {
            "Checkbox": {"classNames": {
                "root": "checkbox-add-custom-sizes-root",
                "label": "checkbox-add-custom-sizes-label"
            }}
        }
    }
)

if __name__ == "__main__":
    app.run(debug=True, port=8053)