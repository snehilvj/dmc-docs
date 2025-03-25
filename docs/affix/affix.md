---
name: Affix
description: Use the Affix component to show content at any fixed positon inside your app.
endpoint: /components/affix
package: dash_mantine_components
category: Overlay
---

.. toc::

### Simple Example

Look at the bottom right!

.. exec::docs.affix.simple

### Position prop
The `position` prop controls the affix position on the screen. By default, the component is positioned at `{ bottom: 0, right: 0 }`.  

Accepted Keys:
- `top` (MantineSize | str | number) – Distance from the top.  
- `left`(MantineSize | str | number) – Distance from the left.  
- `bottom`(MantineSize | str | number) – Distance from the bottom.  
- `right` (MantineSize | str | number) – Distance from the right.  

Accepted Value Types:
1. MantineSize (`'xs' | 'sm' | 'md' | 'lg' | 'xl'`) – Uses predefined spacing values.  
2. String (CSS units) (e.g., `"10px"`, `"5rem"`, `"50%"`) – Allows precise control using CSS units.  
3. Number (e.g., `10`, `50`) – Treated as pixel values (`px`).  


Example:
```python
import dash_mantine_components as dmc

dmc.Affix(
    dmc.Button("Floating Button"),
    position={"bottom": "20px", "right": "lg"} 
)
```


### Styles API

.. styles_api_text::

#### Affix selectors

| Selector | Static selector | Description |
|----------|----------------|-------------|
| root     | .mantine-Affix-root | Root element |

#### Affix CSS variables

| Selector | Variable | Description |
|----------|----------|-------------|
| root     | --affix-z-index  | Controls `z-index` property |
| root     | --affix-top      | Controls `top` property |
| root     | --affix-bottom   | Controls `bottom` property |
| root     | --affix-left     | Controls `left` property |
| root     | --affix-right    | Controls `right` property |


### Keyword Arguments

#### Affix

.. kwargs::Affix
