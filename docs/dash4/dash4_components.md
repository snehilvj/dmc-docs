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
app when needed. 

This section explains how to style Dash 4 components to match a Mantine theme in light and dark mode.


### dcc.Dropdown

The Dash 4 `dcc.Dropdown` features not in `dmc.Select` or `dmc.MultiSelect`:

* Built-in search input inside the menu
* Select all and deselect all actions
* Virtualization for large option lists
* Compact display when `multi=True`



### dcc.Slider

The Dash 4 `dcc.Slider` adds:

* Optional numeric input fields
* Automatic mark generation based on range and width
* Vertical slider option



### Styling Dash 4 Components

Dash 4 components do not automatically use Mantine styles. To keep a consistent appearance, you can style them using
Mantine CSS variables. Styles can be applied using the `style` or `className` prop.


### Accent Color

To change the accent color of Dash 4 components, set the Dash CSS variable. This example matches the accent color to your Mantine primary color:

```python
style={
    "--Dash-Fill-Interactive-Strong": "var(--mantine-primary-color-filled)"
}
```

This is sufficient for apps that only use light mode.



### Light and Dark Mode

For apps with light and dark mode, map Dash CSS variables to Mantine theme variables. Add the following CSS to `assets/`:

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

Wrap your layout:

```python
app.layout = dmc.MantineProvider(
    dmc.Container(
        [...],
        className="dmc"
    )
)
```

Dash 4 components inside this container will follow the Mantine color scheme and update automatically when the theme changes.



### Example 1: A Mix of DMC and Dash 4 Components

This example shows how a styled Dash 4 component works well with DMC inputs (`NumberInput`, `DatePickerInput`) in grids or forms.

Use `dmc.InputWrapper` to add elements like `label`, `description`, and `error` to components such as `dcc.Dropdown`,
making them consistent with DMC inputs. The `htmlFor` prop links the label to the component for focus and accessibility.

.. exec::docs.dash4.dropdown



### Example 2: Slider

This example shows the `dcc.Slider` styled with a Mantine theme.

.. exec::docs.dash4.slider



### Migrating to Dash v4

All component props remain unchanged, so upgrading should not introduce errors. You may notice layout and style differences due to the redesign.

Custom CSS written for Dash 3 components will not apply to Dash 4. The components were fully rewritten, so selectors have changed. Start with the styling approach shown here and customize as needed for your app.
