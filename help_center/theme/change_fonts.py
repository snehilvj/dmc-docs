import dash_mantine_components as dmc
from dash import Dash, _dash_renderer, Input, Output
_dash_renderer._set_react_version("18.2.0")

app = Dash(external_stylesheets=dmc.styles.ALL)

component = dmc.Box([
    dmc.SegmentedControl(id="segment", data=["default", "custom-fonts"], value="default"),
    dmc.Box([
        dmc.Title("Greycliff CF title", order=3),
        dmc.Button("Verdana button"),
        dmc.Code("Monaco, Courier Code")
    ], bd=True, m="lg")
], m="lg")

theme= {
  "fontFamily": 'Verdana',
  "fontFamilyMonospace": 'Monaco, Courier, monospace',
  "headings": { "fontFamily": 'Greycliff CF' },
}

app.layout = dmc.MantineProvider(
    component,
    id="provider",
    forceColorScheme="light",
    theme=theme

)

@app.callback(
    Output("provider", "theme"),
    Input("segment", "value")
)
def update_font_theme(val):
    if val == "default":
        return {}
    return theme


if __name__ == "__main__":
    app.run(debug=True)