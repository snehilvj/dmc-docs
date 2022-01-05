from lib.blocks import (
    Text,
    Heading,
    CodeBlock,
    DocsBlock,
    ComponentDescription,
)
from lib.blueprints import DmcDash

app = DmcDash(__name__, "accordion")

app.layout = DocsBlock(
    component_name="Accordion",
    children=[
        ComponentDescription("Divide content into collapsible sections."),
        Heading("Simple Example", id="simple-example"),
        Text(
            "This is a basic example showing how you can use accordion. You can also pass a `description` along with "
            "the `label`."
        ),
        CodeBlock(__file__, "simple.py", app),
        Heading("Callbacks and State Management", id="callbacks"),
        Text(
            "A `state` is associated with each Accordion component. Click on any section to see how it looks."
        ),
        CodeBlock(__file__, "state.py", app),
        Heading("Multiple Items", id="multiple-items"),
        Text("Pass `multiple=True` flag to allow opening multiple items."),
        CodeBlock(__file__, "multiple.py", app),
    ],
)
