import dash_mantine_components as dmc

component = dmc.AspectRatio(
    dmc.Image(
        src="https://www.nasa.gov/wp-content/uploads/2022/07/web_first_images_release.png",
        alt="Carina Nebula"
    ),
    ratio=720 / 1080, maw=400, mx="auto"
)