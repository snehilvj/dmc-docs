---
name: Stepper
description: Use the Stepper, StepperStep and StepperCompleted components to display content divided into a steps sequence
endpoint: /components/stepper
package: dash_mantine_components
category: Navigation
---

.. toc::

### Basic usage

.. exec::docs.stepper.basic

### Color, radius and size

You can use any color from Mantine's theme colors. Colors can also be set on individual steps.

.. exec::docs.stepper.color
    :code: false

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
    :code: false

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

### Loading state

To indicate loading state set `loading` prop on `Step` component, `Loader` will replace step icon.

.. exec::docs.stepper.loading

### Custom icons

You can replace step icon by setting `icon` prop on Step component. To change completed check icon set `completedIcon` on Stepper component.
You can also change completed icon for each step, for example, to indicate error state.

.. exec::docs.stepper.icons

### Vertical orientation

.. exec::docs.stepper.vertical

### Styles API

| Name                    | Static selector                          | Description                                   |
|:------------------------|:-----------------------------------------|:----------------------------------------------|
| root                    | .mantine-Stepper-root                    | Root element                                  |
| steps                   | .mantine-Stepper-steps                   | Steps controls wrapper                        |
| separator               | .mantine-Stepper-separator               | Separator line between step controls          |
| verticalSeparator       | .mantine-Stepper-verticalSeparator       | Vertical separator line between step controls |
| separatorActive         | .mantine-Stepper-separatorActive         | Separator active modifier                     |
| verticalSeparatorActive | .mantine-Stepper-verticalSeparatorActive | Vertical separator active modifier            |
| content                 | .mantine-Stepper-content                 | Current step content wrapper                  |
| stepWrapper             | .mantine-Stepper-stepWrapper             | Wrapper for the step icon and separator       |
| step                    | .mantine-Stepper-step                    | Step control button                           |
| stepIcon                | .mantine-Stepper-stepIcon                | Step icon wrapper                             |
| stepCompletedIcon       | .mantine-Stepper-stepCompletedIcon       | Completed step icon, rendered within stepIcon |
| stepBody                | .mantine-Stepper-stepBody                | Contains stepLabel and stepDescription        |
| stepLabel               | .mantine-Stepper-stepLabel               | Step label                                    |
| stepDescription         | .mantine-Stepper-stepDescription         | Step description                              |
| stepLoader              | .mantine-Stepper-stepLoader              | Step loader                                   |

### Keyword Arguments

#### Stepper

.. kwargs::Stepper

#### StepperStep

.. kwargs::StepperStep

#### StepperCompleted

.. kwargs::StepperCompleted
