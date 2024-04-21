---
name: Migration Guide 0.12 to 0.14
endpoint: /migration
description: This page helps you migrate from an old version to a newer version of Dash Mantine Components
dmc: false
---

.. toc::

### Backstory

There are many breaking changes going from DMC `v0.12` to DMC `v0.14`. The major reason behind this was we jumped from 
underlying Mantine `v5` to Mantine `v7` and DMC tries to be as aligned with Mantine as possible. 

This hard alignment ensures that I can continue developing and maintaining this library alongside my day job. However, 
as per the author of Mantine itself, Mantine is reaching maturity and 
Mantine `v8` is supposed to introduce a lot of new features without the cost of API change.

I'd recommend going through the [getting started](/getting-started) page as well.

### MantineProvider

It is now mandatory to wrap your app into [MantineProvider](/components/mantineprovider) (of which only one can be there in the app).
This component is responsible for providing theme to all DMC components.

Dark theme is changed like this now:

  ```python
import dash_mantine_components as dmc

dmc.MantineProvider(
        forceColorScheme="dark",
        theme={...}
)
```

Mantine provides some better way to manage color themes in your app, but they are yet to be made available in DMC.

### React 18+ only

Starting with `v0.14`, DMC will need REACT 18. You can ensure that in two ways:

#### In the app settings

```python
import dash

# add this before creating app object
dash._dash_renderer._set_react_version('18.2.0')

app = Dash(__name__)
```

#### Environment variable

```bash
REACT_VERSION=18.2.0 python app.py
```

### Required StyleSheets

Except styling for core elements, the styling for components like `CodeHighlight`, `DatePicker`, `Carousel`, etc. have to be 
included by the user.

```python
from dash import Dash

# below covers all the stylesheets, you can pick as per your need.
stylesheets = [
    "https://unpkg.com/@mantine/dates@7/styles.css",
    "https://unpkg.com/@mantine/code-highlight@7/styles.css",
    "https://unpkg.com/@mantine/charts@7/styles.css",
    "https://unpkg.com/@mantine/carousel@7/styles.css",
    "https://unpkg.com/@mantine/notifications@7/styles.css",
    "https://unpkg.com/@mantine/nprogress@7/styles.css",
]

app = Dash(__name__, external_stylesheets=stylesheets)
```

### Missing components

- `Chip` and `ChipGroup` components are not working as expected when ported over in dash. It will be worked on as part of subsequent releases.
- `TransferList` is no longer available.

### left and right section

Components that previously had `rightSection` and `icon` props, now use `leftSection` instead of `icon`. Example of Button sections:

.. exec::docs.migration.button

### Progress

[Progress](/components/progress) component now supports compound components pattern. Advanced features that were previously implemented in Progress
are now supposed to be implemented with compound components instead.

.. exec::docs.progress.sections

.. admonition:: Tooltips
    :color: red
    :icon: radix-icons:info-circled

     Tooltips on Progress are not working as expected for now. Will have to tackle this in the subsequent releases.

### Table

[Table](/components/table) component changes:

- [Styles API](/styles-api) support
- It is now required to use `dmc` compound components instead of `html` table ones: `dmc.TableTr`, `dmc.TableTd`, etc.
- New props: `borderColor`, `withRowBorders`, `stripedColor`, `highlightOnHoverColor`
- `withBorder` prop was renamed to `withTableBorder`
- `fontSize` prop was removed, use `fz` [style prop](/style-props) instead

.. exec::docs.table.simple

### Group

[Group](/components/group) component changes:

- `position` prop was renamed to `justify` – it now supports all `justify-content` values
- `spacing` prop was renamed to `gap`

.. exec::docs.group.interactive
    :code: false

### Button

[Button](/components/button) changes

- `compact` prop was removed, use `size='compact-xx'` instead
- `leftIcon` and `rightIcon` props were renamed to `leftSection` and `rightSection`
- `uppercase` prop was removed, use `tt` [style prop](/style-props) instead
- `loaderPosition` prop was removed, Loader is now always rendered in the center to prevent layout shifts

### AppShell

[AppShell](/components/appshell) component is more feature rich now and has undergone following changes:

- `AppShell` now uses compound components pattern: `dmc.AppShellNavbar`, `dmc.AppShellAside`, `dmc.AppShellHeader`, `dmc.AppShellFooter`, and `dmc.AppShellMain`.
- `AppShell` now supports animations when navbar/aside are opened/closed
- `AppShell` no longer supports `fixed` prop – all components have `position: fixed` styles, static positioning is no longer supported

### SimpleGrid

[SimpleGrid](/components/simplegrid) now uses object format to define grid breakpoints and spacing, it works the same way as [style props](/style-props).

.. exec::docs.simplegrid.responsive

### Grid

[Grid](/components/grid) now uses object format in `gutter`, `offset`, `span` and `order` props, all props now work the same way as [style props](/style-props).

- `Col` component has been renamed to `GridCol`

### Image

[Image](/components/image) component changes:

- `caption` prop is no longer available 
- `width` and `height` props are replaced with `w` and `h` [style props](/style-props)
- Placeholder functionality was replaced with fallback image

.. exec::docs.image.placeholder

### Notification

`NotificationsProvider` has been renamed to `NotificationProvider`.

### Prism

`Prism` has been replaced by [CodeHighlight](/components/code-highlight).

### MediaQuery

MediaQuery has been removed. You can use CSS or `visibleFrom` and `hiddenFrom` props.

All DMC components now support `hiddenFrom` and `visibleFrom` props. These props accept breakpoint (`xs`, `sm`, `md`, `lg`, `xl`) 
and hide the component when viewport width is less than or greater than the specified breakpoint.

.. exec::docs.migration.hidden
