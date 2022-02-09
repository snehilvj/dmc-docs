import dash_mantine_components as dmc

component = dmc.MantineProvider(
    theme={
        "colorScheme": "dark",
        # add your colors
        "colors": {
            "deep-blue": ["#E9EDFC", "#C1CCF6", "#99ABF0" "..."],
        },
        "shadows": {
            # other shadows (xs, sm, lg) will be merged from default theme
            "md": "1px 1px 3px rgba(0,0,0,.25)",
            "xl": "5px 5px 3px rgba(0,0,0,.25)",
        },
        "headings": {
            "fontFamily": "Roboto, sans-serif",
            "sizes": {
                "h1": {"fontSize": 30},
            },
        },
    },
    children=[
        # dash/dmc components here
    ],
)
