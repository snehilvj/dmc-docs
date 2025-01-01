---
name: MantineProvider
description: Use MantineProvider component to enable dark theme in your app globally.
endpoint: /components/mantineprovider
package: dash_mantine_components
category: Theming
---

.. toc::

### Usage

Your app must be wrapped inside a MantineProvider, and it must be used only once.

```python
import dash_mantine_components as dmc

app.layout = dmc.MantineProvider(
    theme = {...},
    children={...}
)
```

### theme

See the [Theme Object](/theme-object) section to learn how to customize the default Mantine theme.


### Color Scheme

Color Scheme is currently controlled using the prop `forceColorScheme`.

```python
import dash_mantine_components as dmc

app.layout = dmc.MantineProvider(
    forceColorScheme="dark",
    theme = {...},
    children={...}
)
```


### Custom Colors

You can add custom colors using MantineProvider, other than the ones found in `dmc.DEFAULT_THEME['colors']`.
Use [this](https://omatsuri.app/color-shades-generator) tool to generate 10 shades of the color you like. Mantine's
styling system needs 10 shades for any color so that it can use the right one depending on the colorScheme.

You can also use the same color 10 times but using the tool will give you better results. You can add more than 10 values
as well but the extra values will not be used by Mantine.

.. exec::docs.mantineprovider.colors
    :code: false

```python
import dash_mantine_components as dmc

dmc.MantineProvider(
    theme={
        "colors": {
            "myColor": [                
              "#F2FFB6",
              "#DCF97E",
              "#C3E35B",
              "#AAC944",
              "#98BC20",
              "#86AC09",
              "#78A000",
              "#668B00",
              "#547200",
              "#455D00",                
            ]
        },
    },
    children=[dmc.Button("Custom Colors!", color="myColor")],
)
```

### Keyword Arguments

#### MantineProvider

.. kwargs::MantineProvider
