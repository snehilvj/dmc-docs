import dash_mantine_components as dbc
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
import copy


def add_figure_templates(default=None):

    """
    Create and register Plotly figure templates styled to match the Mantine default theme with Green Primary color.

    This function generates two custom Plotly templates:
    - "mantine_light" for light mode
    - "mantine_dark" for dark mode

    Templates are registered with `plotly.io.templates`, allowing you to apply them to Plotly figures
    using the template names "mantine_light" or "mantine_dark". These templates include Mantine-inspired
    color palettes, background colors, and other layout customizations.

    Parameters:
    - default (str): The default template to apply globally. Must be either "mantine_light" or "mantine_dark".
                      If not set, the default Plotly template remains unchanged.

    Returns:
    - None: The templates are registered and optionally set as the default, but no value is returned.

    """

    colors = dbc.theme.DEFAULT_THEME["colors"]
    font_family = dbc.theme.DEFAULT_THEME["fontFamily"]

    # Default theme configurations
    default_themes = {
        "light": {
            "colorway": [
                colors[color][6]
                for color in ["green", "red", "blue", "violet", "orange", "cyan", "pink", "yellow"]
            ],
            "paper_bgcolor":  "#ffffff",  # mantine background color
            "plot_bgcolor": "#ffffff",
            "gridcolor": "#dee2e6",
        },
        "dark": {
            "colorway": [
                colors[color][8]
                for color in ["green", "red", "blue", "violet", "orange", "cyan", "pink", "yellow"]
            ],
            "paper_bgcolor":  colors["dark"][7], # mantine background color
            "plot_bgcolor":  colors["dark"][7],
            "gridcolor": "#343a40",
        }
    }

    def make_template(name):
        #Start with either a light or dark Plotly template
        base = "plotly_white" if name == "light" else "plotly_dark"
        template = copy.deepcopy(pio.templates[base])

        layout = template.layout
        theme_config = default_themes[name]

        # Apply theme settings
        layout.colorway = theme_config["colorway"]
        layout.colorscale.sequential = px.colors.sequential.Viridis
        layout.piecolorway = theme_config["colorway"]
        layout.paper_bgcolor = theme_config["paper_bgcolor"]
        layout.plot_bgcolor = theme_config["plot_bgcolor"]
        layout.font.family = font_family

        # Grid settings
        for axis in (layout.xaxis, layout.yaxis):
            axis.gridcolor = theme_config["gridcolor"]
            axis.gridwidth = 0.5
            axis.zerolinecolor = theme_config["gridcolor"]

        # Geo settings
        layout.geo.bgcolor = theme_config["plot_bgcolor"]
        layout.geo.lakecolor = theme_config["plot_bgcolor"]
        layout.geo.landcolor = theme_config["plot_bgcolor"]

        # Hover label settings
        layout.hoverlabel.font.family = font_family

        # Scatter plot settings
        template.data.scatter = (go.Scatter(marker_line_color=theme_config["plot_bgcolor"]),)
        template.data.scattergl = (go.Scattergl(marker_line_color=theme_config["plot_bgcolor"]),)

        return template


    # #register templates
    pio.templates["mantine_light"] = make_template("light")
    pio.templates["mantine_dark"] = make_template("dark")

    # set the default
    if default in ["mantine_light", "mantine_dark"]:
        pio.templates.default = default
    elif default:
        raise ValueError(f"unrecognized {default=}, allowed values are 'mantine_light' and 'mantine_dark'")

    return None