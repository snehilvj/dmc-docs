import dash_mantine_components as dmc
from dash import dcc, Input, Output, callback
import plotly.express as px

df = px.data.gapminder()
dff = df[df.year == 2007]

dmc.add_figure_templates()

component = dcc.Graph(id="figure-templates-histogram")

@callback(
    Output("figure-templates-histogram", "figure"),
    Input("m2d-mantine-provider", "forceColorScheme"),
)
def update_figure(theme):
    return px.histogram(dff, x='lifeExp', title='2007 Life Expectancy', template=f"mantine_{theme}")