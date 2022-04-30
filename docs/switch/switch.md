---
name: Switch
section: Inputs & Buttons
head: Capture boolean input from user.
description: Use the Switch component to capture boolean input from user.
component: Switch
---

##### Interactive Demo

.. exec::docs.switch.interactive
    :prism: false

##### Radius and Size

Set the radius and size of the Switch component using the `radius` and `size` prop respectively.

```python
import dash_mantine_components as dmc

dmc.Switch(
    size="lg",
    radius="sm",
    label="Enable this option",
    checked=True
)
```

##### Callbacks

Use the property `checked` to use dmc.Switch in callbacks.

.. exec::docs.switch.callback

##### Inner Labels

```python
import dash_mantine_components as dmc

dmc.Switch(
    label="I agree to sell my privacy",
    onLabel="ON",
    offLabel="OFF"
)
```

.. exec::docs.switch.label
    :prism: false
