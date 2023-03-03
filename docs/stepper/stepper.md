---
name: Stepper
section: Navigation
head: Display content divided into a steps sequence
description: Use the Stepper, StepperStep and StepperCompleted components to display content divided into a steps sequence
component: Stepper, StepperStep, StepperCompleted
styles: stepper
---

##### Basic usage

.. exec::docs.stepper.basic
    :center: true

##### Color, radius and size

You can use any color from Mantine's theme colors. Colors can also be set on individual steps.

.. exec::docs.stepper.color
    :prism: false

```python
import dash_mantine_components as dmc

dmc.Stepper(
    active=1,
    color="green",
    radius="lg",
    size="sm", 
    children=[
        dmc.StepperStep(label="First step", description="Create an account"),
        dmc.StepperStep(label="Second step", description="Verify email"),
    ],
)
```

Component size is controlled by two props: `size` and `iconSize`. `size` prop controls icon size, label and description font size.
`iconSize` allows to overwrite icon size separately from other size values.

.. exec::docs.stepper.size
    :prism: false

```python
import dash_mantine_components as dmc

dmc.Stepper(
    active=1,
    iconSize=42,
    children=[
        dmc.StepperStep(label="First step", description="Create an account"),
        dmc.StepperStep(label="Second step", description="Verify email"),
    ],
)
```

##### Custom icons

You can replace step icon by setting `icon` prop on Step component. To change completed check icon set `completedIcon` on Stepper component.
You can also change completed icon for each step, for example, to indicate error state.

.. exec::docs.stepper.icons
    :center: true

##### Vertical orientation

.. exec::docs.stepper.vertical
