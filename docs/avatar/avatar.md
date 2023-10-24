---
name: Avatar
description: Use Avatar to display user profile pictures. It supports images, icons, or letters. Use AvatarGroup to display stack Avatar components.
endpoint: /components/avatar
package: dash_mantine_components
---

.. toc::

### Simple Usage

.. exec::docs.avatar.simple

### Size and Radius

Control Avatar's height and width with `size` prop and border-radius with `radius` prop. Both props have
predefined values: xs, sm, md, lg, xl. Alternatively, a number can be used to set radius or size in px.

```python
import dash_mantine_components as dmc

dmc.Avatar(src="/assets/avatar.jpeg", size="sm"),
dmc.Avatar(src="/assets/avatar.jpeg"),
dmc.Avatar(src="/assets/avatar.jpeg", size=50, radius="xl"),
dmc.Avatar(src="/assets/avatar.jpeg", size="xl", radius=20),
```

.. exec::docs.avatar.interactive
    :code: false

### AvatarGroup

Use AvatarGroup to stack Avatar components.

.. exec::docs.avatar.group

### Avatar link with tooltip

.. exec::docs.avatar.tooltip

### Dynamically created AvatarGroup

Here's an example of a dynamically created AvatarGroup from github contributors to dmc library.

.. exec::docs.avatar.contributors

### Styles API

| Name            | Static selector                 | Description                                                              |
|:----------------|:--------------------------------|:-------------------------------------------------------------------------|
| root            | .mantine-Avatar-root            | Root element                                                             |
| image           | .mantine-Avatar-image           | Main img tag, rendered when src is set to valid image url                |
| placeholder     | .mantine-Avatar-placeholder     | Placeholder element, rendered when src is null or image cannot be loaded |
| placeholderIcon | .mantine-Avatar-placeholderIcon | Default placeholder icon                                                 |

### Keyword Arguments

#### Avatar

.. kwargs::Avatar

#### AvatarGroup

.. kwargs::AvatarGroup
