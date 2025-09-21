---
name: Migration Guide
endpoint: /migration
description: This page helps you migrate from an old version to a newer version of Dash Mantine Components
category: Releases
order: 500
---

.. toc::


### Version Compatibility  

Below is a list of Dash Mantine Components (DMC) versions, their corresponding Mantine versions, and required Dash versions.

| Dash Mantine Components | Release Date | Mantine Version | Required Dash Version |
|-------------------------|--------------|-----------------|----|
| **2.3.0**               | Sep 2025     | 8.3.1           | `dash>=2.0.0` |
| **2.2.1**               | Aug 2025     | 8.2.7           | `dash>=2.0.0` |
| **2.2.0**               | Aug 2025     | 8.2.5           | `dash>=2.0.0` |
| **2.1.0**               | Jul 2025     | 8.1.2           | `dash>=2.0.0` |
| **2.0.0**               | Jun 2025     | 8.0.2           | `dash>=2.0.0` |
| **1.3.0**               | May 2025     | 7.17.7          | `dash>=2.0.0` |
| **1.2.0**               | Apr 2025     | 7.17.4          | `dash>=2.0.0` |
| **1.1.0**               | Mar 2025     | 7.17.2          | `dash>=2.0.0` |
| **1.0.0**               | Mar 2025     | 7.17.0          | `dash>=2.0.0` |
| **0.15.0**              | Nov 2024     | 7.14.1          | `dash>=2.0.0,<3.0.0`|
| **0.14.0**              | Apr 2024     | 7.0             | `dash>=2.0.0,<3.0.0` |
| **0.13.0a1**            | Aug 2023     | 6.0             | `dash>=2.0.0,<3.0.0` |
| **0.12.0**              | Mar 2023     | 5.10.5          | `dash>=2.0.0,<3.0.0` |


### Migrating from 1.2.0 to 2.x

DMC V2 is based on Mantine V8.  For more information see the [Mantine 8 Changelog.](https://mantine.dev/changelog/8-0-0/)
and the [DMC 2.0.0 Release announcement.]( /release-2-0-0)

Starting with DMC v2.3.0,` RichTextEditor` uses Tiptap v3. There are no known breaking changes, but projects with
customizations—such as clientside callbacks that rely on the Tiptap API or custom controls—should check for compatibility.
The Text Style API has also been updated, which may affect how JSON and HTML content are generated. For details on
changes and new features, see the [Tiptap v3 changelog](https://tiptap.dev/docs/resources/whats-new).


#### Switch withThumbIndicator

[Switch](/components/switch) component default styles were updated, it now includes checked state indicator inside the
thumb. If you want to use old styles without indicator, set `withThumbIndicator` prop to false in theme:

```python
dmc.MantineProvider(    
    theme={
        "components": {
            "Switch": {
                "defaultProps": {
                    # ✅ Disable withThumbIndicator if you want to use old styles
                    "withThumbIndicator": False,                  
                },
            },
        },
    }
)
```
#### DatesProvider timezone
DatesProvider component no longer supports timezone option:

```python
dmc.DatesProvider(
    # children= ...
    # ❌ timezone option is no longer supported
    setting={"timezone": 'UTC', "consistentWeeks": True}
)
```



#### DateTimePicker timeInputProps
`DateTimePicker` component no longer accepts `timeInputProps` prop, as the underlying `TimeInput` component was
replaced with `TimePicker`. To pass props down to `TimePicker` component, use `timePickerProps` prop instead.

1.x
```python
dmc.DateTimePicker(
    # ❌ timeInputProps is no longer available
      timeInputProps={
        "leftSection": dashIconify(icon="bi:clock"),
      }
)
```

2.x
```python
dmc.DateTimePicker(
    #   ✅ Use timePickerProps instead of timeInputProps
      timePickerProps={
        "leftSection": dashIconify(icon="bi:clock"),
         "minutesStep": 5,
        "withDropdown": True,
      }
)
```

#### CodeHighlight usage

To reduce the bundle size and increase performance,  only the top 10 languages from highlight.js are available.  See [CodeHighlight](/components/code-highlight)
for more details.  If you would like additional languages, please open an issue on our [GitHub](https://github.com/snehilvj/dash-mantine-components/issues)


#### Popover hideDetached
`Popover` now supports `hideDetached` prop to automatically close popover when target element is removed from the DOM.
Please see the example in the [Popover docs](/components/popover)

By default, `hideDetached` is enabled – the behavior has changed from 1.x version. If you prefer to keep the old
behavior, you can disable `hideDetached` for all components:


```python
dmc.MantineProvider(    
    theme={
        "components": {
            "Popover": {
                "defaultProps": {
                    #  ✅ Disable hideDetached by default if you want to keep the old behavior
                    "hideDetached": False,                  
                },
            },
        },
    }
)
```

#### Carousel changes

Update embla props that were previously passed to `Carousel` component to `emblaOptions`. Full list of props:

- `loop`
- `align`
- `slidesToScroll`
- `dragFree`
- `inViewThreshold`
- `skipSnaps`
- `containScroll`
- `speed` and `draggable` props were removed – they are no longer supported by embla

```python
#  ❌ 1.x – embla options passed as props no longer works in 2.x
dmc.Carousel(loop=True,  dragFree=True,  align="start")

# ✅ 2.x – use emblaOptions to pass options to embla
dmc.Carousel({ "loop": True, "dragFree": True, "align": 'start' })
```


#### Image No longer has `flex:0` as a default style

```python
  # ✅ Add back flex:0 style if needed
dmc.Image(src=logo, h=40, flex=0)

```

####  New DatePicker

A new `DatePicker` component has been added — this is a standalone calendar (no input field), matching Mantine's upstream
component.

Note that in v0.15.0, the original `DatePicker` was renamed to `DatePickerInput` to align with Mantine’s naming.

If you are migrating from DMC < 0.15.0 and your app used `dmc.DatePicker` update it to use `dmc.DatePickerInput`

#### New NotificationContainer component

Notifications are now handled by a single component: `NotificationContainer`. This replaces the previous
`NotificationProvider` + `Notification` approach with one that is more aligned with Mantine's implementation. Also, there is
now direct access to Mantine's  Notification API in clientside callbacks. 

Please see the new [Notification docs](/components/notification) for more details.

The `NotificationProvider` and `Notification` components are now deprecated and will be removed in a future major release.
Please see the [Notification Migration Guide](/migration-notifications) for a step-by-step guild for updating your apps.



#### Portal reuseTargetNode
`reuseTargetNode` prop of `Portal` component is now enabled by default. This option improves performance by reusing the
target node between portal renders, but in some edge cases, it might cause issues with z-index stacking context.

For more information see the [Mantine Portal documentation.](https://mantine.dev/core/portal/)

If you experience issues with z-index, change `reuseTargetNode` prop to `False` in `theme`:


```python
dmc.MantineProvider(    
    theme={
        "components": {
            "Portal": {
                "defaultProps": {
                    # ✅ Disable reuseTargetNode by default if your application has z-index issues
                    "reuseTargetNode": False,                  
                },
            },
        },
    }
)
```


#### Menu data-hovered attribute
`MenuItem` no longer uses `data-hovered` attribute to indicate hovered state. If you used `data-hovered` in your styles,
you need to change it `:hover` and `:focus` selectors instead:

.css files:
```css
// ❌ 7.x – styles with `data-hovered`,
// no longer works in 8.x
.item {
  &[data-hovered] {
    background-color: red;
  }
}

// ✅ 8.x – use styles with `:hover` and `:focus`
.item {
  &:hover,
  &:focus {
    background-color: red;
  }
}
```


### Stylesheets Are Now Included Automatically (DMC ≥ 1.2.0)

As of `dash-mantine-components >= 1.2.0`, you no longer need to manually include optional stylesheets for components like `DatePicker`, `Carousel`, `CodeHighlight`, or `RichTextEditor`.

These styles are now bundled automatically — making setup faster and simpler.

#### Still using an older version?

If you're working with **DMC < 1.2.0**, you may need to manually include stylesheets like this:

```python
import dash_mantine_components as dmc
from dash import Dash

app = Dash(
    external_stylesheets=[
        dmc.styles.CAROUSEL,
        dmc.styles.CODE_HIGHLIGHT,
        dmc.styles.NOTIFICATIONS,
        # or just use dmc.styles.ALL
    ]
)
```

You can also inspect any style path directly:

```python
print(dmc.styles.CODE_HIGHLIGHT)
# → https://unpkg.com/@mantine/code-highlight@7.x.x/styles.css
```



### Migrating from 0.15 to 1.0.0

This release ensures dash-mantine-components V1 is fully compatible with both Dash 2 and Dash 3.
**If you are using dash-mantine-components<1.0.0 you must  pin your dash version to < 3.0.0**

#### Breaking Change: Carousel Props
The `draggable` and `speed` props have been removed from `Carousel` as they are no longer supported in Embla Carousel V8.
These props were functional until DMC 0.14.7, when Embla was upgraded to V8.

#### React 18 
Dash 3.0 now uses react 18 by default.  If your app uses dash>=3.0 it is no longer necessary to set the React version:
```python
import dash
# not needed with dash>=3.0
dash._dash_renderer._set_react_version("18.2.0")
```

### Migrating from 0.14 to 0.15

The `DatePicker` component has been renamed to `DatePickerInput` to align with the component names of  the upstream
Mantine Library.  We plan to add the Mantine [`DatePicker`](https://mantine.dev/dates/date-picker/) component in a future release.

We still expect far fewer breaking changes going forward compared to what you may have experienced in the past. For more details, please see our [Roadmap](https://github.com/snehilvj/dash-mantine-components/discussions/377).


### Migrating from 0.12 to 0.14

#### Backstory

There are many breaking changes going from DMC `v0.12` to DMC `v0.14`. The major reason behind this was we jumped from 
underlying Mantine `v5` to Mantine `v7` and DMC tries to be as aligned with Mantine as possible. 

It's helpful to also refer to the upstream docs as well for a description of breaking changes:
  - [Mantine V7.0](https://mantine.dev/changelog/7-0-0/)
  - [Mantine V6.0](https://v6.mantine.dev/changelog/6-0-0/)

This hard alignment ensures that I can continue developing and maintaining this library alongside my day job. However, 
as per the author of Mantine itself, Mantine is reaching maturity and 
Mantine `v8` is supposed to introduce a lot of new features without the cost of API change.

I'd recommend going through the [getting started](/getting-started) page as well.

#### MantineProvider

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

#### React 18+ only

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

#### Required StyleSheets

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
app = Dash(external_stylesheets=dmc.styles.ALL)
```

#### Missing components

- `Chip` and `ChipGroup` components are not working as expected when ported over in dash. It will be worked on as part of subsequent releases.
- `TransferList` is no longer available. You might benefit from [AIO based TransferList component](https://community.plotly.com/t/dash-mantine-components-0-14-1/83865/18?u=snehilvj) created by a community member.
**update** `Chip` and `ChipGroup` are available as of 0.14.6

#### Creatable option in Select and MultiSelect

`creatable` prop has been removed from `Select` and `MultiSelect`. However, [TagsInput](/components/tagsinput) can be used to emulate
the same functionality as `MultiSelect` with `creatable` prop.

#### Left and Right section

Components that previously had `rightSection` and `icon` props, now use `leftSection` instead of `icon`. Example of Button sections:

.. exec::docs.migration.button

#### Title

[Title](/components/title) doesn't accept other [Text](/components/text) props like gradient etc. anymore.

#### Progress

[Progress](/components/progress) component now supports compound components pattern. Advanced features that were previously implemented in Progress
are now supposed to be implemented with compound components instead.

.. exec::docs.progress.sections

.. admonition:: Tooltips
    :color: red
    :icon: radix-icons:info-circled

     Tooltips on Progress are not working as expected for now. Will have to tackle this in the subsequent releases.

#### Table

[Table](/components/table) component changes:

- [Styles API](/styles-api) support
- It is now required to use `dmc` compound components instead of `html` table ones: `dmc.TableTr`, `dmc.TableTd`, etc.
- New props: `borderColor`, `withRowBorders`, `stripedColor`, `highlightOnHoverColor`
- `withBorder` prop was renamed to `withTableBorder`
- `fontSize` prop was removed, use `fz` [style prop](/style-props) instead

.. exec::docs.table.simple

#### Group

[Group](/components/group) component changes:

- `position` prop was renamed to `justify` – it now supports all `justify-content` values
- `spacing` prop was renamed to `gap`

.. exec::docs.group.interactive
    :code: false

#### Button

[Button](/components/button) changes

- `compact` prop was removed, use `size='compact-xx'` instead
- `leftIcon` and `rightIcon` props were renamed to `leftSection` and `rightSection`
- `uppercase` prop was removed, use `tt` [style prop](/style-props) instead
- `loaderPosition` prop was removed, Loader is now always rendered in the center to prevent layout shifts

#### AppShell (renamed Navbar, Aside, Header, Footer, Main)

[AppShell](/components/appshell) component is more feature rich now and has undergone following changes:

- `AppShell` now uses compound components pattern: `dmc.AppShellNavbar`, `dmc.AppShellAside`, `dmc.AppShellHeader`, `dmc.AppShellFooter`, and `dmc.AppShellMain`.
- `AppShell` now supports animations when navbar/aside are opened/closed
- `AppShell` no longer supports `fixed` prop – all components have `position: fixed` styles, static positioning is no longer supported

#### SimpleGrid

[SimpleGrid](/components/simplegrid) now uses object format to define grid breakpoints and spacing, it works the same way as [style props](/style-props).

.. exec::docs.simplegrid.responsive

#### Grid

[Grid](/components/grid) now uses object format in `gutter`, `offset`, `span` and `order` props, all props now work the same way as [style props](/style-props).

- `Col` component has been renamed to `GridCol`

#### Image

[Image](/components/image) component changes:

- `caption` prop is no longer available 
- `width` and `height` props are replaced with `w` and `h` [style props](/style-props)
- Placeholder functionality was replaced with fallback image

.. exec::docs.image.placeholder

#### Notification

`NotificationsProvider` has been renamed to `NotificationProvider`.
`disallowClose` is no longer available.  Use `withCloseButton`

#### Prism

`Prism` has been replaced by [CodeHighlight](/components/code-highlight).

#### MediaQuery

MediaQuery has been removed. You can use CSS or `visibleFrom` and `hiddenFrom` props.

All DMC components now support `hiddenFrom` and `visibleFrom` props. These props accept breakpoint (`xs`, `sm`, `md`, `lg`, `xl`) 
and hide the component when viewport width is less than or greater than the specified breakpoint.

.. exec::docs.migration.hidden
