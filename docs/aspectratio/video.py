import dash_mantine_components as dmc
from dash import html

component = dmc.AspectRatio(
    html.Iframe(
       src="https://www.youtube.com/embed/KsTKREWoVC4",
        title = "YouTube video player",
        allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; fullscreen",
    ),
    ratio=16 / 9
)