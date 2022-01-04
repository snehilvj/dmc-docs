from lib.blocks import (
    Text,
    Heading,
    CodeBlock,
    DocsBlock,
)
from lib.blueprints import DmcDash

app = DmcDash(__name__, "checkbox")

app.layout = DocsBlock(
    component_name="Checkbox",
    children=[
        Text("Capture boolean input from user."),
        Heading("Simple Example"),
        Text("Use the property `checked` in the callbacks."),
        CodeBlock(__file__, "simple.py", app, prism=False),
        Heading("Different sizes"),
        Text("Choose from one of the following sizes: `xs, sm, md, lg, xl`."),
        CodeBlock(__file__, "sizes.py", app),
        Heading("Different colors"),
        Text("Set checkbox color using the `color` prop."),
        CodeBlock(__file__, "colors.py", app, prism=False),
    ],
)
