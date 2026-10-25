---
name: Marquee
description: Create continuous scrolling animation for content
endpoint: /components/marquee
package: dash_mantine_components
category: Miscellaneous
---

.. toc::
.. llms_copy::Marquee

### Usage

`Marquee` component creates a continuous scrolling animation for its children.
It is commonly used for displaying logos, testimonials, or any repeating content.

Set a width on the Marquee children to ensure smooth scrolling when the content repeats.

.. exec::docs.marquee.usage

### Pause on hover

Set `pauseOnHover` prop to pause the animation when the user hovers over the component:


.. exec::docs.marquee.pauseonhover


### Vertical orientation

Set `orientation="vertical"` to scroll content vertically. Note that you need to set
a fixed height on the container for vertical scrolling:


.. exec::docs.marquee.vertical

### Multiple rows

You can combine multiple `Marquee` components with different directions to create
more complex layouts:


.. exec::docs.marquee.multiplerows


### Fade edges

By default, `Marquee` displays gradient fade on edges to create a smooth transition effect.
You can customize the fade using the following props:

* `fadeEdges` – enables/disables fade gradient (default: `true`)
* `fadeEdgeColor` – color of the fade gradient (default: `var(--mantine-color-body)`)
* `fadeEdgeSize` – size of the fade area (default: `5%`)


.. exec::docs.marquee.fade

### Customization

Use the following props to customize the marquee behavior:

* `reverse` – reverses animation direction
* `repeat` – number of times children are repeated (default: 4)
* `duration` – animation duration in ms (default: 100000)
* `gap` – gap between repeated children, key of `theme.spacing` or any valid CSS value


.. exec::docs.marquee.interactive
    :code: false


### Styles API

.. styles_api_text::


#### Marquee selectors

| Selector | Static selector | Description |
|----------|----------------|-------------|
| root | .mantine-Marquee-root | Root element |
| content | .mantine-Marquee-content | Animated scrolling container |
| group | .mantine-Marquee-group | Repeated children wrapper |

#### Marquee CSS variables

| Selector | Variable | Description |
|----------|----------|-------------|
| root | --marquee-duration | Controls animation duration |
| root | --marquee-gap | Controls gap between items |
| root | --marquee-repeat | Number of times content is repeated |
| root | --marquee-fade-color | Controls the fade edge gradient color |
| root | --marquee-fade-size | Controls the size of the fade gradient |

#### Marquee data attributes

| Selector | Attribute | Condition | Value |
|----------|-----------|-----------|-------|
| root | data-orientation | Value depends on `orientation` prop | horizontal \| vertical |
| root | data-reverse | `reverse` prop is set | - |
| root | data-pause-on-hover | `pauseOnHover` prop is set | - |
| root | data-fade-edges | `fadeEdges` prop is `true` (default) | - |


### Keyword Arguments
.. style_props_text::

#### Marquee

.. kwargs::Marquee





