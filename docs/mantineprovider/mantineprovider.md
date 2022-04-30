---
name: MantineProvider
section: Miscellaneous
head: MantineProvider component allows you to change theme globally.
description: Use MantineProvider component to enable dark theme in your app globally.
component: MantineProvider
---

##### Dark Theme

All mantine components support dark color scheme natively without any additional steps. To use dark color scheme wrap
your application in MantineProvider and specify colorScheme.

.. exec::docs.mantineprovider.dark

##### Global Styles

theme.colors.dark[7] shade is considered to be the body background color and theme.colors.dark[0] shade as text color
with dark color scheme. You can create these styles on your own or add them by setting withGlobalStyles prop on 
MantineProvider, which includes them by default.

```python
import dash_mantine_components as dmc

component = dmc.MantineProvider(withGlobalStyles=True, theme={"colorScheme": "dark"})
```

##### Further Customization

You can further customize your theme such as theme colors, shadows, etc. Refer to
[mantine.dev](https://mantine.dev/theming/mantine-provider/) for more information.

```python
import dash_mantine_components as dmc

dmc.MantineProvider(
    theme={
        "colorScheme": "dark",
        # add your colors
        "colors": {
            "deep-blue": ["#E9EDFC", "#C1CCF6", "#99ABF0" "..."],
        },
        "shadows": {
            # other shadows (xs, sm, lg) will be merged from default theme
            "md": "1px 1px 3px rgba(0,0,0,.25)",
            "xl": "5px 5px 3px rgba(0,0,0,.25)",
        },
        "headings": {
            "fontFamily": "Roboto, sans-serif",
            "sizes": {
                "h1": {"fontSize": 30},
            },
        },
    },
    children=[
        # dash/dmc components here
    ],
)
```

##### Usage in dmc-docs

MantineProvider is used to customize theme for these docs as well. The theming is more or less inline with below. You 
need to load fonts separately.

```python
import dash_mantine_components as dmc

layout = dmc.MantineProvider(
    theme={
        "colorScheme": "light",
        "fontFamily": "'Inter', sans-serif",
        "primaryColor": "indigo",
    },
    styles={
        "Button": {"root": {"fontWeight": 400}},
        "Alert": {"title": {"fontWeight": 500}},
        "AvatarsGroup": {"truncated": {"fontWeight": 500}},
    },
    withGlobalStyles=True,
    withNormalizeCSS=True,
    children=[],
)
```
