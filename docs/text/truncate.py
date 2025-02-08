import dash_mantine_components as dmc

content = """
Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde provident eos fugiat id
necessitatibus magni ducimus molestias. Placeat, consequatur. Quisquam, quae magnam
perspiciatis excepturi iste sint itaque sunt laborum. Nihil?
"""

component = dmc.Box(
    [
        dmc.Title("truncate='end'", order=5),
        dmc.Text(content, truncate="end"),
        
        dmc.Title("truncate='start'", order=5, mt="lg"),
        dmc.Text(content, truncate="start"),
    ],
    w=300
)
