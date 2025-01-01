import dash_mantine_components as dmc
from dash import Dash, _dash_renderer
_dash_renderer._set_react_version("18.2.0")

app = Dash(external_stylesheets=dmc.styles.ALL)


app.layout = dmc.MantineProvider(
    dmc.Button("click button to see focus ring", m="lg"),
    theme={
        "focusClassName": "focus"
    }
)

if __name__ == "__main__":
    app.run(debug=True)