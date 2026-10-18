import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Text(
    """
    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quasi voluptatibus inventore iusto
      cum dolore molestiae perspiciatis! Totam repudiandae impedit maxime!
    """,
    textWrap="wrap"

)

configurator = Configurator(target)

configurator.add_select("textWrap", ["wrap", "balance", "pretty", "stable", "nowrap"], "wrap")
component = configurator.panel
