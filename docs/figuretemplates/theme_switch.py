import dash_mantine_components as dmc
from dash import dcc, Input, Output, callback
import plotly.express as px

df = px.data.gapminder()
dff = df[df.year == 2007]

dmc.add_figure_templates()

# Theme switch in the dmc-docs header:
# dmc.Switch(
#     offLabel=DashIconify(icon="radix-icons:sun", width=15, color= "var(--mantine-color-yellow-8)"),
#     onLabel=DashIconify(icon="radix-icons:moon", width=15, color= "var(--mantine-color-yellow-6)"),
#     id="docs-color-scheme-switch",
#     persistence=True,
#     color="grey",
# )
component = dcc.Graph(id="figure-templates-histogram")

@callback(
    Output("figure-templates-histogram", "figure"),
    Input("docs-color-scheme-switch", "checked"),
)
def update_figure(switch_on):
    template = "mantine_dark" if switch_on else "mantine_light"
    return px.bar(dff, x="continent", y="pop", title="Population by Continent", template=template)
