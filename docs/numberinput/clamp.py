import dash_mantine_components as dmc

component = dmc.NumberInput(
    label="You cannot enter number less than 0 or greater than 100",
    placeholder="You cannot enter number less than 0 or greater than 100",
    clampBehavior="strict",
    min=0,
    max=100,
    w=450,
)
