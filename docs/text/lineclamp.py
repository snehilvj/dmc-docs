import dash_mantine_components as dmc

from lib.configurator import Configurator


content = """
Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde provident eos fugiat id
necessitatibus magni ducimus molestias. Placeat, consequatur. Quisquam, quae magnam
perspiciatis excepturi iste sint itaque sunt laborum. Nihil?
"""

target = dmc.Text(content + content, w=400)

configurator = Configurator(target)
configurator.add_slider("size", "sm")
configurator.add_number_slider("lineClamp", 2, min=1, max=10)


component = configurator.panel
