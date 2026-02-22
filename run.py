import dash
from dash import Dash, hooks, html
import dash_mantine_components as dmc
print(dash.__version__, dmc.__version__)
dash._dash_renderer._set_react_version("18.2.0")

from components.appshell import create_appshell
from llm.llms_routing import register_llm_middleware


scripts = [
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/dayjs.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/locale/fr.min.js",
    "https://www.googletagmanager.com/gtag/js?id=G-4PJELX1C4W",
    "https://media.ethicalads.io/media/client/ethicalads.min.js",
    "https://cdn.jsdelivr.net/npm/hotkeys-js@4.0.0/dist/hotkeys-js.min.js",
   # "https://unpkg.com/react-scan/dist/auto.global.js"  # performance monitor
]

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    use_pages=True,
    external_scripts=scripts,
    update_title=None,
    prevent_initial_callbacks=True
)

register_llm_middleware(app)


@hooks.index()
def update_index(app_index):
    head_tag = "<head>"
    insert_pos = app_index.find(head_tag) + len(head_tag)
    link_tag = '\n    <link rel="alternate" href="/assets/llms.txt" type="text/plain" title="LLMs Friendly Complete DMC Documentation">'
    updated_index = app_index[:insert_pos] + link_tag + app_index[insert_pos:]
    return updated_index

app.layout = create_appshell(dash.page_registry.values())

server = app.server

if __name__ == "__main__":
    app.run(debug=True, port=8052)
