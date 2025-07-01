import dash_mantine_components as dmc
import dash_iconify  # required in order to use DashIconify in the renderNode function
from .data import data


component = dmc.Tree(
    data=data,
    renderNode={"function": "myLeaf"},
    expanded=[
        "node_modules",
        "node_modules/react",
    ]
)
