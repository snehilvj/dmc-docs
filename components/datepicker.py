from pathlib import Path

import dash_mantine_components as dmc
import pandas as pd
from dash import html, dcc

from reusable_components import (
    ComponentBlock,
    ComponentDescription,
    ComponentName,
    ComponentReference,
    Title,
    SubText,
)
from utils import parse_apidocs

description, apidocs = parse_apidocs(dmc.DatePicker.__doc__)
date_formats = pd.read_csv(Path(__file__).parent.joinpath("date_formats.csv"))

layout = html.Div(
    children=[
        ComponentName("DatePicker"),
        ComponentDescription(description),
        ComponentBlock(
            title="Simple DatePicker Example",
            caption=dcc.Markdown(
                "This is a simple example of DatePicker tied to a callback. You can either use strings in a valid "
                "datetime format such as `YYYY-MM-DD` or use the date object from datetime library. "
            ),
            code="""import dash_mantine_components as dmc
from datetime import datetime, date
from dash import Input, Output, html
from dash.exceptions import PreventUpdate

component = html.Div([
    dmc.DatePicker(
        id='date-picker',
        label="Start Date",
        description="You can also provide a description",
        minDate=date(2020, 8, 5),
        maxDate=date(2022, 9, 19),
        date=datetime.now().date()
    ),
    dmc.Space(h=10),
    dmc.Text(id="selected-date"),
])


@app.callback(
    Output('selected-date', 'children'),
    Input('date-picker', 'date'))
def update_output(date):
    prefix = 'You have selected: '
    if date:
        return prefix + date
    else:
        raise PreventUpdate""",
        ),
        Title("Date formats"),
        SubText(
            dcc.Markdown(
                "Use `format` property to change the format of the date displayed in the date picker. You can use any "
                "permutation from the below table to achieve the desired date format. Note: This is not the format of "
                "the value you'll receive from the date picker in a callback. That will always follow: `YYYY-MM-DD`. "
            )
        ),
        dmc.Table(rows=date_formats.values, columns=date_formats.columns),
        dmc.Space(h=50),
        Title("Date Format Examples"),
        ComponentBlock(
            code="""import dash_mantine_components as dmc
from datetime import datetime

component = dmc.Group(
    position="apart",
    children=[
        dmc.DatePicker(
            date=datetime.now().date(),
            format="ddd, MMM D YY",
            label="ddd, MMM D YY"
        ),
        dmc.DatePicker(
            date=datetime.now().date(),
            format="MMMM DD, YY",
            label="MMMM DD, YY",
        ),
        dmc.DatePicker(
            date=datetime.now().date(),
            format="DD-MM-YYYY",
            label="DD-MM-YYYY",
        )
    ],
)
""",
        ),
        ComponentBlock(
            title="DatePicker clear and Overlay mode",
            caption=dcc.Markdown(
                """dmc.DatePicker is clearable by default. You can change this behaviour by setting the `clearable` 
                prop to `False`.\ndmc.DatePicker also supports opening date picker as an overlay instead of the 
                normal popover mode. To enable that, set the type `dropdownType` prop to `modal`."""
            ),
            code="""import dash_mantine_components as dmc
from datetime import datetime

component = dmc.DatePicker(
    date=datetime.now().date(),
    clearable=False,
    dropdownType="modal",
)""",
        ),
        ComponentBlock(
            title="Error Display",
            caption=dcc.Markdown(
                """You can convey errors in your date picker by setting the `error` prop. For instance, in the below 
                example we try to convey the user that its a required field and the date can't be an odd date. Since 
                it's a required field, we also set `clearable=False`."""
            ),
            code="""import dash_mantine_components as dmc
from datetime import datetime
from dash import Output, Input

component = dmc.DatePicker(
    id="datepicker-error",
    date=datetime.now().date(),
    label="Date",
    required=True,
    clearable=False,
)


@app.callback(
    Output("datepicker-error", "error"),
    Input("datepicker-error", "date")
)
def datepicker_error(date):
    day = datetime.strptime(date,"%Y-%M-%d").day
    return "Please select an even date." if day % 2 else "" """,
        ),
        ComponentBlock(
            title="Amount of months",
            caption=dcc.Markdown(
                """You can display more than one months in date picker dropdown by setting the `amountOfMonths` prop 
                to the desired value."""
            ),
            code="""import dash_mantine_components as dmc
from datetime import datetime
from dash import Output, Input

component = dmc.DatePicker(
    date=datetime.now().date(),
    amountOfMonths=2,
)""",
        ),
        ComponentReference(apidocs),
    ]
)
