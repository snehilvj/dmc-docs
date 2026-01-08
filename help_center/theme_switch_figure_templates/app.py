
import dash_mantine_components as dmc
from dash import Dash, dcc, Input, Output, State, callback, clientside_callback, _dash_renderer, Patch, ALL
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

graphs = dcc.Loading(dmc.Grid(
    [
        make_graph_card(bar_fig, "bar"),
        make_graph_card(scatter_fig, "scatter"),
        make_graph_card(line_fig, "line"),
        make_graph_card(map_fig, "map")
    ],
    gutter="xl",
    style={"height": 800}
),delay_hide=1000 )

sample_controls = dmc.Box([
    dmc.Button("sample button"),
    dmc.Button("sample red button", color="red"),
    dmc.Button("sample yellow button", color="yellow"),
    dmc.Slider(value=25, my="lg"),
], w=600)

theme_toggle = dmc.Switch(
    offLabel=DashIconify(icon="radix-icons:sun", width=15, color= "var(--mantine-color-yellow-8)"),
    onLabel=DashIconify(icon="radix-icons:moon", width=15, color= "var(--mantine-color-yellow-6)"),
    id="color-scheme-toggle",
    persistence=True,
    color="grey",
)

layout = dmc.Container([
    dmc.Group([
        dmc.Title("Figure Template Demo", my="md"),
        theme_toggle,
    ], justify="space-between"),
    sample_controls,
    graphs
], fluid=True)


app= Dash(external_stylesheets=dmc.styles.ALL)

app.layout = dmc.MantineProvider(layout)

clientside_callback(
    """ 
    (switchOn) => {
       document.documentElement.setAttribute('data-mantine-color-scheme', switchOn ? 'dark' : 'light');  
       return window.dash_clientside.no_update
    }
    """,
    Output("color-scheme-toggle", "id"),
    Input("color-scheme-toggle", "checked"),
)


@callback(
    Output({"index": ALL}, "figure"),
    Input("color-scheme-toggle", "checked"),
    State({"index": ALL}, "id"),
)
def update_figure(switch_on, ids):
    # template must be template object rather than just the template string name
    template = pio.templates["mantine_dark"] if switch_on else pio.templates["mantine_light"]
    patched_figures = []
    for i in ids:
        patched_fig = Patch()
        patched_fig["layout"]["template"] = template
        patched_figures.append(patched_fig)

    return patched_figures

if __name__ == "__main__":
    app.run(debug=True)

