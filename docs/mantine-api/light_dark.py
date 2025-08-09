import dash_mantine_components as dmc

code = """
import dash_mantine_components as dmc
from dash import Dash

app = Dash()

app.layout = dmc.MantineProvider(
    forceColorScheme="dark",
    # your content    
)

app.run()
"""



component = dmc.Card([
    dmc.SimpleGrid([
        dmc.Image(src="assets/dmc-light-dark.png"),

        dmc.CodeHighlight(
            language="python",
            code=code,
        )

    ], cols=2)
], withBorder=True)