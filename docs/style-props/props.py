from pathlib import Path

import dash_mantine_components as dmc
import pandas as pd

from lib.utils import create_table

df = pd.read_csv(Path.cwd().joinpath("docs/style-props/props.csv"), index_col=None)

component = dmc.Table(create_table(df), horizontalSpacing=40, withColumnBorders=True)
