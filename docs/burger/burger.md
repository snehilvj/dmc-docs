---
name: Burger
description: Open/close navigation button. Use the dmc.Burger component to toggle navigation menus.
endpoint: /components/burger
package: dash_mantine_components
category: Navigation
---

.. toc::

### Simple Example

Burger component renders open/close menu button. If it's burger state is clicked, the `opened` property is set to `True`,
and if it's cross state is clicked, the `opened` property is set to `False`.

.. exec::docs.burger.simple

### Size and Line Size

Use `size` prop to control the `Burger` width and height, numbers are converted to rem, 'md' by default.
Use the `lineSize` prop to control height of lines, by default calculated based on `size` prop.  

.. exec::docs.burger.interactive
    :code: false

```python
dmc.Burger(id="burger-button", opened=False, lineSize=2, size="md")
```

### Colors

.. exec::docs.burger.color

### Styles API

This component supports [Styles API](/styles-api). With Styles API, you can customize styles of any inner element.
For more information on styling components,  please also refer to the [Mantine Styles](https://mantine.dev/styles/styles-overview/) documentation.

#### Burger Selectors

| Selector | Static selector         | Description                           |
|----------|--------------------------|---------------------------------------|
| root     | .mantine-Burger-root     | Root element (button)                 |
| burger   | .mantine-Burger-burger   | Inner element that contains burger lines |

#### Burger CSS Variables

| Selector | Variable                            | Description                                |
|----------|-------------------------------------|--------------------------------------------|
| root     | --burger-line-size                  | Controls height of lines                   |
|          | --burger-color                      | Controls background-color of lines         |
|          | --burger-size                       | Controls width and height of the button    |
|          | --burger-transition-duration        | Controls transition-duration of lines      |
|          | --burger-transition-timing-function | Controls transition-timing-function of lines |

#### Burger Data Attributes

| Selector | Attribute    | Condition          |
|----------|--------------|--------------------|
| burger   | data-opened  | `opened` prop is set |

### Keyword Arguments

#### Burger

.. kwargs::Burger
