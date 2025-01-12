---
name: Theme Object
description: Mantine theme is an object where your application's colors, fonts, spacing, border-radius and other design tokens are stored.
endpoint: /theme-object
package: dash_mantine_components
category: Theming
order: 2  # sets order in navbar section
---

.. toc::

### Usage


```python
import dash_mantine_components as dmc

dmc.MantineProvider(
    theme={
        # add your colors
        "colors": {
             # add your colors
            "deepBlue": ["#E9EDFC", "#C1CCF6", "#99ABF0" "..."], # 10 colors
            # or replace default theme color
            "blue": ["#E9EDFC", "#C1CCF6", "#99ABF0" "..."],   # 10 colors
        },
        "shadows": {
            # other shadows (xs, sm, lg) will be merged from default theme
            "md": "1px 1px 3px rgba(0,0,0,.25)",
            "xl": "5px 5px 3px rgba(0,0,0,.25)",
        },
        "headings": {
            "fontFamily": "Roboto, sans-serif",
            "sizes": {
                "h1": {"fontSize": '30px'},
            },
        },
    },
    children=[
        # your app layout here
    ],
)
```


### Theme properties
You can find a complete list of all theme properties in the theme object in the references section at the bottom of the 
page. In the next section, we’ll focus on a few key properties to explain them in more detail.

#### Colors

See more information and examples in [Colors](/colors) section

- `colors` adds colors or over-rides named theme colors
- `primaryColor` sets the app's primary (default) accent color 
- `primaryShade` sets the app's primary shade in either light or dark mode

#### Typography

See more information and examples in [Typography](/typography) section

- `fontFamily` – controls font-family in all components except `Title`, `Code` and `Kbd`
- `fontFamilyMonospace` – controls font-family of components that require monospace font: `Code`, `Kbd` and `CodeHighlight`
- `headings.fontFamily` – controls font-family of h1-h6 tags in `Title`, fallbacks to `theme.fontFamily` if not defined
- `fontSizes` - defines the font-size from `xs` to `xl`
- `lineHeights` -defines `line-height` values for `Text` component, most other components use `theme.lineHeights.md` by default

#### Breakpoints

See more information and examples in [Responsive Styles](/responsive-styles) section

#### autoContrast
`autoContrast` controls whether text color should be changed based on the given color prop in the following components:

* `ActionIcon` with `variant='filled'` only
* `Alert` with `variant='filled'` only
* `Avatar` with `variant='filled'` only
* `Badge` with `variant='filled'` only
* `Button` with `variant='filled'` only
* `Chip` with `variant='filled'` only
* `NavLink` with `variant='filled'` only
* `ThemeIcon` with `variant='filled'` only
* `Checkbox` with `variant='filled'` only
* `Radio` with `variant='filled'` only
* `Tabs` with `variant='filled'` only
* `SegmentedControl`
* `Stepper`
* `Pagination`
* `Progress`
* `Indicator`
* `Timeline`
* `Spotlight`
* All dates components that are based on Calendar component

`autoContrast` checks whether the given color luminosity is above or below the `luminanceThreshold` value and changes text color to either `theme.white` or `theme.black` accordingly.

`autoContrast` can be set globally on the theme level or individually for each component via `autoContrast` prop, except for dates components which only support global theme setting.


.. exec::docs.theme-object.autocontrast


#### luminanceThreshold

`luminanceThreshold` controls which luminance value is used to determine if text color should be light or dark. It is 
used only if `theme.autoContrast` is set to `True`. Default value is 0.3.

See a live demo of `luminanceThreshold` in the [Mantine Docs](https://mantine.dev/theming/theme-object/#luminancethreshold)

```python
dmc.MantineProvider(
    dmc.Group([
        dmc.Button("button", color=f"blue.{i}") for i in range(10)
    ]),
    theme={
        "luminanceThreshold": .45,
        "autoContrast": True
    }
)
```

#### focusRing
`theme.focusRing` controls focus ring styles, it supports the following values:

- 'auto' (default and recommended) – focus ring is visible only when the user navigates with keyboard, this is the default browser behavior for native interactive elements
- 'always' – focus ring is visible when user navigates with keyboard and mouse, for example, the focus ring will be visible when user clicks on a button
- 'never' – focus ring is always hidden, it is not recommended – users who navigate with keyboard will not have visual indication of the current focused element


See a live demo of `focusRing` in the [Mantine Docs](https://mantine.dev/theming/theme-object/#focusring)

#### focusClassName

`theme.focusClassName` is a CSS class that is added to elements that have focus styles, for example, `Button` or 
`ActionIcon`. It can be used to customize focus ring styles of all interactive components except inputs. Note that when
`theme.focusClassName` is set, `theme.focusRing` is ignored.

See a live demo of `focusClassName` in the [Mantine Docs](https://mantine.dev/theming/theme-object/#focusclassname)

```python
dmc.MantineProvider(
    dmc.Button("click button to see focus ring", m="lg"),
    theme={"focusClassName": "focus"}
)
```
Define the class in the `.css` file in `/assets` folder
```css

/* Use `&:focus` when you want focus ring to be visible when control is clicked */
.focus {
  &:focus {
    outline: 2px solid var(--mantine-color-red-filled);
    outline-offset: 3px;
  }
}
```


#### activeClassName
`theme.activeClassName` is a CSS class that is added to elements that have active styles, for example, `Button` or
`ActionIcon`. It can be used to customize active styles of all interactive components.

To disable active styles for all components, set `theme.activeClassName` to an empty string.


See a live demo of `activeClassName` in the [Mantine Docs](https://mantine.dev/theming/theme-object/#activeclassname)

#### defaultRadius 

`theme.defaultRadius` controls the default border-radius property in most components, for example, `Button` or `TextInput`.
You can set to either one of the values from `theme.radius` or a number/string to use exact value. Note that numbers are
treated as pixels, but converted to rem. For example, `{'defaultRadius': 4}` will be converted to 0.25rem. You can learn
more about rem conversion in the [rem units guide](https://mantine.dev/styles/rem/).


See a live demo of `defaultRadius` in the [Mantine Docs](https://mantine.dev/theming/theme-object/#defaultradius)

```python

dmc.MantineProvider(
    dmc.Box([
        dmc.Button("Button", m="sm"),
        dmc.TextInput(m="sm", label="TextInput with defaultRadius", placeholder="TextInput with default radius")
    ]),
    theme={"defaultRadius": "xl"},    
)
```

#### cursorType
`theme.cursorType` controls the default cursor type for interactive elements, that do not have cursor: pointer styles 
by default. For example, `Checkbox`.


See a live demo of `cursorType` in the [Mantine Docs](https://mantine.dev/theming/theme-object/#cursortype)


```python
dmc.MantineProvider(
    dmc.Checkbox(label="Pointer cursor", mt="md"),
    theme={"cursorType": 'pointer'},    
)
```

#### defaultGradient
`theme.defaultGradient` controls the default gradient configuration for components that support `variant='gradient'`
(Button, ActionIcon, Badge, etc.).


See a live demo of `defaultGradient` in the [Mantine Docs](https://mantine.dev/theming/theme-object/#defaultgradient)

```python
dmc.MantineProvider(
    dmc.Button("Button with custom default gradient", variant="gradient"),
    theme={
        "defaultGradient": {
            "from": 'orange',
            "to": 'red',
            "deg": 45,
          },
    }  
)
```
#### components defaultProps

Default props  

You can define default props for every Mantine component by setting `theme.components`. These props will be used by
default by all components of your application unless they are overridden by component props.

See a live demo of `defaultProps` in the [Mantine Docs](https://mantine.dev/theming/default-props/)


```python
dmc.MantineProvider(
    dmc.Group(
        [
            dmc.Button("Default button"),
            dmc.Button("Button with props", color="red", variant="filled"),
        ]
    ),
    theme={
        "components": {
            "Button": {
                "defaultProps": {
                    "color": "cyan",
                    "variant": "outline",
                },
            },
        },
    }
)
```

#### components custom variants

See how to add custom variants to `ActionIcon` and `Button` in the theme object, making these variants available globally
across your app. Detailed examples are provided in their respective documentation sections.  Also, see examples live:

- [Live Demo: Button Variants on PyCafe](https://py.cafe/dash.mantine.components/button-custom-variants-demo-0)  
- [Live Demo: ActionIcon Variants on PyCafe](https://py.cafe/dash.mantine.components/actionicon-custom-variants-demo)  

#### components custom sizes

See and example of adding custom sizes in the  [Checkbox](/components/checkbox) section.  Also see a live dome on PyCafe:

- [Live Demo: Checkbox Sizes PyCafe](https://py.cafe/dash.mantine.components/checkbox-custom-sizes-demo) 

#### other 

`theme.other` is an object that can be used to store any other properties that you want to access with the theme objects.

```python
dmc.MantineProvider(
    # your app layout,
    theme={
        "other": {
            "charcoal": "#333333",
            "primaryHeadingSize": 45,
            "fontWeights": {
                "bold": 700,
                "extraBold": 900,
            },
        },
    }
)
```


### Usage in DMC docs

MantineProvider is used to customize theme for these docs as well. The theming is more or less inline with below.

```python
import dash_mantine_components as dmc

app.layout = dmc.MantineProvider(
     forceColorScheme="light",
     theme={
         "primaryColor": "indigo",
         "fontFamily": "'Inter', sans-serif",
         "components": {
             "Button": {"defaultProps": {"fw": 400}},
             "Alert": {"styles": {"title": {"fontWeight": 500}}},
             "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
             "Badge": {"styles": {"root": {"fontWeight": 500}}},
             "Progress": {"styles": {"label": {"fontWeight": 500}}},
             "RingProgress": {"styles": {"label": {"fontWeight": 500}}},
             "CodeHighlightTabs": {"styles": {"file": {"padding": 12}}},
             "Table": {
                 "defaultProps": {
                     "highlightOnHover": True,
                     "withTableBorder": True,
                     "verticalSpacing": "sm",
                     "horizontalSpacing": "md",
                 }
             },
         },
     },
     children=[
         # content
     ],
 )
```

### Default theme

Default theme is available as `dmc.DEFAULT_THEME`. It includes all theme properties with default values. 
When you pass theme override to MantineProvider, it will be deeply merged with the default theme.

.. exec::docs.theme-object.theme
    :code: false



### Theme Object Reference

| **Name**               | **Description**                                                                                                                                                                | **Type**                         |
|:-----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------|
| `focusRing`            | Controls focus ring styles. Options: `auto` (default, shows when navigating with keyboard), `always` (shows for keyboard and mouse), `never` (always hidden, not recommended). | 'auto' or 'always' or 'never'    | 
| `scale`                | rem units scale, adjust if customizing `<html />` font-size. Default: `1` (16px font-size).                                                                                    | `number`                         |
| `fontSmoothing`        | Determines whether `font-smoothing` is applied to the body. Default: `true`.                                                                                                   | `boolean`                        |
| `white`                | Base white color. Example: `#ffffff`.                                                                                                                                          | `string`                         |
| `black`                | Base black color. Example: `#000000`.                                                                                                                                          | `string`                         |
| `colors`               | Object of colors, where each key is a color name, and each value is an array of at least 10 shades. Example: `colors.blue = ['#f0f8ff', '#add8e6', ...]`.                      | `object`                         |
| `primaryShade`         | Determines which shade of `colors.primary` is used. Options: `{light: 6, dark: 8}` (default) or a single number (e.g., `6` for both modes).                                    | `number or object`               |
| `primaryColor`         | Key of `theme.colors`. Determines the default primary color. Default: `blue`.                                                                                                  | `string`                         |
| `variantColorResolver` | Function to resolve colors for variants like `Button` and `ActionIcon`. Can be used for deep customization.                                                                    | `function`                       |
| `autoContrast`         | If `true`, adjusts text color for better contrast based on the background color. Default: `false`.                                                                             | `boolean`                        |
| `luminanceThreshold`   | Threshold for determining whether text should be light or dark when `autoContrast` is enabled. Default: `0.3`.                                                                 | `number`                         |
| `fontFamily`           | Font-family used in all components. Example: `'Arial, sans-serif'`.                                                                                                            | `string`                         |
| `fontFamilyMonospace`  | Monospace font-family used in code components. Example: `'Courier, monospace'`.                                                                                                | `string`                         |
| `headings`             | Controls heading styles. Includes `fontFamily`, `fontWeight`, `textWrap` (e.g., `'wrap'`, `'nowrap'`) and sizes for `h1` to `h6` (e.g., `{'fontSize': 32, 'lineHeight': 1.4}`). | `object`                         |
| `radius`               | Object defining border-radius values. Example: `{sm: 4, md: 8, lg: 16}`.                                                                                                       | `object`                         |
| `defaultRadius`        | Default border-radius used by most components. Example: `md`.                                                                                                                  | `string`                         |
| `spacing`              | Object defining spacing values (e.g., margins, padding). Example: `{xs: 4, sm: 8, md: 16, lg: 24}`.                                                                            | `object`                         |
| `fontSizes`            | Object defining font-size values. Example: `{xs: 12, sm: 14, md: 16, lg: 20}`.                                                                                                 | `object`                         |
| `lineHeights`          | Object defining line-height values. Example: `{xs: 1.2, sm: 1.4, md: 1.6}`.                                                                                                    | `object`                         |
| `breakpoints`          | Object defining responsive breakpoints (in em). Example: `{xs: 30, sm: 48, md: 64}` (for 480px, 768px, and 1024px respectively).                                               | `object`                         |
| `shadows`              | Object defining box-shadow values. Example: `{sm: '0px 1px 3px rgba(0, 0, 0, 0.2)', md: '0px 4px 6px rgba(0, 0, 0, 0.1)'}`.                                                    | `object`                         |
| `respectReducedMotion` | If `true`, respects OS reduce-motion settings. Default: `false`.                                                                                                               | `boolean`                        |
| `cursorType`           | Determines cursor style for interactive elements. Options: `'default'` or `'pointer'`. Default: `'default'`.                                                                   | `'default' or 'pointer'`         |
| `defaultGradient`      | Default gradient configuration. Example: `{'from': '#6a11cb', 'to': '#2575fc', 'deg': 45}`.                                                                                    | `object`                         |
| `activeClassName`      | CSS class applied to elements with active styles (e.g., `Button`).                                                                                                             | `string`                         |
| `focusClassName`       | CSS class applied to elements with focus styles (overrides `focusRing`).                                                                                                       | `string`                         |
| `components`           | Customizations for individual components (e.g., default props for `Button`).                                                                                                   | `object`                         |
| `other`                | User-defined custom properties for additional flexibility.                                                                                                                     | `object`                         |

