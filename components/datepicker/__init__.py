from pathlib import Path

import dash_mantine_components as dmc
import pandas as pd

from lib.blocks import (
    Text,
    Heading,
    CodeBlock,
    DocsBlock,
)
from lib.blueprints import DmcDash

app = DmcDash(__name__, "datepicker")
date_formats = pd.read_csv(Path(__file__).parents[2].joinpath("date_formats.csv"))

app.layout = DocsBlock(
    component_name="DatePicker",
    children=[
        Text("Capture date input from user."),
        Heading("Simple Example"),
        Text(
            "This is a simple example of DatePicker tied to a callback. You can either use strings in a valid "
            "datetime format such as `YYYY-MM-DD` or use the date object from datetime library. "
        ),
        CodeBlock(__file__, "simple.py", app),
        Heading("Date formats"),
        Text(
            "Use `format` property to change the format of the date displayed in the date picker. You can use any "
            "permutation from the below table to achieve the desired date format. Note: This is not the format of "
            "the value you'll receive from the date picker in a callback. That will always follow: `YYYY-MM-DD`. "
        ),
        dmc.Container(
            size="sm",
            style={"marginBottom": 40},
            children=[
                dmc.Paper(
                    withBorder=True,
                    children=[
                        dmc.Table(
                            rows=date_formats.values,
                            columns=date_formats.columns,
                        )
                    ],
                )
            ],
        ),
        Heading("Date Format Examples"),
        CodeBlock(__file__, "formats.py", app),
        Heading("DatePicker clear and Overlay mode"),
        Text(
            """dmc.DatePicker is clearable by default. You can change this behaviour by setting the `clearable` prop 
            to `False`.\ndmc.DatePicker also supports opening date picker as an overlay instead of the normal popover 
            mode. To enable that, set the type `dropdownType` prop to `modal`. """
        ),
        CodeBlock(__file__, "dropdown_type.py", app),
        Heading("Amount of months"),
        Text(
            """You can display more than one months in date picker dropdown by setting the `amountOfMonths` prop to the desired value."""
        ),
        CodeBlock(__file__, "amount_months.py", app),
        Heading("Error Display"),
        Text(
            """You can convey errors in your date picker by setting the `error` prop. For instance, in the below example we try to convey the user that its a required field and the date can't be an odd date. Since it's a required field, we also set `clearable=False`."""
        ),
        CodeBlock(__file__, "errors.py", app),
    ],
)
