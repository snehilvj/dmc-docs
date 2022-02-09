import dash_mantine_components as dmc
from dash import Dash  # no-run
from dash_iconify import DashIconify

app = Dash(__name__)  # no-run

layout = dmc.Group(
    [
        DashIconify(icon="ion:logo-github", width=30, rotate=1, flip="horizontal"),
        DashIconify(icon="flat-ui:settings", width=30),
        DashIconify(icon="feather:info", color="blue", width=30),
    ]
)

if __name__ == "__main__":  # no-run
    app.run_server()  # no-run
