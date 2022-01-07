import dash_mantine_components as dmc
from dash import Dash  # no-exec

app = Dash(__name__)  # no-exec

app.layout = dmc.Alert(
    [
        "Hi from Dash Mantine Components. You can create some great looking dashboards using me!"
    ],
    title="Welcome!",
    color="violet",
)

if __name__ == "__main__":  # no-exec
    app.run_server()  # no-exec
