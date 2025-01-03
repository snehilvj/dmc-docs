from dash import html
import dash_mantine_components as dmc

# don't do this - It works in that the `size` changes based on screen size, but wont
# work in callbacks.  Plus you could have different user inputs showing on different
# screen sizes
component = html.Div([
    dmc.TextInput(size="xs", hiddenFrom="sm", label="My input", placeholder="My input"),
    dmc.TextInput(size="xl", visibleFrom="sm", label="My input", placeholder="My input"),
])

