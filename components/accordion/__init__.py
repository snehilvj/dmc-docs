from lib.blocks import (
    Text,
    Heading,
    CodeBlock,
    DocsBlock,
)
from lib.blueprints import DmcDash

app = DmcDash(__name__, "accordion")

app.layout = DocsBlock(
    component_name="Accordion",
    children=[
        Text("Divide content into collapsible sections."),
        Heading("Simple Example"),
        Text(
            "This is a basic example showing how you can use accordion. You can also pass a `description` along with "
            "the `label`."
        ),
        CodeBlock(__file__, "simple.py", app),
        Heading("Callbacks and state management"),
        Text(
            "A `state` is associated with each Accordion component. Click on any section to see how it looks."
        ),
        CodeBlock(__file__, "state.py", app),
        Heading("Allow multiple items to be opened at the same time"),
        Text("Pass `multiple=True` flag to allow opening multiple items."),
        CodeBlock(__file__, "multiple.py", app),
    ],
)
