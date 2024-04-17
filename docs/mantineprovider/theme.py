import json

import dash_mantine_components as dmc

theme = json.dumps(dmc.DEFAULT_THEME, indent=8)
component = dmc.CodeHighlight(code=theme, language="json")
