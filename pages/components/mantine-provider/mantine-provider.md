MantineProvider | MantineProvider component allows you to change theme globally

### Dark Theme

All mantine components support dark color scheme natively without any additional steps. To use dark color scheme wrap
your application in MantineProvider and specify colorScheme.

> example:components/mantine-provider/_dark.py

### Global Styles

theme.colors.dark\\[7\\] shade is considered to be the body background color and theme.colors.dark\\[0\\] shade as text
color with dark color scheme. You can create these styles on your own or add them by setting `withGlobalStyles` prop on
MantineProvider, which includes them by default.

> example:components/mantine-provider/_global.py:no-run

### Further customization

You can further customize your theme such as theme colors, shadows, etc.

> dmc:components/mantine-provider/_refer.py

> example:components/mantine-provider/_theme.py:no-run

> apidoc:MantineProvider
