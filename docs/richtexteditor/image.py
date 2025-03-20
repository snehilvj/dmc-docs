import dash_mantine_components as dmc

content = """
<p>This is a basic example of implementing images. Drag to re-order.</p>
<img src="https://placehold.co/800x400" />
<img src="https://placehold.co/800x400/6A00F5/white" />      
"""

component = dmc.RichTextEditor(
    html=content,
    extensions=[
        "StarterKit",
        "Image",
    ],
)
