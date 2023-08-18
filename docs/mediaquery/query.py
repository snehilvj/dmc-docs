import dash_mantine_components as dmc

component = dmc.MediaQuery(
    [dmc.Text("Try to change the size of your browser window.")],
    query="(max-width: 1200px) and (min-width: 800px)",
    styles={"fontSize": 20, "backgroundColor": "silver"},
)
