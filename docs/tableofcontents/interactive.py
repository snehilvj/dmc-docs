import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.TableOfContents(
    selector=".mantine-AppShell-main :is( h2, h3, h4)",
    variant="filled",
    color="blue",
    size="sm",
    radius="sm"
)

configurator = Configurator(target, center_component=True)


configurator.add_segmented_control(
    "variant",
    ["filled",  "light", "none"],
    "filled",
)
configurator.add_colorpicker("color", "indigo")
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "sm")


component = configurator.panel
