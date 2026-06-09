import dash_mantine_components as dmc
from .data import data

component = dmc.Heatmap(
    data=data,
    startDate="2024-02-16",
    endDate="2025-02-16",
    colors=[
        'var(--mantine-color-orange-4)',
        'var(--mantine-color-orange-6)',
        'var(--mantine-color-orange-7)',
        'var(--mantine-color-orange-9)',
      ]
)