import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Tabs(
    variant="outline",
    children=[
        dmc.Tab(
            label="styles.css",
            icon=[DashIconify(icon="vscode-icons:file-type-css", width=20)],
            children=[
                dmc.Prism(
                    """@font-face {
  font-family: Chunkfive; src: url('Chunkfive.otf');
}

body, .usertext {
  color: #F0F0F0; background: #600;
  font-family: Chunkfive, sans;
  --heading-1: 30px/32px Helvetica, sans-serif;
}

@import url(print.css);
@media print {
  a[href^=http]::after {
    content: attr(href)
  }
}""",
                    language="css",
                )
            ],
        ),
        dmc.Tab(
            label="decorator.py",
            icon=[DashIconify(icon="vscode-icons:file-type-python", width=20)],
            children=[
                dmc.Prism(
                    """@requires_authorization
def somefunc(param1='', param2=0):
    r'''A docstring'''
    if param1 > param2: # interesting
        print 'Greater'
    return (param2 - param1 + 1 + 0b10l) or None

class SomeClass:
    pass

>>> message = '''interpreter
... prompt'''""",
                    language="python",
                )
            ],
        ),
        dmc.Tab(
            label="component.jsx",
            icon=[DashIconify(icon="vscode-icons:file-type-reactts", width=20)],
            children=[
                dmc.Prism(
                    """import { Button } from '@mantine/core';

function Demo() {
  return <Button>Hello</Button>
}""",
                    language="tsx",
                )
            ],
        ),
    ]
)
