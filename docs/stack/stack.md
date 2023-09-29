---
name: Stack
description: Use Stack component to compose elements and components in a vertical flex container
endpoint: /components/stack
package: dash_mantine_components
---

.. toc::

### Simple Example

Adjust stack styles with `align`, `justify`, and `spacing` props.

.. exec::docs.stack.simple
    :code: true

### Introduction

```python
import dash_mantine_components as dmc

dmc.Stack(
    [
        dmc.Button("1", variant="outline"),
        dmc.Button("2", variant="outline"),
        dmc.Button("3", variant="outline"),
    ],
    style={"height": 200},
    align="stretch",
    justify="center",
)
```

.. exec::docs.stack.interactive
    :code: false

### Keyword Arguments

#### Stack

.. kwargs::Stack
