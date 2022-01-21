import dash_mantine_components as dmc
from dash import Dash  # no-run

app = Dash(__name__)  # no-run

app.layout = dmc.Alert(
    [
        "Hi from Dash Mantine Components. You can create some great looking dashboards using me!"
    ],
    title="Welcome!",
    color="violet",
)

if __name__ == "__main__":  # no-run
    app.run_server()  # no-run
