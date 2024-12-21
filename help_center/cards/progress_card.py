
import dash_mantine_components as dmc
from dash import Dash, _dash_renderer
_dash_renderer._set_react_version("18.2.0")

app = Dash(external_stylesheets=dmc.styles.ALL)

component = dmc.Card(
        children=[
            dmc.Text("Monthly goal", fz="xs", tt="uppercase", fw=700, c="dimmed"),
            dmc.Text("$5.431 / $10.000", fz="lg", fw=500),
            dmc.Progress(value=54.31, mt="md", size="lg", radius="xl"),
        ],
        withBorder=True,
        radius="md",
        padding="xl",
        w=400, m="lg"
    )



app.layout = dmc.MantineProvider(
    component
)

if __name__ == "__main__":
    app.run(debug=True)

