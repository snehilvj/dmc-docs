import dash_mantine_components as dmc
from dash import dcc

component = dcc.RangeSlider(0, 200, value=[50, 150], className="dmc")