---
name: Box
description: Base component for all Mantine components
endpoint: /components/box
package: dash_mantine_components
category: Miscellaneous
---

.. toc::

### Usage

The `Box` component serves as a  base for all other components and can be used as a replacement for `html.Div` as a basic container.

The key advantage of using `Box` is its support for [Style Props](/style-props), allowing for cleaner, more readable styling directly within the component.

### Example
Both examples below produce the same result:

```python
# Using html.Div
html.Div(
    [
        # your content here
    ],
    style={"marginTop": 8, "padding": 24}
)

# Using dmc.Box with Style Props
dmc.Box(
    [
        # your content here
    ],
    mt=8, p=24
)

```

> Please see the [Style Props](/style-props) section for more information.


### Keyword Arguments

#### Box

.. kwargs::Box
