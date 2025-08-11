---
name: Layout Overview
endpoint: /layout-overview
description: This guide gives an overview of layout components available in Dash Mantine components.
package: dash_mantine_components
category: Layout
order: 1  # sets order in navbar section
---

.. toc::


### Grid
Use [Grid](/components/grid) if you need columns with different sizes. The `span` prop also accepts a dictionary to change column width based on viewport width.

.. exec::docs.grid.simple
    :code: false


### SimpleGrid
Use [SimpleGrid](/components/simplegrid) if you need columns with equal size. The `cols`, `spacing` and `verticalSpacing` props accepts dictionaries to set responsive values based on viewport width.


.. exec::docs.simplegrid.simple
    :code: false


### Group
Use [Group](/components/group) if you want to put several items next to each other horizontally.

.. exec::docs.group.interactive
    :code: false

### Stack
Use [Stack](/components/stack) if you want to put several items next to each other vertically


.. exec::docs.stack.interactive
    :code: false

### Flex
Use [Flex](/components/flex) if you want to create both horizontal and vertical flexbox layouts. It's more flexible than `Group` and `Stack` but requires more configuration.


.. exec::docs.flex.interactive
    :code: false


### AspectRatio
Use [AspectRatio](/components/aspectratio) to ensure that content always maintains a specific width-to-height ratio,
no matter the screen size.  Great for images and videos.


### Center
Use [Center](/compnents/center) component to center content vertically and horizontally.
This example centers an icon with a link with the `inline` prop:


.. exec::docs.center.inline
    :code: false

### Container
Use [Container](/components/container) to center content horizontally and add horizontal padding from theme. Good for limiting width and centering content on large screens.


###  Box
[Box](/components/box) is like an `html.Div` but also includes Mantine style props.


### Paper

Use [Paper](/components/paper) to group content visually like a card.  It includes props for background, padding, shadow, borders, and rounded corners.


### AppShell

The [AppShell](/components/appshell) component is a layout component designed to create responsive and consistent app layouts.
It includes:
- `AppShell` - root component, it is required to wrap all other components, used to configure layout properties
- `AppShellHeader` - section rendered at the top of the page
- `AppShellNavbar` - section rendered on the left side of the page
- `AppShellAside` - section rendered on the right side of the page
- `AppShellFooter` - section rendered at the bottom of the page
- `AppShellMain` - main section rendered at the center of the page, has static position, all other sections are offset by its padding
- `AppShellSection` - utility component that can be used to render group of content inside `AppShellNavbar` and `AppShellAside`

This DMC documentation app is built using `AppShell` components.

See the [AppShell](/components/appshell) docs for more info and examples:

.. image::/assets/appshell.png
    :w: 600px



