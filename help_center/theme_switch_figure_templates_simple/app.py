
import dash_mantine_components as dmc
from dash import Dash, dcc, Input, Output, State, callback, _dash_renderer, Patch
import plotly.express as px
import plotly.io as pio
from dash_iconify import DashIconify
_dash_renderer._set_react_version("18.2.0")

dmc.add_figure_templates(default="mantine_dark")

df = px.data.gapminder()
dff = df[df.year == 2007]

graph = dcc.Graph(figure=px.bar(dff, x="continent", y="pop", title="2007 Population by Continent"), id="graph")

theme_toggle = dmc.ActionIcon(
    [
        dmc.Paper(DashIconify(icon="radix-icons:sun", width=25), darkHidden=True),
        dmc.Paper(DashIconify(icon="radix-icons:moon", width=25), lightHidden=True),
    ],
    variant="transparent",
    color="yellow",
    id="color-scheme-toggle",
    size="lg",
)


layout = dmc.Container([
    dmc.Group([
        dmc.Title("Figure Template Demo", my="md"),
        theme_toggle,
    ], justify="space-between"),
    graph
], fluid=True)


app= Dash(external_stylesheets=dmc.styles.ALL)

app.layout = dmc.MantineProvider(
    layout,
    forceColorScheme="dark",
    id="mantine-provider"
)


@callback(
    Output("mantine-provider", "forceColorScheme"),
    Input("color-scheme-toggle", "n_clicks"),
    State("mantine-provider", "forceColorScheme"),
    prevent_initial_call=True,
)
def switch_theme(_, theme):
    return "dark" if theme == "light" else "light"

@callback(
    Output("graph", "figure"),
    Input("mantine-provider", "forceColorScheme"),
)
def update_figure(theme):
    # template must be template object rather than just the template string name
    template = pio.templates["mantine_light"] if theme == "light" else pio.templates["mantine_dark"]
    patched_fig = Patch()
    patched_fig["layout"]["template"] = template
    return patched_fig

if __name__ == "__main__":
    app.run(debug=True)


