import dash_mantine_components as dmc

from components.configurator import Configurator

TARGET_ID = "interactive-avatar"

target = dmc.Center(dmc.Avatar(src="/assets/avatar.jpeg", id=TARGET_ID))

configurator = Configurator(target, TARGET_ID)

configurator.add_slider("radius", "sm")
configurator.add_slider("size", "md")

component = configurator.panel
