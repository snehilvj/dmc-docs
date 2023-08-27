---
name: Spoiler
description: Use the Spoiler component to hide long sections of content.
endpoint: /components/spoiler
package: dash_mantine_components
---

.. toc::

### Simple Example

Use Spoiler to hide long sections of content. Pass `maxHeight` prop to control the point at which content will be
hidden under the spoiler and control to show/hide extra appears. If content height is less than `maxHeight`, spoiler
will just render children.

Props `hideLabel` and `showLabel` are required - they are used as spoiler toggle button label in corresponding state.

.. exec::docs.spoiler.simple

### Styles API

| Name    | Static selector          | Description       |
|:--------|:-------------------------|:------------------|
| root    | .mantine-Spoiler-root    | Root element      |
| content | .mantine-Spoiler-content | Content wrapper   |
| control | .mantine-Spoiler-control | Hide/show control |

### Keyword Arguments

#### Spoiler

.. kwargs::Spoiler
