import dash_mantine_components as dmc
from dash import Dash, _dash_renderer
_dash_renderer._set_react_version("18.2.0")

app = Dash(external_stylesheets=dmc.styles.ALL)

layout= dmc.Group([
    dmc.Button(f"button", color=f"blue.{i}") for i in range(10)
])

app.layout = dmc.MantineProvider(
    layout,
    theme={
        "luminanceThreshold": .45,
        "autoContrast": True
    }
)

if __name__ == "__main__":
    app.run(debug=True)