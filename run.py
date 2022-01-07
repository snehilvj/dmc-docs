import importlib
from os import environ

from dash import Output, Input
from flask import Flask, redirect

from data import component_list

server = Flask(__name__)


@server.get("/")
def home():
    return redirect("/installation", 302)


def register_blueprints(type_, blueprint_names):
    for name in blueprint_names:
        print(f"Registering {name}.")
        module = importlib.import_module(f"{type_}.{name.lower()}")
        app = module.app
        app.init_app(server)
        # register callback for component select/search in the header
        app.callback(Output("url", "pathname"), Input("select-component", "value"))(
            lambda value: value
        )
        server.register_blueprint(app)


register_blueprints("components", component_list)
register_blueprints("pages", ["Installation"])

if __name__ == "__main__":
    server.run(debug=environ.get("DMC_DEBUG", False))
