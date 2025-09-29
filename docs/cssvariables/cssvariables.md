---
name: CSS Variables
description: How to use CSS variables with Dash Mantine Components.
endpoint: /css-variables
package: dash_mantine_components
category: Styling
order: 4  # sets order in navbar section
---

.. toc::

MantineProvider exposes all Mantine CSS variables based on the given theme. You can use these variables in CSS files,
style prop or any other styles. See the full list of variables at the bottom of the page.

### Typography variables

#### Font family
The following CSS variables are used to assign font families to all Mantine components:


| Variable                        | Default value           | Description                                              |
|:--------------------------------|:------------------------|:---------------------------------------------------------|
| `mantine-font-family`           | system sans-serif fonts | Controls font-family property of most Mantine components |
| `mantine-font-family-monospace` | system monospace fonts  | Controls font-family property of code blocks             |
| `mantine-font-family-headings`  | system sans-serif fonts | Controls font-family property of headings                |


You can control these variables in the [theme](/theme-object). Note that if `theme.headings.fontFamily` is not set,
`--mantine-font-family-headings` value will be the same as `--mantine-font-family`


```python
theme = {
    # Controls --mantine-font-family
    "fontFamily": "Arial, sans-serif",

    # Controls --mantine-font-family-monospace
    "fontFamilyMonospace": "Courier New, monospace",

    "headings": {
        # Controls --mantine-font-family-headings
        "fontFamily": "Georgia, serif",
    },
}
dmc.MantineProvider(theme=theme, children=[])
```

If you want to use system fonts as a fallback for custom fonts, you can reference `dmc.DEFAULT_THEME` value instead of defining it manually:

```python
import dash_mantine_components as dmc

theme = {
    "fontFamily": f"Roboto, {dmc.DEFAULT_THEME['fontFamily']}"
}
```
You can reference font family variables in your CSS:

```css

.text {
  font-family: var(--mantine-font-family);
}

.code {
  font-family: var(--mantine-font-family-monospace);
}

.heading {
  font-family: var(--mantine-font-family-headings);
}

```

And in `ff` style prop:

- `ff="text"` will use `--mantine-font-family` variable
- `ff="monospace"` will use `--mantine-font-family-monospace` variable
- `ff="heading"` will use `--mantine-font-family-headings` variable


```python
dmc.Text(
    "This text uses --mantine-font-family-monospace variable",
    ff="monospace"
)
```


#### Font size

Font size variables are used in most Mantine components to control text size. The variable that is chosen depends on
the component and its size prop.

| Variable                        | Default value   |
|:--------------------------------|:----------------|
| --mantine-font-size-xs          | 0.75rem (12px)  |
| --mantine-font-size-sm          | 0.875rem (14px) |
| --mantine-font-size-md          | 1rem (16px)     |
| --mantine-font-size-lg          | 1.125rem (18px) |
| --mantine-font-size-xl          | 1.25rem (20px)  |

You can reference font size variables in CSS:

```css
.demo {
  font-size: var(--mantine-font-size-md);
}
```

And in `fz` style prop:
```python
dmc.Text(
    "This text uses --mantine-font-size-xl variable",
    fz="xl"
)
```

To define custom font sizes, can use `theme.fontSizes` property:

```python
theme = {
    'fontSizes': {
    'xs': '0.5rem',
    'sm': '0.75rem',
    'md': '1rem',
    'lg': '1.25rem',
    'xl': '1.5rem',
  },
}
dmc.MantineProvider(theme=theme, children=[])
```


Note that `theme.fontSizes` dict is merged with the dmc.DEFAULT_THEME – it is not required to define all values, only those that you want to change.

```python
theme = {
    'fontSizes': {'xs': '0.5rem'}
}
```

You can add any number of additional font sizes to the `theme.fontSizes` object. These values will be defined as
CSS variables in `--mantine-font-size-{size}` format:


```python
theme = {
    'fontSizes': {
        'xxs': '0.125rem',
        'xxl': '2rem',
    }
}
```

After defining `theme.fontSizes`, you can reference these variables in your CSS:

```css
.demo {
  font-size: var(--mantine-font-size-xxs);
}
```

> Case conversion
>
>Case conversion (camelCase to kebab-case) is not automatically applied to custom font sizes. If you define `theme.fontSizes`
with camelCase keys, you need to reference them in camelCase format. For example, if you define `{ customSize: '1rem' }`, you need to reference it as `--mantine-font-size-customSize`.


#### Line height

Line height variables are used in the Text component. In other components, line-height is either calculated based on font size or set to `--mantine-line-height`, which is an alias for `--mantine-line-height-md`.

| Variable                      | Default value  |
|:------------------------------|:---------------|
| --mantine-line-height         | 1.55           |
| --mantine-line-height-xs      | 1.4            |
| --mantine-line-height-sm      | 1.45           |
| --mantine-line-height-md      | 1.55           |
| --mantine-line-height-lg      | 1.6            |
| --mantine-line-height-xl      | 1.65           |

You can reference line height variables in your CSS:

```css
.demo {
  line-height: var(--mantine-line-height-md);
}
```

```python
dmc.Text("This text uses --mantine-line-height-xl variable", lh="xl")
```

To define custom line heights, you can use theme.lineHeights property:

```python
theme = {
    'lineHeights': {
    'xs': '1.2',
    'sm': '1.3',
    'md': '1.4',
    'lg': '1.5',
    'xl': '1.6',
  },
}
```


#### Headings

`theme.headings` controls `font-size`, `line-height`, `font-weight`, and `text-wrap` CSS properties of headings in `Title` and `TypographyStylesProvider` components.

| Variable                        | Default value   |
|:--------------------------------|:----------------|
| **General variables**           |                 |
| --mantine-heading-font-weight   | 700             |
| --mantine-heading-text-wrap     | wrap            |
| **h1 heading**                  |                 |
| --mantine-h1-font-size          | 2.125rem (34px) |
| --mantine-h1-line-height        | 1.3             |
| --mantine-h1-font-weight        | 700             |
| **h2 heading**                  |                 |
| --mantine-h2-font-size          | 1.625rem (26px) |
| --mantine-h2-line-height        | 1.35            |
| --mantine-h2-font-weight        | 700             |
| **h3 heading**                  |                 |
| --mantine-h3-font-size          | 1.375rem (22px) |
| --mantine-h3-line-height        | 1.4             |
| --mantine-h3-font-weight        | 700             |
| **h4 heading**                  |                 |
| --mantine-h4-font-size          | 1.125rem (18px) |
| --mantine-h4-line-height        | 1.45            |
| --mantine-h4-font-weight        | 700             |
| **h5 heading**                  |                 |
| --mantine-h5-font-size          | 1rem (16px)     |
| --mantine-h5-line-height        | 1.5             |
| --mantine-h5-font-weight        | 700             |
| **h6 heading**                  |                 |
| --mantine-h6-font-size          | 0.875rem (14px) |
| --mantine-h6-line-height        | 1.5             |
| --mantine-h6-font-weight        | 700             |

These variables are used in the `Title` component. The `order` prop controls which heading level to use. For example, `order={3}` Title will use:

- `--mantine-h3-font-size`
- `--mantine-h3-line-height`
- `--mantine-h3-font-weight`


.. exec::docs.title.simple

You can reference heading variables in your CSS:


```css
.h1 {
  font-size: var(--mantine-h1-font-size);
  line-height: var(--mantine-h1-line-height);
  font-weight: var(--mantine-h1-font-weight);
}
```
And in fz and lh style props:

```python
dmc.Text("This text uses --mantine-h1-* variables",  fz="h1", lh="h1")
```

To change heading styles, can use `theme.headings` property:

```python
theme = {
    "headings": {
        "sizes": {
            "h1": {
                "fontSize": "2rem",
                "lineHeight": "1.5",
                "fontWeight": "500",
            },
            "h2": {
                "fontSize": "1.5rem",
                "lineHeight": "1.6",
                "fontWeight": "500",
            },
        },
        # ...
    },
}
```

`theme.headings` dict is deeply merged with the default theme – it is not required to define all values, only those that you want to change.


```python
theme = {
    "headings": {
        "sizes": {
            "h1": {
                "fontSize": "2rem",             
            },          
        },    
    },
}
```


#### Font smoothing

Font smoothing variables control `-webkit-font-smoothing` and `moz-osx-font-smoothing` CSS properties. These variables are used to make text look better on screens with high pixel density.

Font smoothing variables are controlled by the `theme.fontSmoothing` theme property, which is `True` by default. If `theme.fontSmoothing` is `False`, both variables will be set to `unset`.

| Variable                        | Default value  |
|:--------------------------------|:---------------|
| --mantine-webkit-font-smoothing | antialiased    |
| --mantine-moz-font-smoothing    | grayscale      |

If you need to override font smoothing values, the best way is to disable `theme.fontSmoothing` and set global styles on the `body` element:

```python
# Disable font smoothing in your theme
theme = {
  "fontSmoothing": False,
}
```

Add global styles to your project with desired font smoothing values
```css
body {
  -webkit-font-smoothing: subpixel-antialiased;
  -moz-osx-font-smoothing: auto;
}
```


### Colors variables

Colors variables are controlled by `theme.colors` and `theme.primaryColor`. Each color defined in the `theme.colors` object is required to have 10 shades. Theme colors can be referenced by their name and shade index, for example, `--mantine-color-red-6`.

You can define new colors on the theme object or override existing colors:

```python
theme = {
    "colors": {
        "demo": [
            "#FF0000",
            "#FF3333",
            "#FF6666",
            "#FF9999",
            "#FFCCCC",
            "#FFEEEE",
            "#FFFAFA",
            "#FFF5F5",
            "#FFF0F0",
            "#FFEBEB",
        ],
    },
}
```

The code above will define the following CSS variables:

| Variable                      | Default value  |
|:------------------------------|:---------------|
| --mantine-color-demo-0        | #FF0000        |
| --mantine-color-demo-1        | #FF3333        |
| --mantine-color-demo-2        | #FF6666        |
| --mantine-color-demo-3        | #FF9999        |
| --mantine-color-demo-4        | #FFCCCC        |
| --mantine-color-demo-5        | #FFEEEE        |
| --mantine-color-demo-6        | #FFFAFA        |
| --mantine-color-demo-7        | #FFF5F5        |
| --mantine-color-demo-8        | #FFF0F0        |
| --mantine-color-demo-9        | #FFEBEB        |

#### Variant colors

Some Mantine components like `Button` or `Badge` have the `variant` prop that in combination with the `color` prop controls the component text, background, and border colors. For each variant and color, Mantine defines a set of CSS variables that control these colors. For example, for the default blue color the following CSS variables are defined:

| Variable                                         | Default value                 |
|:-------------------------------------------------|:------------------------------|
| **Filled variant**                               |                               |
| --mantine-color-blue-filled                      | var(--mantine-color-blue-6)   |
| --mantine-color-blue-filled-hover                | var(--mantine-color-blue-7)   |
| **Light variant**                                |                               |
| --mantine-color-blue-light                       | rgba(34, 139, 230, 0.1)       |
| --mantine-color-blue-light-hover                 | rgba(34, 139, 230, 0.12)      |
| --mantine-color-blue-light-color                 | var(--mantine-color-blue-6)   |
| **Outline variant**                              |                               |
| --mantine-color-blue-outline                     | var(--mantine-color-blue-6)   |
| --mantine-color-blue-outline-hover               | rgba(34, 139, 230, 0.05)      |


For example, if you use Button component the following way:


.. exec::docs.cssvariables.button

The component will have the following styles:

- Background color will be `var(--mantine-color-pink-filled)`
- Background color on hover will be `var(--mantine-color-pink-filled-hover)`
- Text color will be `var(--mantine-color-white)`
- Border color will be `transparent`

Note that the variables above are not static; they are generated based on the values of `theme.colors` and `theme.primaryShade`. Additionally, their values are different for dark and light color schemes.

#### Variant Colors Variables

Variant colors variables are used in all components that support the `color` prop, for example, `Button`, `Badge`, `Avatar`, and `Pagination`. The color values used by these components are determined by `cssVariablesResolver` and `variantColorResolver`.

#### Primary Color Variables

Primary color variables are defined by `theme.primaryColor` (which must be a key of `theme.colors`). The following CSS variables are defined for the primary color:

| Variable                                      | Default value                                      |
|:----------------------------------------------|:---------------------------------------------------|
| --mantine-primary-color-{shade}               | `var(--mantine-color-{primaryColor}-{shade})`      |
| --mantine-primary-color-filled                | `var(--mantine-color-{primaryColor}-filled)`       |
| --mantine-primary-color-filled-hover          | `var(--mantine-color-{primaryColor}-filled-hover)` |
| --mantine-primary-color-light                 | `var(--mantine-color-{primaryColor}-light)`        |
| --mantine-primary-color-light-hover           | `var(--mantine-color-{primaryColor}-light-hover)`  |
| --mantine-primary-color-light-color           | `var(--mantine-color-{primaryColor}-light-color)`  |

You can reference primary color variables in CSS:

```css
.demo {
  color: var(--mantine-primary-color-0);
  background-color: var(--mantine-primary-color-filled);
}
```

#### Other Color Variables

The following colors are used in various Mantine components. Note that default values are provided for the light color scheme; dark color scheme values are different.

| Variable                          | Description                                             | Default Value                    |
|-----------------------------------|---------------------------------------------------------|----------------------------------|
| --mantine-color-white             | Value of `theme.white`                                  | #fff                             |
| --mantine-color-black             | Value of `theme.black`                                  | #000                             |
| --mantine-color-text              | Color used for text in the body element                 | var(--mantine-color-black)       |
| --mantine-color-body              | Body background color                                   | var(--mantine-color-white)       |
| --mantine-color-error             | Color used for error messages and states                | var(--mantine-color-red-6)       |
| --mantine-color-placeholder       | Color used for input placeholders                       | var(--mantine-color-gray-5)      |
| --mantine-color-dimmed            | Color used for dimmed text                              | var(--mantine-color-gray-6)      |
| --mantine-color-bright            | Color used for bright text                              | var(--mantine-color-black)       |
| --mantine-color-anchor            | Color used for links                                    | var(--mantine-primary-color-6)   |
| --mantine-color-default           | Background color of default variant                     | var(--mantine-color-white)       |
| --mantine-color-default-hover     | Background color of default variant on hover            | var(--mantine-color-gray-0)      |
| --mantine-color-default-color     | Text color of default variant                           | var(--mantine-color-black)       |
| --mantine-color-default-border    | Border color of default variant                         | var(--mantine-color-gray-4)      |


### Spacing variables

`theme.spacing` values are used in most Mantine components to control paddings, margins, and other spacing-related properties. The following CSS variables are defined based on `theme.spacing`:

| Variable               | Default value   |
|------------------------|-----------------|
| --mantine-spacing-xs   | 0.625rem (10px) |
| --mantine-spacing-sm   | 0.75rem (12px)  |
| --mantine-spacing-md   | 1rem (16px)     |
| --mantine-spacing-lg   | 1.25rem (20px)  |
| --mantine-spacing-xl   | 2rem (32px)     |

To define custom spacing values, use the `theme.spacing` property:

```python
theme = {
    "spacing": {
        "xs": "0.5rem",
        "sm": "0.75rem",
        "md": "1rem",
        "lg": "1.5rem",
        "xl": "2rem",
    },
}
```

### Border radius variables

Mantine components that support the `radius` prop use border radius variables to control border radius. The following CSS variables are defined based on `theme.radius`:

| Variable                 | Default value  |
|--------------------------|----------------|
| --mantine-radius-xs      | 0.125rem (2px) |
| --mantine-radius-sm      | 0.25rem (4px)  |
| --mantine-radius-md      | 0.5rem (8px)   |
| --mantine-radius-lg      | 1rem (16px)    |
| --mantine-radius-xl      | 2rem (32px)    |

Additionally, `--mantine-radius-default` variable is defined based on `theme.defaultRadius` value. If the `radius` prop on components is not set explicitly, `--mantine-radius-default` is used instead.

To define custom border radius values, use the `theme.radius` and `theme.defaultRadius` properties:

```python
theme = {
    "defaultRadius": "sm",
    "radius": {
        "xs": "0.25rem",
        "sm": "0.5rem",
        "md": "1rem",
        "lg": "2rem",
        "xl": "3rem",
    },
}
```


### Shadow variables

Shadow variables are used in all Mantine components that support the `shadow` prop. The following CSS variables are defined based on `theme.shadows`:

| Variable              | Default value                                                                                          |
|-----------------------|--------------------------------------------------------------------------------------------------------|
| --mantine-shadow-xs   | 0 1px 3px rgba(0, 0, 0, 0.05), 0 1px 2px rgba(0, 0, 0, 0.1)                                            |
| --mantine-shadow-sm   | 0 1px 3px rgba(0, 0, 0, 0.05), rgba(0, 0, 0, 0.05) 0 10px 15px -5px, rgba(0, 0, 0, 0.04) 0 7px 7px -5px |
| --mantine-shadow-md   | 0 1px 3px rgba(0, 0, 0, 0.05), rgba(0, 0, 0, 0.05) 0 20px 25px -5px, rgba(0, 0, 0, 0.04) 0 10px 10px -5px|
| --mantine-shadow-lg   | 0 1px 3px rgba(0, 0, 0, 0.05), rgba(0, 0, 0, 0.05) 0 28px 23px -7px, rgba(0, 0, 0, 0.04) 0 12px 12px -7px|
| --mantine-shadow-xl   | 0 1px 3px rgba(0, 0, 0, 0.05), rgba(0, 0, 0, 0.05) 0 36px 28px -7px, rgba(0, 0, 0, 0.04) 0 17px 17px -7px|

To define custom shadow values, use the `theme.shadows` property:

```python
theme = {
    "shadows": {
        "xs": "0 1px 2px rgba(0, 0, 0, 0.1)",
        "sm": "0 1px 3px rgba(0, 0, 0, 0.1)",
        "md": "0 2px 4px rgba(0, 0, 0, 0.1)",
        "lg": "0 4px 8px rgba(0, 0, 0, 0.1)",
        "xl": "0 8px 16px rgba(0, 0, 0, 0.1)",
    },
}
```

### z-index variables

z-index variables are defined in `@mantine/core/styles.css`. Unlike other variables, z-index variables are not controlled by the theme and are not exposed in the theme object.

| Variable                  | Default value |
|---------------------------|---------------|
| --mantine-z-index-app     | 100           |
| --mantine-z-index-modal   | 200           |
| --mantine-z-index-popover | 300           |
| --mantine-z-index-overlay | 400           |
| --mantine-z-index-max     | 9999          |

You can reference z-index variables in CSS:

```css
/* Display content above the modal */
.my-content {
  z-index: calc(var(--mantine-z-index-modal) + 1);
}
```

And in components by referencing the CSS variable:

```python
import dash_mantine_components as dmc

dmc.Modal(
    zIndex="var(--mantine-z-index-max)",
    opened=True,
    children="Modal content"
) 
```

### CSS Variables list

#### CSS variables not depending on color scheme
.. exec::docs.cssvariables.cssvariable_list
   :code: false

#### Light color scheme only variables 
.. exec::docs.cssvariables.cssvariable_list_light
   :code: false


#### Dark color scheme only variables
.. exec::docs.cssvariables.cssvariable_list_dark
   :code: false


.. sourcetabs::docs/cssvariables/cssvariables_lists.txt
    :display:none
