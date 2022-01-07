from lib.blocks import Text, Heading, CodeBlock, DocsBlock, ComponentDescription
from lib.blueprints import DmcDash

app = DmcDash(__name__, "chips")

app.layout = DocsBlock(
    component_name="Chips",
    children=[
        ComponentDescription("Alternative to Select and RadioGroup."),
        Heading("Simple Example", id="simple-example"),
        Text(
            "You can customize your Chips and then just copy the auto generated code."
        ),
        CodeBlock(__file__, "interactive.py", app, prism=False),
        Heading("Callbacks", id="callbacks"),
        Text(
            "The `value` property is a list of items if `multiple=True` else a single item"
        ),
        CodeBlock(__file__, "callbacks.py", app),
    ],
)
