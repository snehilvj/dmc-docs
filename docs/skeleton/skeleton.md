---
name: Skeleton
description: Use Skeleton component to disable user interactions and indicate loading state.
endpoint: /components/skeleton
package: dash_mantine_components
category: Feedback
---

.. toc::

### Simple Usage

Use `Skeleton` to create a placeholder for loading content. `Skeleton` support the following props:

- `height` - height - any valid CSS value
- `width` - width - any valid CSS value
- `radius` - key of `theme.radius` or any valid CSS value to set border-radius
- `circle` - if true, width, height and border-radius will equal to value specified in `height` prop
- `animate` - true by default, controls animation

.. exec::docs.skeleton.simple

### Customizing Loader

.. exec::docs.skeleton.graphs

### Styles API

| Name        | Static selector        | Description                                      |
|:------------|:-----------------------|:-------------------------------------------------|
| root        | .mantine-Skeleton-root | Root element                                     |

### Keyword Arguments

#### Skeleton

.. kwargs::Skeleton
