import dash_mantine_components as dmc
from dash import html, dcc

from reusable_components import (
    ComponentBlock,
    ComponentDescription,
    ComponentName,
    ComponentReference,
)
from utils import parse_apidocs

description, apidocs = parse_apidocs(dmc.Drawer.__doc__)

layout = html.Div(
    children=[
        ComponentName("Drawer"),
        ComponentDescription(description),
        ComponentBlock(
            title="Simple Example",
            caption=dcc.Markdown(
                """This is a basic example of dmc.Drawer. Set the `opened` property to open the drawer. The drawer 
                can be closed in the following ways: 
                
* programmatically (using callbacks)
* by clicking on the cross button (if not disabled using `hideCloseButton` prop)
* by clicking outside the drawer area (if not disabled using `noCloseOnClickOutside` prop)
* by pressing the ESC key (if not disabled using `noCloseOnEscape` prop)"""
            ),
            code="""import dash_mantine_components as dmc
from dash import html, Output, Input, State

component = html.Div([
    dmc.Button("Open Drawer", id="drawer-demo-button"),
    dmc.Drawer(
        title="Drawer Example",
        id="drawer",
        padding="md",
    ),
])


@app.callback(
    Output("drawer", "opened"),
    Input("drawer-demo-button", "n_clicks"),
    prevent_initial_call=True,
)
def drawer_demo(n_clicks):
    return True""",
        ),
        ComponentBlock(
            title="Different Sizes",
            caption=dcc.Markdown("Set the size of the drawer using the `size` prop."),
            code="""import dash_mantine_components as dmc
from dash import html, Output, Input, State

component = html.Div([
    dmc.Drawer(title="Size: md", id="drawer-size-md", padding="md", size="md"),
    dmc.Drawer(title="Size: 450px", id="drawer-size-450", padding="md", size=450),
    dmc.Drawer(title="Size: 55%", id="drawer-size-55", padding="md", size="55%"),
    dmc.Drawer(title="Size: full", id="drawer-size-full", padding="md", size="full"),
    dmc.Group([
        dmc.Button("md", id="md-drawer-button"),
        dmc.Button("450px", id="450-drawer-button"),
        dmc.Button("55%", id="55-drawer-button"),
        dmc.Button("full", id="full-drawer-button"),
    ]),
])


for size in ["md", "450", "55", "full"]:
    @app.callback(
        Output(f"drawer-size-{size}", "opened"),
        Input(f"{size}-drawer-button", "n_clicks"),
        State(f"drawer-size-{size}", "opened"),
        prevent_initial_call=True,
    )
    def toggle_drawer(n_clicks, opened):
        return not opened""",
        ),
        ComponentBlock(
            title="Placement",
            caption=dcc.Markdown(
                "By default, Drawer will start to appear from the left, but this position can be customized by "
                "setting the `position` prop. "
            ),
            code="""import dash_mantine_components as dmc
from dash import html, Output, Input, State

component = html.Div([
    dmc.Drawer(id="drawer-position"),
    dmc.Group(
        align="center",
        position="apart",
        children=[
            dmc.RadioGroup(
                id="drawer-position-radio",
                value="left",
                data=[
                    {"label": "Left (Default)", "value": "left"},
                    {"label": "Top", "value": "top"},
                    {"label": "Right", "value": "right"},
                    {"label": "Bottom", "value": "bottom"},
                ],
            ),
            dmc.Button("Open Drawer", id="drawer-position-button"),
        ],
    ),
])


@app.callback(
    Output("drawer-position", "opened"),
    Output("drawer-position", "position"),
    Input("drawer-position-button", "n_clicks"),
    State("drawer-position-radio", "value"),
    prevent_initial_call=True,
)
def toggle_drawer(n_clicks, position):
    return True, position""",
        ),
        ComponentBlock(
            title="Modal with overflow",
            caption=dcc.Markdown(
                "You can control drawer vertical overflow behavior by setting `overflow` prop."
            ),
            code='''import dash_mantine_components as dmc
from dash import html, Output, Input, State

paragraph = """Dash apps give a point-&-click interface to models written in Python, vastly expanding the notion of 
what's possible in a traditional 'dashboard.' With Dash apps, data scientists and engineers put complex Python 
analytics in the hands of business decision-makers and operators.""" * 10

component = html.Div([
    dmc.Modal(
        id="drawer-outside",
        title="Outside Overflow",
        overflow="outside",
        children=[dmc.Text(paragraph)]
    ),
    dmc.Modal(
        id="drawer-inside",
        title="Inside Overflow",
        overflow="inside",
        children=[dmc.Text(paragraph)]
    ),
    dmc.Group([
        dmc.Button("Outside Overflow", id="drawer-outside-button"),
        dmc.Button("Inside Overflow", id="drawer-inside-button"),
    ]),
])


for overflow in ["outside", "inside"]:
    @app.callback(
        Output(f"drawer-{overflow}", "opened"),
        Input(f"drawer-{overflow}-button", "n_clicks"),
        State(f"drawer-{overflow}", "opened"),
        prevent_initial_call=True,
    )
    def toggle_drawer(n_clicks, opened):
        return not opened''',
        ),
        ComponentReference(apidocs),
    ]
)
