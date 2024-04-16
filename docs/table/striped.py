from pathlib import Path

import dash_mantine_components as dmc
import pandas as pd

from lib.configurator import Configurator
from lib.utils import create_table

df = pd.read_csv(Path.cwd().joinpath("docs/table/data.csv"))

target = dmc.Table(create_table(df))

configurator = Configurator(target)
configurator.add_switch("striped", True)
configurator.add_switch("highlightOnHover", True)
configurator.add_switch("withTableBorder", True)
configurator.add_switch("withColumnBorders", True)

component = configurator.panel
