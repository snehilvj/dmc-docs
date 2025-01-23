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

component = dmc.Group(
    [
        dmc.Avatar(name=n, color="initials", allowedInitialsColors=["blue", "red"])
        for n in names
    ]
)
