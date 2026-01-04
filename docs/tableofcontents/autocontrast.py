import dash_mantine_components as dmc

component = dmc.TableOfContents(
    selector=".mantine-AppShell-main :is( h2, h3, h4)",
    variant="filled",
    color="yellow.3",
    autoContrast=True,
    size="sm",
    radius="sm",
    w=300
)