import dash
import dash_labs as dl
from dash import Dash

from lib.appshell import create_appshell

scripts = [
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/dayjs.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/locale/ru.min.js",
]

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    plugins=[dl.plugins.pages],
    external_scripts=scripts,
    update_title=None,
)

app.layout = create_appshell(dash.page_registry.values())
server = app.server

if __name__ == "__main__":
    app.run_server(debug=True)
