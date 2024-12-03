import dash_mantine_components as dmc



names = [
    "John Doe",
    "Jane Mol",
    "Alex Lump",
    "Sarah Condor",
    "Mike Johnson",
    "Kate Kok",
    "Tom Smith",
]

avatars = [dmc.Avatar(name=name, color="initials") for name in names]

component = dmc.Group(avatars)