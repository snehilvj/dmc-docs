from lib.blocks import Text, Heading, CodeBlock, DocsBlock, ComponentDescription
from lib.blueprints import DmcDash

app = DmcDash(__name__, "affix")

app.layout = DocsBlock(
    component_name="Affix",
    children=[
        ComponentDescription("Render react node inside portal at fixed position."),
        Heading("Simple Example", id="simple-example"),
        Text("Look at the bottom right!"),
        CodeBlock(__file__, "simple.py", app),
    ],
)
