from datetime import datetime
import dash_mantine_components as dmc

from components.configurator import Configurator

target = dmc.DatePicker(value=datetime.now().date(), size="sm")

configurator = Configurator(target)

configurator.add_slider("size", "sm")

component = configurator.panel
