import dash_mantine_components as dmc
from dash import Dash  # no-run

scripts = [
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/dayjs.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/locale/ru.min.js",
]

app = Dash(__name__, external_scripts=scripts)  # no-run

layout = dmc.DatePicker(
    id="ru-date-picker",
    label="Дата события",
    locale="ru",
    style={"width": 200},
)
