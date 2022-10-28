---
name: RadioGroup
section: Inputs & Buttons
head: Capture user feedback limited to small set of options.
description: RadioGroup component gives user radio inputs to allow only one selection from a small set of options. 
component: RadioGroup
---

##### Interactive Demo

Use RadioGroup when you need to capture user feedback limited to small set of options. It can be customized using 
`spacing`, `size`, etc.

.. exec::docs.radiogroup.interactive
    :prism: false

##### Callbacks

Use the `value` prop for callbacks.

.. exec::docs.radiogroup.callback

##### Size

You can set the size of the component from one of xs, sm, md, lg and xl using the `size` prop.

```python
import dash_mantine_components as dmc

dmc.RadioGroup(size="lg")
```

##### Color

In a RadioGroup component, the color property is not customized at the individual Radio level.

.. exec::docs.radiogroup.color
