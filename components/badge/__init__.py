from lib.blocks import (
    Text,
    Heading,
    CodeBlock,
    DocsBlock,
)
from lib.blueprints import DmcDash

app = DmcDash(__name__, "badge")

app.layout = DocsBlock(
    component_name="Badge",
    children=[
        Text("Divide content into collapsible sections."),
        Heading("Interactive Demo"),
        Text(
            "You can customize your badge and then just copy the auto generated code."
        ),
        CodeBlock(__file__, "interactive.py", app, prism=False),
        Heading("With Gradient"),
        Text("You can also customize the gradient fill of the badge."),
        CodeBlock(__file__, "gradient.py", app),
        Heading("Badge within a Button"),
        Text("You can put badge in a button's `children`."),
        CodeBlock(__file__, "button.py", app)
    ],
)
