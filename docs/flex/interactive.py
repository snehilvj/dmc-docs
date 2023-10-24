import dash_mantine_components as dmc

from components.configurator import Configurator

target = dmc.Flex(
    [
        dmc.Button("Button 1"),
        dmc.Button("Button 2"),
        dmc.Button("Button 3"),
    ],
    mih=50,
    bg="rgba(0, 0, 0, .3)",
    gap="md",
    justify="flex-start",
    align="flex-start",
    direction="row",
    wrap="wrap",
)

configurator = Configurator(target)
configurator.add_slider("gap", "md")
configurator.add_select("justify", ["flex-start", "center", "flex-end"],"center")
configurator.add_select("align", ["flex-start", "center", "flex-end"], "flex-start")
configurator.add_select("direction", ["row", "column", "row-reverse", "column-reverse"], "row")
configurator.add_select("wrap",["wrap", "nowrap", "wrap-reverse"],"wrap")

component = configurator.panel