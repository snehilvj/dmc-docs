---
name: Spoiler
description: Use the Spoiler component to hide long sections of content.
endpoint: /components/spoiler
package: dash_mantine_components
category: Data Display
---

.. toc::
.. llms_copy::Spoiler

### Simple Example

Use Spoiler to hide long sections of content. Pass `maxHeight` prop to control the point at which content will be
hidden under the spoiler and control to show/hide extra appears. If content height is less than `maxHeight`, spoiler
will just render children.

Props `hideLabel` and `showLabel` are required - they are used as spoiler toggle button label in corresponding state.

.. exec::docs.spoiler.simple
    :code: false

```python
import dash_mantine_components as dmc

# very long string
text = ""

component = dmc.Spoiler(
    showLabel="Show more",
    hideLabel="Hide",
    maxHeight=50,
    children=[dmc.Text(text)],
)
```

### Accessibility

The Spoiler component includes ARIA attributes and keyboard support for screen reader users:

* The toggle button uses `aria-expanded` to indicate whether the content is expanded or collapsed.
* The content region uses `role="region"` and is associated with the toggle button through `aria-controls`.
* The spoiler can be toggled with Space or Enter when the button is focused.

### Best practices for label text

Use descriptive labels for `showLabel` and `hideLabel` that clearly describe the action:

```python
import dash_mantine_components as dmc

dmc.Spoiler(
    showLabel="Show full article",
    hideLabel="Hide article",
)
```

Other good examples include `"Expand details"` / `"Collapse details"`. Avoid vague labels such as `"More"` / `"Less"` or `"..."`.

### Custom accessibility labels

If the visible button labels do not clearly describe the action, use `showAriaLabel` and `hideAriaLabel` to provide descriptive labels for screen readers:

```python
import dash_mantine_components as dmc

component = dmc.Spoiler(
    showLabel="👁️",
    hideLabel="👁️",
    showAriaLabel="Show discussion comments",
    hideAriaLabel="Hide discussion comments",
    children="Comments content",
)
```

The `showAriaLabel` and `hideAriaLabel` values are used as the accessible labels for the toggle button.


### Styles API

.. styles_api_text::

| Name    | Static selector          | Description                                    |
|:--------|:-------------------------|:-----------------------------------------------|
| root    | .mantine-Spoiler-root    | Root element                                   |
| content | .mantine-Spoiler-content | Wraps content to set max-height and transition |
| control | .mantine-Spoiler-control | Show/hide content control                      |


### Keyword Arguments
.. style_props_text::

#### Spoiler

.. kwargs::Spoiler
