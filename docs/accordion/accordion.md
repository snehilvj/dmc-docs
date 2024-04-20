---
name: Accordion
description: Use the Accordion and AccordionX components to toggle between hiding and showing large amount of content.
endpoint: /components/accordion
package: dash_mantine_components
category: Data Display
---

.. toc::

### Introduction

.. exec::docs.accordion.interactive
    :code: false

### Multiple Items

Set `multiple=True` to enable opening multiple items.

```python
import dash_mantine_components as dmc

dmc.Accordion(
    children=[...],
    multiple=True
)
```

.. exec::docs.accordion.multiple
    :code: false

### Custom Accordion Label

.. exec::docs.accordion.label

### Customizing chevron

You can use [dash-iconify](/dash-iconify) to change the chevron icon.

```python
import dash_mantine_components as dmc
from dash_iconify import DashIconify

dmc.Accordion(
    chevron=DashIconify(icon="ant-design:plus-outlined"),
    disableChevronRotation=True,
    children=[...]
)
```

.. exec::docs.accordion.chevron
    :code: false

### With icons

.. exec::docs.accordion.icons

### Change transition

```python
import dash_mantine_components as dmc

dmc.Accordion(
    children=[...],
    transitionDuration=1000
)
```

.. exec::docs.accordion.transition
    :code: false

### Default opened items

Provide a default value using the `value` prop.

```python
import dash_mantine_components as dmc

dmc.Accordion(
    children=[...],
    value="flexibility"
)
```

If `multiple` is `True`, then value will be a list:

```python
import dash_mantine_components as dmc

dmc.Accordion(
    children=[...],
    value=["flexibility", ]
)
```

.. exec::docs.accordion.default

### Callbacks and State Management

.. exec::docs.accordion.state

### Disabled Item

Set `disabled=True` in dmc.AccordionControl to disable it. 

```python
import dash_mantine_components as dmc

dmc.AccordionControl(children=[...], disabled=True)
```

.. exec::docs.accordion.disabled
    :code: false

### Styles API

| Name      | Static selector              | Description                               |
|-----------|------------------------------|-------------------------------------------|
| root      | .mantine-Accordion-root      | Root element                              |
| item      | .mantine-Accordion-item      | Accordion item wrapper                    |
| itemTitle | .mantine-Accordion-itemTitle | Optional heading element wrapping control |
| control   | .mantine-Accordion-control   | Control root                              |
| label     | .mantine-Accordion-label     | Control label                             |
| icon      | .mantine-Accordion-icon      | Control icon                              |
| chevron   | .mantine-Accordion-chevron   | Control chevron icon                      |
| panel     | .mantine-Accordion-panel     | Panel root                                |
| content   | .mantine-Accordion-content   | Panel content                             |

### Keyword Arguments

#### Accordion

.. kwargs::Accordion

#### AccordionControl

.. kwargs::AccordionControl

#### AccordionItem

.. kwargs::AccordionItem

#### AccordionPanel

.. kwargs::AccordionPanel
