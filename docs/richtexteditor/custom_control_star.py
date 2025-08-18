import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.RichTextEditor(
    html= '<div>Click control to insert star emoji</div>',
    toolbar = {
        "controlsGroups": [
            [
                {
                    "CustomControl": {
                        "aria-label": "Custom Button",
                        "title": "Custom Button",
                        "children": DashIconify(icon="mdi:star", width=20, height=20),
                        "onClick": {"function": "insertContent", "options": "⭐"},
                    },
                },
            ],
        ],
    },

)