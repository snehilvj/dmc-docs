import dash_mantine_components as dmc
from dash import html, dcc
from .data import data

# Define patterns for custom colors
pattern_definitions = dcc.Markdown('''
<svg>
  <defs>
    <pattern id="diagonalStripes" patternUnits="userSpaceOnUse" width="6" height="8" patternTransform="rotate(45)">
      <rect width="2" height="8" fill="rgba(0, 128, 128, 0.7)"></rect>
    </pattern>
    <pattern id="crosshatch" patternUnits="userSpaceOnUse" width="8" height="8">
      <path d="M 0 0 L 8 0 L 8 8 L 0 8 Z" fill="none" stroke="rgba(75, 0, 130, 0.7)" strokeWidth="1"></path>
      <path d="M 0 0 L 8 8" stroke="rgba(75, 0, 130, 0.7)" strokeWidth="1"></path>
      <path d="M 8 0 L 0 8" stroke="rgba(75, 0, 130, 0.7)" strokeWidth="1"></path>
    </pattern>
  </defs>
</svg>
''', dangerously_allow_html=True)

component = html.Div([
    pattern_definitions,
    dmc.BarChart(
        h=300,
        dataKey="month",
        data=data,
        type="stacked",
        series=[
            {"name": "Smartphones", "color": "url(#crosshatch)"},
            {"name": "Laptops", "color": "blue.6"},
            {"name": "Tablets", "color": "url(#diagonalStripes)"},
        ],
    )
])
