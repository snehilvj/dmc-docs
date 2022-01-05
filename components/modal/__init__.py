from lib.blocks import (
    Text,
    Heading,
    CodeBlock,
    DocsBlock,
    ComponentDescription,
)
from lib.blueprints import DmcDash

app = DmcDash(__name__, "modal")

app.layout = DocsBlock(
    component_name="Modal",
    children=[
        ComponentDescription("Modal with optional header."),
        Heading("Simple Example", id="simple-example"),
        Text(
            "This is a basic example of dmc.Modal. You can also customize it by setting the desired `radius` or "
            "`padding`. "
        ),
        CodeBlock(__file__, "simple.py", app),
        Heading("Different Sizes", id="sizes"),
        Text("Set the size of the modal using the `size` prop."),
        CodeBlock(__file__, "sizes.py", app),
        Heading("Vertically Centered Modal", id="vertically-centered"),
        Text("To vertically center the modal, set `centered=True`."),
        CodeBlock(__file__, "vertical.py", app),
        Heading("Modal with overflow", id="overflow"),
        Text(
            "You can control modal vertical overflow behavior by setting `overflow` prop."
        ),
        CodeBlock(__file__, "overflow.py", app),
    ],
)
