import dash_mantine_components as dmc

deleted = {"color": "red", "label": "-"}
added = {"color": "green", "label": "+"}

component = dmc.Prism(
    """import { Button } from '@mantine/core';

function Demo() {
  return <Button>Hello</Button>
}

function Usage() {
  return <ActionIcon>Hello</ActionIcon>;
}""",
    language="tsx",
    withLineNumbers=True,
    highlightLines={
        3: deleted,
        4: deleted,
        5: deleted,
        7: added,
        8: added,
        9: added,
    },
)
