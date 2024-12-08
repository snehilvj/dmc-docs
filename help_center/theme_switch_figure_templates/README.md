This app demos:
- Theme switch light/dark.  This theme switch is based on the `dmc.Switch` with icons in the labels
- Uses a clientside callback to update the Mantine theme.
- `add_figure_templates` function for mantine_light and mantine_dark Plotly figure templates
- updating figure templates in a callback using Patch
- updating multiple figures using pattern matching callback
- The figures use `dcc.Loading(delay_hide=800)` to reduce the flashing when switching themes

<img src="/help_center/theme_switch_figure_templates/img_dark.png" />

<img src="/help_center/theme_switch_figure_templates/img_light.png" />
