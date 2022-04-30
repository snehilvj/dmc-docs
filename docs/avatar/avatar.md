---
name: Avatar
section: Data Display
head: Display user profile image, initials or fallback icon.
description: Use Avatar to display user profile pictures. It supports images, icons, or letters.
component: Avatar
---

##### Simple Usage

Use Avatar to display user profile pictures. It supports images, icons, or letters.

.. exec::docs.avatar.simple

##### Size and Radius

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
    :prism: false

##### Gallery

.. gallery::docs.avatar.tooltip
    :label: Avatar link with tooltip
