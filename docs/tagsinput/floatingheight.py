import dash_mantine_components as dmc

data = [f"Option {i}" for i in range(100)]

component = dmc.TagsInput(
    label="Fits viewport height",
    placeholder="Pick value",
    data=data,
    floatingHeight="viewport",
)