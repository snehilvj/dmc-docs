---
name: MantineProvider
description: Use MantineProvider component to manage themes in your app globally.
endpoint: /components/mantineprovider
package: dash_mantine_components
category: Theming
order: 1  # sets order in navbar section
---

.. toc::


Your `app.layout` must be wrapped with a single `MantineProvider`. Only one `MantineProvider` should be used in an app. 
It is responsible for:  

1. Providing the Theme: Controls the overall theme of the app (for example, colors, spacing, fonts).  
2. Setting the Color Scheme: Manages light or dark mode.  
3. Customizing Global Styles: Applies app-wide styles and configurations.
4. Adding CSS variables to the document


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

### Color Scheme
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
