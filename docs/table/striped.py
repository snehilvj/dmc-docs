from pathlib import Path

import dash_mantine_components as dmc
import pandas as pd

from lib.configurator import create_configurator
from lib.utils import create_table

controls = [
    {"property": "striped", "component": "Switch", "checked": True},
    {"property": "highlightOnHover", "component": "Switch", "checked": True},
]

df = pd.read_csv(Path.cwd().joinpath("docs/table/data.csv"))

demo = dmc.Table(create_table(df))

component = create_configurator(demo, controls, center=False)
