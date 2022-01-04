from lib.blocks import Text, Heading, CodeBlock, DocsBlock
from lib.blueprints import DmcDash

app = DmcDash(__name__, "affix")

app.layout = DocsBlock(
    component_name="Affix",
    children=[
        Text("Render react node inside portal at fixed position."),
        Heading("Simple Example"),
        Text("Look at the bottom right!"),
        CodeBlock(__file__, "simple.py", app),
    ],
)
