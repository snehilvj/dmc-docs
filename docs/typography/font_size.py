import dash_mantine_components as dmc

from lib.configurator import Configurator

TARGET_ID = "interactive-font-size"

text="""
Dash Mantine Components makes it easy to adjust font size (fz) and line height (lh) for better readability. You can
 set these properties using predefined sizes, from 'xs' to 'xl', ensuring your text is clear and well-spaced. To
  maintain consistency throughout your app, you can customize these defaults in the theme object.
"""

target = dmc.Text(
    text,
    lh="md",
    fz="md",
    id=TARGET_ID,
)

configurator = Configurator(target, TARGET_ID, "Text")


configurator.add_slider("fz", "md")
configurator.add_slider("lh", "md")

component = configurator.panel


