import dash
from dash import Dash
import dash_mantine_components as dmc

dash._dash_renderer._set_react_version("18.2.0")

from components.appshell import create_appshell

stylesheets = [
    dmc.styles.DATES,
    dmc.styles.CODE_HIGHLIGHT,
    dmc.styles.CHARTS,
    dmc.styles.CAROUSEL,
    dmc.styles.NOTIFICATIONS,
    dmc.styles.NPROGRESS,
]

scripts = [
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/dayjs.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/locale/ru.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/locale/fr.min.js",
    "https://www.googletagmanager.com/gtag/js?id=G-4PJELX1C4W",
    "https://media.ethicalads.io/media/client/ethicalads.min.js",
    "https://unpkg.com/hotkeys-js/dist/hotkeys.min.js",
]

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    use_pages=True,
    external_scripts=scripts,
    external_stylesheets=stylesheets,
    update_title=None,
)

app.layout = create_appshell(dash.page_registry.values())

server = app.server

if __name__ == "__main__":
    app.run(debug=True, port=8052)
