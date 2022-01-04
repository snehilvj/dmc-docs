import importlib
from os import environ

from dash import Output, Input
from flask import Flask

from data import data

server = Flask(__name__)

for component in data:
    print(f"Registering docs for {component}.")
    module = importlib.import_module(f"components.{component.lower()}")
    app = module.app
    app.init_app(server)
    # register callback for component select/search in the header
    app.callback(Output("url", "pathname"), Input("select-component", "value"))(
        lambda value: value
    )
    server.register_blueprint(app)

if __name__ == "__main__":
    server.run(debug=environ.get("DMC_DEBUG", False))
