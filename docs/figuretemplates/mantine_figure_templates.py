import dash_mantine_components as dmc
from dash import dcc
import plotly.express as px

df = px.data.gapminder()
dff = df[df.year == 2007]

dmc.add_figure_templates()


component = dmc.SimpleGrid(
    [
        dcc.Graph(figure=px.bar(dff, x="continent", y="pop", template="mantine_light", title="matine_light theme" )),
        dcc.Graph(figure=px.bar(dff, x="continent", y="pop", template="mantine_dark",  title="mantine_dark theme"))
    ],
    cols=2
)