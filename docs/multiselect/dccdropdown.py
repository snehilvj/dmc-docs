from dash import dcc
import dash_mantine_components as dmc

component = dmc.InputWrapper(
    dcc.Dropdown([f"option {i}" for i in range(100)],  value=["option 1", "option 2", "option 3"], multi=True, id="dcc4-dropdown"),
    label="dcc.Dropdown with a dmc.InputWrapper",
    htmlFor="dcc4-dropdown",
    className="dmc"  # styles with Mantine theme
)