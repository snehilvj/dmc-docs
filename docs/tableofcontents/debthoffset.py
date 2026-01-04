import dash_mantine_components as dmc

component = dmc.TableOfContents(
    selector=".mantine-AppShell-main :is( h2, h3, h4)",
    variant="filled",
    color="blue",
    size="sm",
    radius="sm",
    minDepthToOffset=0,
    depthOffset=40,
    w=300
)