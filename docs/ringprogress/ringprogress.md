---
name: RingProgress
description: Use the RingProgress component to give feedback to the user about the status of a task with label, sections, etc.
endpoint: /components/ringprogress
package: dash_mantine_components
category: Feedback
---

.. toc::
.. llms_copy::RingProgress

### Simple Example

Set `sections` prop to an array of:
* `value` - number between 0 and 100 - amount of space filled by segment
* `color` - segment color from theme or any other css color value

.. exec::docs.ringprogress.simple

### Root Color

Use `rootColor` property to change the root color.

.. exec::docs.ringprogress.root

### Section Tooltips

Hover on the sections to see tooltips in action.

.. exec::docs.ringprogress.tooltip

### With label

.. exec::docs.ringprogress.label

### Size, Thickness And Rounded Caps

Use `size`, `thickness`, `roundCaps` props to customize the component.

```python
import dash_mantine_components as dmc

dmc.RingProgress(
    size=120,
    thickness=12,
    roundCaps=False,
    sections=[
        {"value": 40, "color": "red"},
        {"value": 15, "color": "yellow"},
        {"value": 15, "color": "violet"},
    ],
)
```

.. exec::docs.ringprogress.interactive
    :code: false

### Styles API

.. styles_api_text::

| Name  | Static selector             | Description    |
|:------|:----------------------------|:---------------|
| root  | .mantine-RingProgress-root  | Root element   |
| svg   | .mantine-RingProgress-svg   | svg element    |
| curve | .mantine-RingProgress-curve | circle element |
| label | .mantine-RingProgress-label | Label element  |

### Keyword Arguments

#### RingProgress

.. kwargs::RingProgress
