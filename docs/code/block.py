import dash_mantine_components as dmc

component = dmc.Code(
    """from dash import Dash
import dash_mantine_components as dmc

app = Dash(__name__)

app.layout = dmc.Button("Settings")

if __name__ == "__main__":
    app.run_server(debug=True)""",
    block=True,
)
