from pathlib import Path

import dash_mantine_components as dmc
import pandas as pd

from components.configurator import Configurator
from lib.utils import create_table

df = pd.read_csv(Path.cwd().joinpath("docs/table/data.csv"))

target = dmc.Table(create_table(df))

configurator = Configurator(target)
configurator.add_slider("horizontalSpacing", "xs")
configurator.add_slider("verticalSpacing", "xs")

component = configurator.panel
