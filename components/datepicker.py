import dash_mantine_components as dmc
from dash import html
from utils import create_component_title
from datetime import datetime

datepicker = html.Div(
    [
        create_component_title("Datepicker and DateRangePicker"),
        dmc.Group(
            children=[
                dmc.DatePicker(label="Select date", date=str(datetime.now().date())),
                dmc.DateRangePicker(label="Select a range", amountOfMonths=2),
            ]
        ),
        dmc.Space(h=30),
    ]
)
