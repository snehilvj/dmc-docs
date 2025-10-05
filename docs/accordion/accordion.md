---
name: Accordion
description: Use the Accordion and AccordionX components to toggle between hiding and showing large amount of content.
endpoint: /components/accordion
package: dash_mantine_components
category: Data Display
---

.. toc::


.. llms_copy::Accordion

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

### Compose control

You can add any additional elements that will be displayed next to `AccordionControl`, for example, you can add `ActionIcon` or `Menu`.
 This enables interaction with the element without affecting the opening or closing of the accordion item. In this
example, try clicking the heart icon.

.. exec::docs.accordion.compose



### Disabled Item

Set `disabled=True` in dmc.AccordionControl to disable it. 

```python
import dash_mantine_components as dmc

dmc.AccordionControl(children=[...], disabled=True)
```

.. exec::docs.accordion.disabled
    :code: false

### Styles API

.. styles_api_text::


#### Accordion selectors

| Selector   | Static selector                | Description                                    |
|------------|---------------------------------|------------------------------------------------|
| root       | .mantine-Accordion-root         | Root element                                   |
| item       | .mantine-Accordion-item         | Accordion.Item root element                    |
| control    | .mantine-Accordion-control      | Accordion.Control root element                 |
| chevron    | .mantine-Accordion-chevron      | Accordion.Control chevron container element    |
| label      | .mantine-Accordion-label        | Accordion.Control label                        |
| icon       | .mantine-Accordion-icon         | Accordion.Control icon                         |
| itemTitle  | .mantine-Accordion-itemTitle    | Accordion.Control title (h2-h6) tag            |
| panel      | .mantine-Accordion-panel        | Accordion.Panel root element                   |
| content    | .mantine-Accordion-content      | Wrapper element of Accordion.Panel children    |


#### Accordion CSS variables

| Selector | Variable                        | Description                                                    |
|----------|----------------------------------|----------------------------------------------------------------|
| root     | --accordion-chevron-size         | Controls chevron container element width and min-width          |
|          | --accordion-radius               | Controls border-radius in various elements, depending on variant |
|          | --accordion-transition-duration  | Controls all animations' transition-duration                    |


#### Accordion data attributes

| Selector      | Attribute               | Condition               | Value                                   |
|---------------|-------------------------|-------------------------|-----------------------------------------|
| item, control | data-active              | Item is active (opened)  | –                                       |
| control       | data-chevron-position    | –                       | Value of `chevronPosition` prop on Accordion |



### Keyword Arguments

#### Accordion

.. kwargs::Accordion

#### AccordionControl

.. kwargs::AccordionControl

#### AccordionItem

.. kwargs::AccordionItem

#### AccordionPanel

.. kwargs::AccordionPanel
