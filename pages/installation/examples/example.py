import dash_mantine_components as dmc
from dash import Dash  # no-exec

app = Dash(__name__)  # no-exec

app.layout = dmc.Alert(
    [
        "Hi from Dash Mantine Components. Please support us on",
        dmc.Anchor(
            "GitHub",
            href="https://github.com/snehilvj/dash-mantine-components",
            style={"marginLeft": 5},
            size="sm",
            color="violet",
        ),
        ".",
    ],
    title="Welcome!",
    color="violet",
)

if __name__ == "__main__":  # no-exec
    app.run_server()  # no-exec
