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

app = DmcDash(__name__, "daterangepicker")
date_formats = pd.read_csv(Path(__file__).parents[2].joinpath("date_formats.csv"))

app.layout = DocsBlock(
    component_name="DateRangePicker",
    children=[
        Text("Capture dates range from user."),
        Heading("Simple Example"),
        Text(
            "This is a simple example of DateRangePicker tied to a callback. You can either use strings in a valid "
            "datetime format such as `YYYY-MM-DD` or use the date object from datetime library. "
        ),
        CodeBlock(__file__, "simple.py", app),
        Heading("Date formats"),
        Text(
            "Use `format` property to change the format of the date displayed in the dmc.DateRangePicker. You can use "
            "any permutation from the below table to achieve the desired date format. Note: This is not the format of "
            "the value you'll receive from the dmc.DateRangePicker in a callback. That will always follow: "
            "`YYYY-MM-DD`. "
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
        Heading("DateRangePicker clear and Overlay mode"),
        Text(
            "dmc.DateRangePicker is clearable by default. You can change this behaviour by setting the `clearable` "
            "prop to `False`.\ndmc.DateRangePicker also supports opening dmc.DateRangePicker as an overlay instead of "
            "the normal popover mode. To enable that, set the type `dropdownType` prop to `modal`. "
        ),
        CodeBlock(__file__, "dropdown_type.py", app),
        Heading("Amount of months"),
        Text(
            "You can display more than one months in dmc.DateRangePicker dropdown by setting the `amountOfMonths` "
            "prop to the desired value. "
        ),
        CodeBlock(__file__, "amount_months.py", app),
        Heading("Error Display"),
        Text(
            "You can convey errors in your dmc.DateRangePicker by setting the `error` prop. For instance, "
            "in the below example we try to convey the user that its a required field and the difference between the "
            "start and the end date should be more than 4. Since it's a required field, we also set `clearable=False`. "
        ),
        CodeBlock(__file__, "errors.py", app),
    ],
)
