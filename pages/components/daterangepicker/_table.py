from pathlib import Path

import dash_mantine_components as dmc
import pandas as pd

date_formats = pd.read_csv(Path.cwd().joinpath("date_formats.csv"))

component = dmc.Container(
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
)
