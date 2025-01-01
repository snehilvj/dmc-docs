"""
const theme = createTheme({
  autoContrast: true,
  luminanceThreshold: 0.33,
});

function Wrapper(props: any) {
  const buttons = Array(10)
    .fill(0)
    .map((_, index) => (
      <Button
        key={index}
        color={`blue.${index}`}
      >
        Button
      </Button>
    ));

  return (
    <MantineProvider theme={theme}>
      <Stack>{buttons}</Stack>
    </MantineProvider>
  );
}
"""
import dash_mantine_components as dmc
from dash import Dash

component = dmc.Stack([
    dmc.Button(f"button", color=f"blue.{i}") for i in range(10)
])

