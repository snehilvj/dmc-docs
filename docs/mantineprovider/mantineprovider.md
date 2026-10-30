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


### theme

Use the `theme` prop to customize the Mantine theme. The theme is merged with the default Mantine theme and is available to all DMC components.

See the [Theme Object](/theme-object) section to learn how to customize the default Mantine theme.

For example, you can change the default font and primary color:

```python
import dash_mantine_components as dmc

theme = {
    "fontFamily": "Open Sans, sans-serif",
    "primaryColor": "cyan",
}

app.layout = dmc.MantineProvider(
    theme=theme,
    children=dmc.Text("Hello")
)
```

See the [Mantine theme documentation](https://mantine.dev/llms/theming-theme-object.md) for the available theme options.


### Light and Dark Color Schemes
Mantine supports both light and dark color schemes.  The default color scheme is "light".
When the `MantineProvider` is added to your app, it automatically sets the `data-mantine-color-scheme` attribute at the 
top level of the app. This attribute controls whether the app uses light or dark mode. All components in the app 
reference this attribute to decide which colors to apply.

You can change the color scheme with the `forceColorScheme` prop.

In the [Theme Switch Components](/theme-switch) section, learn how to add a component to allow users to select either light or dark mode.

```python
import dash_mantine_components as dmc

app.layout = dmc.MantineProvider(
    forceColorScheme="dark",
    theme = {...},
    children={...}
)
```



### cssVariablesSelector

`cssVariablesSelector` specifies the CSS selector to which Mantine CSS variables are added.

```python
dmc.MantineProvider(
    cssVariablesSelector="html",
    children=dmc.Text("Hello")
)
```

By default, Mantine variables are added to the root element.

### withCssVariables

`withCssVariables` determines whether Mantine CSS variables are generated. It defaults to `True`.

```python
dmc.MantineProvider(
    withCssVariables=False,
    children=dmc.Text("Hello")
)
```

You normally should not disable this option. If you do, you will need to provide the required CSS variables yourself.

### deduplicateCssVariables

`deduplicateCssVariables` determines whether CSS variables that have the same value as the default theme are omitted.

It defaults to `True`. Set it to `False` if you need all Mantine CSS variables to be generated.

```python
dmc.MantineProvider(
    deduplicateCssVariables=False,
    children=dmc.Text("Hello")
)
```

### classNamesPrefix

`classNamesPrefix` sets the prefix used for Mantine component static classes. The default is `"mantine"`.

```python
dmc.MantineProvider(
    classNamesPrefix="app",
    children=dmc.Text("Hello")
)
```

With the default prefix, a component such as `Text` has a static class such as `mantine-Text-root`. Setting `classNamesPrefix="app"` changes this to `app-Text-root`.

This only changes static component classes. It does not change Mantine's generated component classes or global utility classes.

### withStaticClasses

`withStaticClasses` determines whether Mantine component static classes are generated. It defaults to `True`.

```python
dmc.MantineProvider(
    withStaticClasses=False,
    children=dmc.Text("Hello")
)
```

Static classes are used by the Mantine Styles API and can also be useful when writing custom CSS.

### withGlobalClasses

`withGlobalClasses` determines whether Mantine global utility classes are generated. It defaults to `True`.

Global classes are required for features such as `hiddenFrom`, `visibleFrom`, `lightHidden`, and `darkHidden`.

```python
dmc.MantineProvider(
    withGlobalClasses=False,
    children=dmc.Text("Hello")
)
```

You normally should not disable this option because some Mantine components and style props depend on the global classes.

### deduplicateInlineStyles

`deduplicateInlineStyles` enables React 19 style tag deduplication for responsive style props.

When enabled, components that use identical responsive style props can share a single generated `<style>` tag instead of each generating their own.

```python
dmc.MantineProvider(
    deduplicateInlineStyles=True,
    children=dmc.Text("Hello")
)
```

This can improve performance when many components use the same responsive style values.

### cssVariablesResolver

`cssVariablesResolver` is a function that generates CSS variables based on the theme.

DMC supports functions as props using the `window.dashMantineFunctions` mechanism. For example, a function can be registered in JavaScript and then referenced from Python.

```python
dmc.MantineProvider(
    cssVariablesResolver={"function": "myCssVariablesResolver"},
    children=dmc.Text("Hello")
)
```

See the [Functions as Props](../advanced/functions-as-props) documentation for more information.

### useV8CssVariablesResolver

`useV8CssVariablesResolver` enables Mantine's v8 CSS variable resolver.

This option is provided for applications that need compatibility with the CSS variable behavior used by Mantine v8. It defaults to `False`.

```python
dmc.MantineProvider(
    useV8CssVariablesResolver=True,
    children=dmc.Text("Hello")
)
```

If both `useV8CssVariablesResolver` and `cssVariablesResolver` are specified, the explicitly provided `cssVariablesResolver` takes precedence.

This option is specific to DMC v3 and is not part of the Mantine `MantineProvider` API.


### Keyword Arguments


#### MantineProvider

.. kwargs::MantineProvider
