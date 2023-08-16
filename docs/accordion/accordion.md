---
name: Accordion
description: Use the Accordion and AccordionX components to toggle between hiding and showing large amount of content.
endpoint: /components/accordion
package: dash_mantine_components
---

.. toc::

## Accordion

### Introduction

.. exec::docs.accordion.interactive
    :code: false

### Multiple Items

Set `multiple=True` to enable opening multiple items.

```python
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
dmc.Accordion(
    children=[...],
    value="flexibility"
)
```

If `multiple` is `True`, then value will be a list:

```python
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
dmc.AccordionControl(children=[...], disabled=True)
```

.. exec::docs.accordion.disabled
    :code: false

### Styles API

.. exec::docs.accordion.styles

### Keyword Arguments

#### Accordion
.. kwargs::Accordion

#### AccordionControl
.. kwargs::AccordionControl

#### AccordionItem
.. kwargs::AccordionItem

#### AccordionPanel
.. kwargs::AccordionPanel
