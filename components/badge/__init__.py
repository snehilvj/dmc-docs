from lib.blocks import (
    Text,
    Heading,
    CodeBlock,
    DocsBlock,
    ComponentDescription,
)
from lib.blueprints import DmcDash

app = DmcDash(__name__, "badge")

app.layout = DocsBlock(
    component_name="Badge",
    children=[
        ComponentDescription("Display badge, pill or tag."),
        Heading("Simple Example", id="simple-example"),
        Text(
            "You can customize your badge and then just copy the auto generated code."
        ),
        CodeBlock(__file__, "interactive.py", app, prism=False),
        Heading("With Gradient", id="gradient"),
        Text("You can also customize the gradient fill of the badge."),
        CodeBlock(__file__, "gradient.py", app),
        Heading("Badge within a Button", id="in-button"),
        Text("You can put badge in a button's `children`."),
        CodeBlock(__file__, "button.py", app),
    ],
)
