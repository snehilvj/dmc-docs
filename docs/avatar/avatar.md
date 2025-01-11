---
name: Avatar
description: Use Avatar to display user profile pictures. It supports images, icons, or letters. Use AvatarGroup to display stack Avatar components.
endpoint: /components/avatar
package: dash_mantine_components
category: Data Display
---

.. toc::

### Simple Usage

.. exec::docs.avatar.simple

### Initials
To display initials instead of the default placeholder, set name prop to the name of the person, for example,
`name='John Doe'`. If the name is set, you can use `color='initials'` to generate color based on the name:

.. exec::docs.avatar.initials

### Allowed initials colors
By default, all colors from the default theme are allowed for initials, you can restrict them by providing 
`allowedInitialsColors` prop with an array of colors. Note that the default colors array does not include custom
colors defined in the theme, you need to provide them manually if needed.

.. exec::docs.avatar.allowedinitialscolors

### Size, Radius and Variant

Control Avatar's height and width with `size` prop and border-radius with `radius` prop. Both props have
predefined values: xs, sm, md, lg, xl. Alternatively, a number can be used to set radius or size in px.

You can also use `variant` to style the Avatar.

```python
import dash_mantine_components as dmc

dmc.Avatar(src="/assets/avatar.jpeg", size="sm"),
dmc.Avatar(src="/assets/avatar.jpeg"),
dmc.Avatar(src="/assets/avatar.jpeg", size=50, radius="xl"),
dmc.Avatar(src="/assets/avatar.jpeg", size="xl", radius=20),
dmc.Avatar(src="/assets/avatar.jpeg", size="xl", variant="outline"),
```

.. exec::docs.avatar.interactive
    :code: false

### Avatar Group

Use AvatarGroup to stack Avatar components.

.. exec::docs.avatar.group

### Avatar link with tooltip

.. exec::docs.avatar.tooltip

### Dynamically created AvatarGroup

Here's an example of a dynamically created AvatarGroup from GitHub contributors to DMC library.

.. exec::docs.avatar.contributors

### Styles API

| Name            | Static selector                 | Description                                               |
|:----------------|:--------------------------------|:----------------------------------------------------------|
| root            | .mantine-Avatar-root            | Root element                                              |
| image           | .mantine-Avatar-image           | `img` element                                             |
| placeholder     | .mantine-Avatar-placeholder     | Placeholder element, rendered when image cannot be loaded |

### Keyword Arguments

#### Avatar

.. kwargs::Avatar

#### AvatarGroup

.. kwargs::AvatarGroup
