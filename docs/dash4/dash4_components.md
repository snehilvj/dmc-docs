---
name: Dash 4 Components
description: Style Dash 4 Core Components with a Mantine theme
endpoint: /dash4-components
category: Dash
---

.. toc::
.. llms_copy::Dash 4 Components

Dash 4 completely redesigned its core components for a consistent look and feel and added many new features. Components 
like `dcc.Slider` and `dcc.Dropdown` now include functionality not available in DMC, making them useful to mix into your
app when needed.  This section shows how to style Dash 4 components to match a Mantine theme in light and dark mode.


### Dash 4 Accent Color

The accent for Dash 4 components is controlled by a CSS variable so it's easy to change. The value can be any valid CSS color.

This example changes the default purple color to your Mantine primary color:

```python
style={
    "--Dash-Fill-Interactive-Strong": "var(--mantine-primary-color-filled)"
}
```


### Dark Mode Support

Dash 4 components do not include built-in dark mode support. You can enable light and dark mode by mapping Dash CSS
variables to Mantine theme variables.

Add the following CSS to `assets/`:

```css
.dmc {
    --Dash-Stroke-Strong: var(--mantine-color-default-border);
    --Dash-Stroke-Weak: var(--mantine-color-disabled);
    --Dash-Fill-Interactive-Strong: var(--mantine-primary-color-filled);
    --Dash-Fill-Inverse-Strong: var(--mantine-color-body);
    --Dash-Text-Primary: var(--mantine-color-text);
    --Dash-Text-Strong: var(--mantine-color-text);
    --Dash-Text-Disabled: var(--mantine-color-dimmed);
    --Dash-Text-Weak: var(--mantine-color-dimmed);
}

:root[data-mantine-color-scheme="dark"] .dmc {
    --Dash-Fill-Inverse-Strong: var(--mantine-color-dark-6);
    --Dash-Fill-Weak: rgba(255, 255, 255, 0.06);
    --Dash-Fill-Primary-Hover: rgba(255, 255, 255, 0.08);
    --Dash-Fill-Primary-Active: rgba(255, 255, 255, 0.12);
    --Dash-Fill-Disabled: rgba(255, 255, 255, 0.15);
}
```

Wrap your app layout with  `dmc` class:

```python
app.layout = dmc.MantineProvider(
    dmc.Container(
        [...],
        className="dmc"
    )
)
```

Dash 4 components inside this container will follow the Mantine color scheme and update automatically when the theme changes.


### Example 1: dcc.Dropdown

This example shows how a `dcc.Dropdown` works well with other DMC inputs in grids or forms.

The Dash 4 `dcc.Dropdown` supports virtualization, which renders only the visible options instead of the entire list.
This improves performance and responsiveness when working with large data sets. It also includes a search input and
Select all / Deselect all buttons inside the dropdown menu. When `multi=True`, it displays a count of selected items,
preventing the input from resizing as selections grow.

The `dmc.InputWrapper` is used to add elements like `label`, `description`, and `error` to the `dcc.Dropdown`,
making it consistent with the other DMC inputs. The `htmlFor` prop links the label to the component for focus and accessibility.

.. exec::docs.dash4.dropdown



### Example 2: dcc.Slider

The `dcc.Slider` includes optional numeric input fields and automatic mark generation based on range and width.  There is
also an option for a vertical slider.

This example shows the `dcc.Slider` styled with a Mantine theme.

.. exec::docs.dash4.slider



### Migrating to Dash v4

All component props remain unchanged, so upgrading should not introduce errors. You may notice layout and style differences due to the redesign.

Custom CSS written for Dash 3 components will not apply to Dash 4. The components were fully rewritten, so selectors have changed. Start with the styling approach shown here and customize as needed for your app.
