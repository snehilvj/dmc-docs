import dash_mantine_components as dmc
from dash import dcc, Input, Output, callback
import plotly.express as px

df = px.data.gapminder()
dff = df[df.year == 2007]

dmc.add_figure_templates()

# Theme switch in the dmc-docs header:
# dmc.ColorSchemeToggle(
#     lightIcon=DashIconify(icon="radix-icons:sun", width=20),
#     darkIcon=DashIconify(icon="radix-icons:moon", width=20),
#     variant="light",
#     color="gray",
#     id="docs-color-scheme-switch",
# )
component = dcc.Graph(id="figure-templates-histogram")

@callback(
    Output("figure-templates-histogram", "figure"),
    Input("docs-color-scheme-switch", "computedColorScheme"),
)
def update_figure(color):
    template = "mantine_dark" if color=="dark" else "mantine_light"
    return px.bar(dff, x="continent", y="pop", title="Population by Continent", template=template)
