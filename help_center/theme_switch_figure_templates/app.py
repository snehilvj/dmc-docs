
import dash_mantine_components as dmc
from dash import Dash, dcc, Input, Output, State, callback, _dash_renderer, Patch, ALL
import plotly.express as px
import plotly.io as pio
from dash_iconify import DashIconify
_dash_renderer._set_react_version("18.2.0")

dmc.add_figure_templates(default="mantine_dark")

df = px.data.gapminder()

line_fig = px.line(
    df.query("1952 <= year <= 1982 & continent != 'Asia'"),
    x="year",
    y="gdpPercap",
    color="continent",
    line_group="country"
)

dff = df[df.year == 2007]
scatter_fig = px.scatter(
    dff,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    log_x=True,
    size_max=60,
    title=f"2007 GDP per Capita vs Life Expectancy, Sized by Population ",
)


avg_lifeExp = (dff["lifeExp"] * dff["pop"]).sum() / dff["pop"].sum()
map_fig = px.choropleth(
    dff,
    locations="iso_alpha",
    color="lifeExp",
    title="%.0f World Average Life Expectancy was %.1f years" % (2007, avg_lifeExp),
)

bar_fig = px.bar(dff, x="continent", y="pop", title="2007 Population by Continent")

def make_graph_card(fig, index):
    return dmc.GridCol(
        dmc.Card(dcc.Graph(figure=fig, id={"index": index}), withBorder=True),
        span={"base": 12, "md": 6}
    )

graphs = dmc.Grid(
    [
        make_graph_card(bar_fig, "bar"),
        make_graph_card(scatter_fig, "scatter"),
        make_graph_card(line_fig, "line"),
        make_graph_card(map_fig, "map")
    ],
    gutter="xl",
)

sample_controls = dmc.Box([
    dmc.Button("sample button"),
    dmc.Button("sample red button", color="red"),
    dmc.Button("sample yellow button", color="yellow"),
    dmc.Slider(value=25, my="lg"),
], w=600)


theme_toggle = dmc.Affix(
    dmc.ActionIcon(
        [
            dmc.Paper(DashIconify(icon="radix-icons:sun", width=25), darkHidden=True),
            dmc.Paper(DashIconify(icon="radix-icons:moon", width=25), lightHidden=True),
        ],
        variant="transparent",
        color="yellow",
        id="color-scheme-toggle",
        size="lg",
        ms="auto",
    ),
    position={"top": 10, "right": 10}
)

layout = dmc.Container([
    dmc.Title("Figure Template Demo", my="md"),
    theme_toggle,
    sample_controls,
    graphs
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
    Output({"index": ALL}, "figure"),
    Input("mantine-provider", "forceColorScheme"),
    State({"index": ALL}, "id"),
)
def update_figure(theme, ids):
    # template must be template object rather than just the template string name
    template = pio.templates["mantine_light"] if theme == "light" else pio.templates["mantine_dark"]
    patched_figures = []
    for i in ids:
        patched_fig = Patch()
        patched_fig["layout"]["template"] = template
        patched_figures.append(patched_fig)

    return patched_figures

if __name__ == "__main__":
    app.run(debug=True)

