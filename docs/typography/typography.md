---
name: Typography
description: How to set fonts, size and line height in the app theme
endpoint: /typography
package: dash_mantine_components
category: Theming
order: 3  # sets order in navbar section
---

.. toc::

### Change fonts

You can change fonts and other text styles for headings, code and all other components with the following theme properties:

- `theme.fontFamily` – controls font-family in all components except `Title`, `Code` and `Kbd`
- `theme.fontFamilyMonospace` – controls font-family of components that require monospace font: `Code`, `Kbd` and `CodeHighlight`
- `theme.headings.fontFamily` – controls font-family of h1-h6 tags in `Title`, fallbacks to `theme.fontFamily` if not defined

In this example, you can toggle between the default fonts and custom fonts specified in the `theme`.

```python
import dash_mantine_components as dmc
from dash import Dash, _dash_renderer, Input, Output
_dash_renderer._set_react_version("18.2.0")

app = Dash(external_stylesheets=dmc.styles.ALL)

component = dmc.Box([
    dmc.SegmentedControl(id="segment", data=["default", "custom-fonts"], value="default"),
    dmc.Box([
        dmc.Title("Greycliff CF title", order=3),
        dmc.Button("Verdana button"),
        dmc.Code("Monaco, Courier Code")
    ], bd=True, m="lg")
], m="lg")

theme= {
  "fontFamily": 'Verdana',
  "fontFamilyMonospace": 'Monaco, Courier, monospace',
  "headings": { "fontFamily": 'Greycliff CF' },
}

app.layout = dmc.MantineProvider(
    component,
    id="provider",
)

@app.callback(
    Output("provider", "theme"),
    Input("segment", "value")
)
def update_font_theme(val):
    if val == "default":
        return {}
    return theme


if __name__ == "__main__":
    app.run(debug=True)
```

Font Explorer
Explore and preview different fonts with this interactive example. The application allows you to select from various font families and see how they look in both regular text and code blocks. It also includes a theme switch to toggle between light and dark modes.
.. exec::docs.typography.font_options
    :code: false

### System fonts
By default, Mantine uses system fonts. It means that different devices will display components based on available font,
for example, macOS and iOS users will see San Francisco font, Windows users will see Segoe UI font, Android users will
see Roboto font and so on. This approach provides a familiar experience to the users and allows avoiding common problems 
related to custom fonts loading (layout shift, invisible text, etc.), if you do not have strict requirements, it is 
recommended to use system fonts for better performance.

Default values for theme properties:

- Default value for `theme.fontFamily` and `theme.headings.fontFamily` is `-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji`
- Default value for `theme.fontFamilyMonospace` is `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace`


### Font Sizes

.. exec::docs.typography.font_size
    :code: false

Default `theme.fontSizes` Values

| Key | Value      | Value in px |
|-----|------------|-------------|
| xs  | 0.75rem    | 12px        |
| sm  | 0.875rem   | 14px        |
| md  | 1rem       | 16px        |
| lg  | 1.125rem   | 18px        |
| xl  | 1.25rem    | 20px        |

You can customize the `fontSizes` defaults in the `theme`: 
```python
theme = {
    "fontSizes" : {
        "xs": "0.75rem",            # customize font sizes here
        "sm": "0.875rem",
        "md": "1rem",
        "lg": "1.125rem",
        "xl": "1.25rem",
    }
}

dmc.MantineProvider(
    # your layout,
    theme=theme
)
```

### Line Heights

`theme.lineHeights` property defines line-height values for `Text` component, most other components use 
`theme.lineHeights.md` by default:

 Default `theme.lineHeights` Values


| Key | Value  |
|-----|--------|
| xs  | 1.4    |
| sm  | 1.45   |
| md  | 1.55   |
| lg  | 1.6    |
| xl  | 1.65   |

You can customize the `lineHeights` defaults in the `theme`:

```python
theme = {
    "lineHeights" : {
        "xs": "1.4",            # customize line heights here
        "sm": "1.45",
        "md": "1.55",
        "lg": "1.6",
        "xl": "1.65",
    }
}

dmc.MantineProvider(
    # your layout,
    theme=theme
)

```

### h1-h6 styles
To customize headings styles in `Title` components set `theme.headings`:

```python
import dash_mantine_components as dmc

theme = {
    "headings": {
        # Properties for all headings
        "fontWeight": "400",
        "fontFamily": "Roboto",
        # Properties for individual headings
        "sizes": {
            "h1": {
                "fontWeight": "100",
                "fontSize": "36px",
                "lineHeight": "1.4",
            },
            "h2": {
                "fontSize": "30px",
                "lineHeight": "1.5",
            },
            # Additional heading levels
            "h6": {
                "fontWeight": "900",
            },
        },
    },
}

dmc.MantineProvider(    
    # your app layout here,
    theme=theme,
)
```

With `theme.headings` you can customize `font-size`, `font-weight` and `line-height` per heading level. If you need
more control over styles, use `:is` selector with [Styles API](/styles-api) to target specific heading level:

You can find a complete minimal example in the [Help Center](https://github.com/snehilvj/dmc-docs/blob/main/help_center/theme/change_headings.py)

```python

theme = {
    "components": {
        "Title": {
            "classNames": {
                "root": "change-heading-demo",
            },
        },
    },
}

dmc.MantineProvider(
    theme=theme,
    children=[
        dmc.Title("Heading 1", order=1),
        dmc.Title("Heading 2", order=2),
        dmc.Title("Heading 3", order=3),
        dmc.Title("Heading 4", order=4),
        dmc.Title("Heading 5", order=5),
        dmc.Title("Heading 6", order=6),
    ],
)
```

In a `.css` file in `/assets` folder add:

```css

.change-heading-demo {
  &:is(h1) {
    font-family: GreycliffCF, sans-serif;
    font-weight: 900;
  }

  &:is(h5, h6) {
    color: var(--mantine-color-dimmed);
  }
}

```

