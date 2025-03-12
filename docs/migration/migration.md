---
name: Migration Guide
endpoint: /migration
description: This page helps you migrate from an old version to a newer version of Dash Mantine Components
dmc: false
---

.. toc::


## Version Compatibility  

Below is a list of Dash Mantine Components (DMC) versions, their corresponding Mantine versions, and required Dash versions:  

| Dash Mantine Components | Release Date | Mantine Version | Required Dash Version |
|----------------------|--------------|-----------------|----|
| **1.0.0**           | Mar 2025     | 7.17.0          | `dash>=2.0.0` |
| **0.15.0**          | Nov 2024     | 7.14.1          | `dash>=2.0.0,<3.0.0`|
| **0.14.0**          | Apr 2024     | 7.0             | `dash>=2.0.0,<3.0.0` |
| **0.13.0a1**        | Aug 2023     | 6.0             | `dash>=2.0.0,<3.0.0` |
| **0.12.0**          | Mar 2023     | 5.10.5          | `dash>=2.0.0,<3.0.0` |



## Migrating from 0.15 to 1.0.0

This release ensures dash-mantine-components V1 is fully compatible with both Dash 2 and Dash 3.
**If you are using dash-mantine-components<1.0.0rc1 you must  pin your dash version to < 3.0.0**

### Breaking Change: Carousel Props
The `draggable` and `speed` props have been removed from `Carousel` as they are no longer supported in Embla Carousel V8.
These props were functional until DMC 0.14.7, when Embla was upgraded to V8.



## Migrating from 0.14 to 0.15

The `DatePicker` component has been renamed to `DatePickerInput` to align with the component names of  the upstream
Mantine Library.  We plan to add the Mantine [`DatePicker`](https://mantine.dev/dates/date-picker/) component in a future release.

We still expect far fewer breaking changes going forward compared to what you may have experienced in the past. For more details, please see our [Roadmap](https://github.com/snehilvj/dash-mantine-components/discussions/377).


## Migrating from 0.12 to 0.14

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
import dash_mantine_components as dmc

# below covers all the stylesheets, you can pick as per your need.
stylesheets = [
    dmc.styles.DATES,
    dmc.styles.CODE_HIGHLIGHT,
    dmc.styles.CHARTS,
    dmc.styles.CAROUSEL,
    dmc.styles.NOTIFICATIONS,
    dmc.styles.NPROGRESS,
]

app = Dash(__name__, external_stylesheets=stylesheets)
```
Or, include all the stylesheets like this:

```python
app = Dash(__name__, external_stylesheets=dmc.styles.ALL)
```

### Missing components

- `Chip` and `ChipGroup` components are not working as expected when ported over in dash. It will be worked on as part of subsequent releases.
- `TransferList` is no longer available. You might benefit from [AIO based TransferList component](https://community.plotly.com/t/dash-mantine-components-0-14-1/83865/18?u=snehilvj) created by a community member.
**update** `Chip` and `ChipGroup` are available as of 0.14.6

### Creatable option in Select and MultiSelect

`creatable` prop has been removed from `Select` and `MultiSelect`. However, [TagsInput](/components/tagsinput) can be used to emulate
the same functionality as `MultiSelect` with `creatable` prop.

### Left and Right section

Components that previously had `rightSection` and `icon` props, now use `leftSection` instead of `icon`. Example of Button sections:

.. exec::docs.migration.button

### Title

[Title](/components/title) doesn't accept other [Text](/components/text) props like gradient etc. anymore.

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
`disallowClose` is no longer available.  Use `withCloseButton`

### Prism

`Prism` has been replaced by [CodeHighlight](/components/code-highlight).

### MediaQuery

MediaQuery has been removed. You can use CSS or `visibleFrom` and `hiddenFrom` props.

All DMC components now support `hiddenFrom` and `visibleFrom` props. These props accept breakpoint (`xs`, `sm`, `md`, `lg`, `xl`) 
and hide the component when viewport width is less than or greater than the specified breakpoint.

.. exec::docs.migration.hidden
