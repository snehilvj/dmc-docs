from lib.blocks import (
    Text,
    Heading,
    CodeBlock,
    DocsBlock,
    ComponentDescription,
)
from lib.blueprints import DmcDash

app = DmcDash(__name__, "checkbox")

app.layout = DocsBlock(
    component_name="Checkbox",
    children=[
        ComponentDescription("Capture boolean input from user."),
        Heading("Simple Example", id="simple-example"),
        Text("Use the property `checked` in the callbacks."),
        CodeBlock(__file__, "simple.py", app),
        Heading("Different sizes", id="sizes"),
        Text("Choose from one of the following sizes: `xs, sm, md, lg, xl`."),
        CodeBlock(__file__, "sizes.py", app),
        Heading("Different colors", id="colors"),
        Text("Set checkbox color using the `color` prop."),
        CodeBlock(__file__, "colors.py", app, prism=False),
    ],
)
