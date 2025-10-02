---
name: MantineProvider
description: Use MantineProvider component to manage themes in your app globally.
endpoint: /components/mantineprovider
package: dash_mantine_components
category: Theming
order: 1  # sets order in navbar section
---

.. toc::
.. llms_copy::MantineProvider


Wrap your `app.layout` with a single `MantineProvider` to enable theming and styling features across your app. There should only be one `MantineProvider` in your app.

The `MantineProvider`:

1. Sets the global theme, including colors, spacing, and fonts.
2. Handles light and dark mode toggling.
3. Provides Mantine CSS variables according to the selected theme.

### Usage

Your app must be wrapped inside a MantineProvider, and it must be used only once.

```python
import dash_mantine_components as dmc

app.layout = dmc.MantineProvider(
    theme = {...},
    children={...}
)
```

### theme object

See the [Theme Object](/theme-object) section to learn how to customize the default Mantine theme`.


### Custom Colors

See the [Colors](/colors) section to learn how to customize the theme colors.

### Light and Dark Color Schemes
Mantine supports both light and dark color schemes.  The default color scheme is "light".
When the `MantineProvider` is added to your app, it automatically sets the `data-mantine-color-scheme` attribute at the 
top level of the app. This attribute controls whether the app uses light or dark mode. All components in the app 
reference this attribute to decide which colors to apply.

You can change the color scheme with the `forceColorScheme` prop.

In the [Theme Switch Componets](/theme-switch) section, learn how to add a component to allow users to select either light or dark mode.

```python
import dash_mantine_components as dmc

app.layout = dmc.MantineProvider(
    forceColorScheme="dark",
    theme = {...},
    children={...}
)
```

### Keyword Arguments

#### MantineProvider

.. kwargs::MantineProvider
