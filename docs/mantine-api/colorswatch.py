import dash_mantine_components as dmc

colors = dmc.DEFAULT_THEME["colors"]
color_picker_value_mapping = {color: codes[6] for color, codes in colors.items()}
theme_name_mapping = {codes[6]: color for color, codes in colors.items()}
radius_name_mapping = {1: "xs", 2: "sm", 3: "md", 4: "lg", 5: "xl"}

component= dmc.SimpleGrid([
    dmc.Card([
        dmc.Box(h=100, w=100, bg=f"blue.{i}" ),
        dmc.Text(f"blue {i}", size="sm"),
        dmc.Text(f"{colors['blue'][i]}", size="sm", c="dimmed")
    ]) for i in range(10)

], cols={ "base": 5,  "lg": 10 }, spacing="xs")

