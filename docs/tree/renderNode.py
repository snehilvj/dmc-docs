import dash_mantine_components as dmc
import dash_iconify
from .data import data


component = dmc.Tree(data=data, renderNode={"function": "myLeaf"}, m="lg")
