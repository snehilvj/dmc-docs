import dash_mantine_components as dmc
from dash import html, dcc
from reusable_components import (
    ComponentBlock,
    ComponentName,
    ComponentReference,
    ComponentDescription,
)
from utils import parse_apidocs

description, apidocs = parse_apidocs(dmc.Accordion.__doc__)

layout = html.Div(
    children=[
        ComponentName("Accordion"),
        ComponentDescription(description),
        ComponentBlock(
            title="Simple Accordion Example",
            caption=dcc.Markdown(
                "This is a simple example showing how you can use accordion. You can also pass a `description` along with the `label`."
            ),
            code="""import dash_mantine_components as dmc

component = dmc.Accordion(
    children=[
        dmc.AccordionItem(
            "Colors, fonts, shadows and many other parts are customizable to fit your design needs",
            label="Customization",
            description="Description about flexibility",
        ),
        dmc.AccordionItem(
            "Configure components appearance and behavior with vast amount of settings or overwrite any part of component styles",
            label="Flexibility",
            description="Something something about something",
        ),
    ],
)""",
        ),
        ComponentBlock(
            title="Callbacks and state management",
            caption=dcc.Markdown(
                "A `state` is associated with each Accordion component. Click on any section to see how it looks."
            ),
            code="""import dash_mantine_components as dmc
from dash import Output, Input, html

component = html.Div(
    children=[
        dmc.Accordion(
            id="accordion",
            children=[
                dmc.AccordionItem(
                    "Content 1",
                    label="Section 1",
                ),
                dmc.AccordionItem(
                    "Content 2",
                    label="Section 2", 
                ),
            ]
        ),
        dmc.Text(id="accordion-state", style={"marginTop": 10})
    ]
)


@app.callback(
    Output("accordion-state", "children"),
    Input("accordion", "state")
)
def show_state(state):
    return str(state)
""",
        ),
        ComponentBlock(
            title="Allow multiple items to be opened at the same time",
            caption=dcc.Markdown(
                "Pass `multiple=True` flag to allow opening multiple items."
            ),
            code="""import dash_mantine_components as dmc
    
component = dmc.Accordion(
    multiple=True,
    children=[
        dmc.AccordionItem(
            "Content 1",
            label="Section 1",
        ),
        dmc.AccordionItem(
            "Content 2",
            label="Section 2",
            
        ),
    ],
)""",
        ),
        ComponentReference(apidocs),
    ]
)
