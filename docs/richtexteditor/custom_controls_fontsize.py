
import dash_mantine_components as dmc
from dash_iconify import DashIconify


component = dmc.RichTextEditor(
    html="<p>Change font size with the controls!</p>",
    toolbar={
        "controlsGroups": [
            ["H1", "H2", "H3", "H4"],
            [
                {
                    "CustomControl": {
                        "aria-label": "Increase font size",
                        "title": "Increase font size",
                        "children": DashIconify(icon="mdi:format-font-size-increase", width=16),
                        "onClick": {"function": "increaseFontSize"},
                    },
                },
                {
                    "CustomControl": {
                        "aria-label": "Decrease font size",
                        "title": "Decrease font size",
                        "children": DashIconify(icon="mdi:format-font-size-decrease", width=16),
                        "onClick": {"function": "decreaseFontSize"},
                    },
                },
            ],
         ],
    },
)