import dash_mantine_components as dmc
from dash import dcc
import plotly.express as px

df = px.data.gapminder()
dff = df[df.year == 2007]

component = dmc.SimpleGrid(
    [
        dcc.Graph(figure=px.bar(dff, x="continent", y="pop", template="plotly_white", title="plotly_white theme")),
        dcc.Graph(figure=px.bar(dff, x="continent", y="pop", template="plotly_dark", title="plotly_dark theme"))
    ],
    cols=2
)
