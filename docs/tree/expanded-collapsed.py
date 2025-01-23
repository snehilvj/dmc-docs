import dash_mantine_components as dmc
from dash_iconify import DashIconify
from .data import data

component = dmc.Tree(
    data=data,
    expandedIcon=DashIconify(icon="fa6-regular:folder-open"),
    collapsedIcon=DashIconify(icon="fa6-solid:folder-plus"),
)
