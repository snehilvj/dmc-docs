from pathlib import Path

import dash_mantine_components as dmc
import pandas as pd

from lib.utils import render_html_table

date_formats = pd.read_csv(Path.cwd().joinpath("date_formats.csv"))

component = dmc.Container(
    size="sm",
    style={"marginBottom": 40},
    children=[
        dmc.Paper(
            withBorder=True,
            children=[
                dmc.Table(
                    render_html_table(
                        columns=date_formats.columns,
                        rows=date_formats.values,
                    )
                )
            ],
        )
    ],
)
