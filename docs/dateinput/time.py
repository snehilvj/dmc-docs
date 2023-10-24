from datetime import datetime
import dash_mantine_components as dmc


component = dmc.DateInput(
    valueFormat="DD/MM/YYYY HH:mm:ss",
    label="Date and Time input",
    value=datetime.now()
)