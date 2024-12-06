
import dash_mantine_components as dmc
from dash import  dcc, Input, Output, State, callback, Patch, ALL
import plotly.express as px
import plotly.io as pio

dmc.add_figure_templates(default="mantine_light")

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

bar_fig = px.bar(dff, x="continent", y="pop", title="Population by Continent")

graphs = dmc.Grid(
    [
        dmc.GridCol(dcc.Graph(figure=bar_fig, id={"type": "graph", "index": "bar"}), span={"base": 12, "md":6}),
        dmc.GridCol(dcc.Graph(figure=scatter_fig, id={"type": "graph", "index": "scatter"}), span={"base": 12, "md":6}),
        dmc.GridCol(dcc.Graph(figure=line_fig, id={"type": "graph", "index": "line"}), span={"base": 12, "md":6}),
        dmc.GridCol(dcc.Graph(figure=map_fig, id={"type": "graph", "index": "map"}), span={"base": 12, "md":6}),
    ],
    gutter="xl",
)

sample_controls = dmc.Box([
    dmc.Button("sample button"),
    dmc.Button("sample red button", color="red"),
    dmc.Button("sample yellow button", color="yellow"),
    dmc.Slider(value=25, my="lg"),
], w=600)

# used in the children prop of  MantinePovider([], id="m2d-mantine-provider)
component = dmc.Box([sample_controls, graphs])

@callback(
    Output({"type": "graph", "index": ALL}, "figure"),
    Input("m2d-mantine-provider", "forceColorScheme"),
    State({"type": "graph", "index": ALL}, "id"),
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
