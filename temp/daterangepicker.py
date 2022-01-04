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
from data import parse_apidocs

description, apidocs = parse_apidocs(dmc.DateRangePicker.__doc__)
date_formats = pd.read_csv(Path(__file__).parent.joinpath("date_formats.csv"))

layout = html.Div(
    children=[
        ComponentName("DateRangePicker"),
        ComponentDescription(description),
        ComponentBlock(
            title="Simple DateRangePicker Example",
            caption=dcc.Markdown(
                "This is a simple example of DateRangePicker tied to a callback. You can either use strings in a valid "
                "datetime format such as `YYYY-MM-DD` or use the date object from datetime library. "
            ),
            code="""import dash_mantine_components as dmc
from datetime import datetime, timedelta, date
from dash import Input, Output, html
from dash.exceptions import PreventUpdate

component = html.Div([
    dmc.DateRangePicker(
        id='date-range-picker',
        label="Date Range",
        description="You can also provide a description",
        minDate=date(2020, 8, 5),
        maxDate=date(2022, 9, 19),
        dates=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
    ),
    dmc.Space(h=10),
    dmc.Text(id="selected-date-date-range-picker"),
])


@app.callback(
    Output('selected-date-date-range-picker', 'children'),
    Input('date-range-picker', 'dates'))
def update_output(dates):
    prefix = 'You have selected: '
    if dates:
        return prefix + "   -   ".join(dates)
    else:
        raise PreventUpdate""",
        ),
        Title("Date formats"),
        SubText(
            dcc.Markdown(
                "Use `format` property to change the format of the date displayed in the dmc.DateRangePicker. You can "
                "use any permutation from the below table to achieve the desired date format. Note: This is not the "
                "format of the value you'll receive from the dmc.DateRangePicker in a callback. That will always "
                "follow: `YYYY-MM-DD`."
            )
        ),
        dmc.Table(rows=date_formats.values, columns=date_formats.columns),
        dmc.Space(h=50),
        Title("Date Format Examples"),
        ComponentBlock(
            code="""import dash_mantine_components as dmc
from datetime import datetime, timedelta

component = dmc.Group(
    position="apart",
    children=[
        dmc.DateRangePicker(
            dates=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
            format="ddd, MMM D YY",
            label="ddd, MMM D YY"
        ),
        dmc.DateRangePicker(
            dates=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
            format="MMMM DD, YY",
            label="MMMM DD, YY",
        ),
        dmc.DateRangePicker(
            dates=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
            format="DD-MM-YYYY",
            label="DD-MM-YYYY",
        )
    ],
)
""",
        ),
        ComponentBlock(
            title="DateRangePicker clear and Overlay mode",
            caption=dcc.Markdown(
                """dmc.DateRangePicker is clearable by default. You can change this behaviour by setting the 
                `clearable` prop to `False`.\ndmc.DateRangePicker also supports opening dmc.DateRangePicker as an 
                overlay instead of the normal popover mode. To enable that, set the type `dropdownType` prop to 
                `modal`."""
            ),
            code="""import dash_mantine_components as dmc
from datetime import datetime, timedelta

component = dmc.DateRangePicker(
    dates=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
    clearable=False,
    dropdownType="modal",
)""",
        ),
        ComponentBlock(
            title="Error Display",
            caption=dcc.Markdown(
                """You can convey errors in your dmc.DateRangePicker by setting the `error` prop. For instance, 
                in the below example we try to convey the user that its a required field and the difference between 
                the start and the end date should be more than 4. Since it's a required field, we also set 
                `clearable=False`."""
            ),
            code="""import dash_mantine_components as dmc
from datetime import datetime, timedelta
from dash import Output, Input

component = dmc.DateRangePicker(
    id="datepicker-range-error",
    dates=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
    label="Date",
    required=True,
    clearable=False,
)


@app.callback(
    Output("datepicker-range-error", "error"),
    Input("datepicker-range-error", "dates")
)
def datepicker_error(dates):
    start = datetime.strptime(dates[0],"%Y-%M-%d").day
    end = datetime.strptime(dates[1],"%Y-%M-%d").day
    return "Diff between the dates should be more than 4." if (end-start) < 5 else "" """,
        ),
        ComponentBlock(
            title="Amount of months",
            caption=dcc.Markdown(
                """You can display more than one months in dmc.DateRangePicker dropdown by setting the `amountOfMonths` 
                prop to the desired value."""
            ),
            code="""import dash_mantine_components as dmc
from datetime import datetime, timedelta
from dash import Output, Input

component = dmc.DateRangePicker(
    dates=[datetime.now().date(), datetime.now().date() + timedelta(days=5)],
    amountOfMonths=2,
)""",
        ),
        ComponentReference(apidocs),
    ]
)
