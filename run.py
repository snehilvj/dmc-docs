import dash
from dash import Dash
import dash_mantine_components as dmc
print(dash.__version__, dmc.__version__)
dash._dash_renderer._set_react_version("18.2.0")

from components.appshell import create_appshell

scripts = [
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/dayjs.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/locale/fr.min.js",
    "https://www.googletagmanager.com/gtag/js?id=G-4PJELX1C4W",
    "https://media.ethicalads.io/media/client/ethicalads.min.js",
    "https://unpkg.com/hotkeys-js/dist/hotkeys.min.js",
   # "https://unpkg.com/react-scan/dist/auto.global.js"  # performance monitor
]

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    use_pages=True,
    external_scripts=scripts,
    external_stylesheets=dmc.styles.ALL,
    update_title=None,
)

app.layout = create_appshell(dash.page_registry.values())

server = app.server

if __name__ == "__main__":
    app.run(debug=True, port=8052)
