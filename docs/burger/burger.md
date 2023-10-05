---
name: Burger
description: Use the dmc.Burger component to toggle navigation menus.
endpoint: /components/burger
package: dash_mantine_components
---

.. toc::

### Simple Example

Burger component renders open/close menu button. If it's burger state is clicked, the `opened` property is set to False, and if it's cross state is clicked, the `opened` property is set to False.

.. exec::docs.burger.simple

### Colors

.. exec::docs.burger.color

### Size

```python
import dash_mantine_components as dmc

dmc.Group(
    [
        dmc.Burger(),
        dmc.Burger(size="xs"),
        dmc.Burger(size="md"),
    ]
)
```

.. exec::docs.burger.size
    :code: false

### Styles API

| Name   | Static selector        | Description         |
|:-------|:-----------------------|:--------------------|
| root   | .mantine-Burger-root   | Root button element |
| burger | .mantine-Burger-burger | Burger icon         |

### Keyword Arguments

#### Burger

.. kwargs::Burger
