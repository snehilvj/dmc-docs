import dash_mantine_components as dmc
from dash import html, dcc

from reusable_components import (
    ComponentBlock,
    ComponentDescription,
    ComponentName,
    ComponentReference,
)
from utils import parse_apidocs

description, apidocs = parse_apidocs(dmc.Modal.__doc__)

layout = html.Div(
    children=[
        ComponentName("Modal"),
        ComponentDescription(description),
        ComponentBlock(
            title="Simple Example",
            caption=dcc.Markdown(
                "This is simple example of dmc.Modal. You can also customize it by setting the "
                "desired `radius` or `padding`."
            ),
            code="""import dash_mantine_components as dmc
from dash import html, Output, Input, State

component = html.Div([
    dmc.Button("Open Modal", id="modal-demo-button"),
    dmc.Modal(
        title="New Modal",
        id="modal",
        children=[
            dmc.Text("I am in a modal component."),
            dmc.Space(h=20),
            dmc.Group(
                [
                    dmc.Button("Submit", id="modal-submit-button"),
                    dmc.Button(
                        "Close",
                        color="red",
                        variant="outline",
                        id="modal-close-button",
                    ),
                ],
                position="right",
            ),
        ],
    )
])


@app.callback(
    Output("modal", "opened"),
    Input("modal-demo-button", "n_clicks"),
    Input("modal-close-button", "n_clicks"),
    Input("modal-submit-button", "n_clicks"),
    State("modal", "opened"),
    prevent_initial_call=True,
)
def modal_demo(nc1, nc2, nc3, opened):
    return not opened""",
        ),
        ComponentBlock(
            title="Different Sizes",
            caption=dcc.Markdown("Set the size of the modal using the `size` prop."),
            code="""import dash_mantine_components as dmc
from dash import html, Output, Input, State

component = html.Div([
    dmc.Modal(title="Size: lg", id="modal-size-lg", size="lg"),
    dmc.Modal(title="Size: 378px", id="modal-size-378", size=378),
    dmc.Modal(title="Size: 55%", id="modal-size-55", size="55%"),
    dmc.Modal(title="Size: full", id="modal-size-full", size="full"),
    dmc.Group([
        dmc.Button("lg", variant="outline", id="lg-modal-button"),
        dmc.Button("378px", variant="outline", id="378-modal-button"),
        dmc.Button("55%", variant="outline", id="55-modal-button"),
        dmc.Button("full", variant="outline", id="full-modal-button"),
    ]),
])


for size in ["lg", "378", "55", "full"]:
    @app.callback(
        Output(f"modal-size-{size}", "opened"),
        Input(f"{size}-modal-button", "n_clicks"),
        State(f"modal-size-{size}", "opened"),
        prevent_initial_call=True,
    )
    def toggle_modal(n_clicks, opened):
        return not opened""",
        ),
        ComponentBlock(
            title="Vertically Centered Modal",
            caption=dcc.Markdown(
                "To vertically center the modal, set `centered=True`."
            ),
            code="""import dash_mantine_components as dmc
from dash import html, Output, Input, State

component = html.Div([
    dmc.Modal(
        title="Centered Modal",
        id="modal-centered",
        centered=True,
        children=[
            dmc.Text("This is a vertically centered modal.")    
        ]
    ),
    dmc.Button("Open modal", id="modal-centered-button"),
])


@app.callback(
    Output("modal-centered", "opened"),
    Input("modal-centered-button", "n_clicks"),
    State("modal-centered", "opened"),
    prevent_initial_call=True,
)
def toggle_modal(n_clicks, opened):
    return not opened""",
        ),
        ComponentBlock(
            title="Modal with overflow",
            caption=dcc.Markdown(
                "You can control modal vertical overflow behavior by setting `overflow` prop."
            ),
            code='''import dash_mantine_components as dmc
from dash import html, Output, Input, State

paragraph = """Dash apps give a point-&-click interface to models written in Python, vastly expanding the notion of 
what's possible in a traditional 'dashboard.' With Dash apps, data scientists and engineers put complex Python 
analytics in the hands of business decision-makers and operators.""" * 10

component = html.Div([
    dmc.Modal(
        id="modal-outside",
        title="Outside Overflow",
        overflow="outside",
        children=[dmc.Text(paragraph)]
    ),
    dmc.Modal(
        id="modal-inside",
        title="Inside Overflow",
        overflow="inside",
        children=[dmc.Text(paragraph)]
    ),
    dmc.Group([
        dmc.Button("Outside Overflow", id="modal-outside-button"),
        dmc.Button("Inside Overflow", id="modal-inside-button"),
    ]),
])


for overflow in ["outside", "inside"]:
    @app.callback(
        Output(f"modal-{overflow}", "opened"),
        Input(f"modal-{overflow}-button", "n_clicks"),
        State(f"modal-{overflow}", "opened"),
        prevent_initial_call=True,
    )
    def toggle_modal(n_clicks, opened):
        return not opened''',
        ),
        ComponentReference(apidocs),
    ]
)
