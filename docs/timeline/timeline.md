---
name: Timeline
description: Use the Timeline and TimelineItem components to display a list of events in chronological order.
endpoint: /components/timeline
package: dash_mantine_components
category: Data Display
---

.. toc::
.. llms_copy::Timeline

### Introduction

.. exec::docs.timeline.interactive
    :code: false

### Usage

Control timeline appearance with the following props:

- `active` - index of current active element, all elements before this index will be highlighted with color
- `color` - color from theme that should be used to highlight active items, defaults to theme.primaryColor
- `lineWidth` - controls line width and bullet border
- `bulletSize` - bullet width, height and border-radius
- `align` - defines line and bullets position relative to content, also sets textAlign

.. exec::docs.timeline.simple


### Components in Bullets

.. exec::docs.timeline.bullets



    
### Styles API

.. styles_api_text::

#### Timeline Selectors

| Selector     | Static selector               | Description                               |
|-------------|-------------------------------|-------------------------------------------|
| root        | .mantine-Timeline-root        | Root element                             |
| item        | .mantine-Timeline-item        | Item root element                        |
| itemBody    | .mantine-Timeline-itemBody    | Item body, wraps title and content       |
| itemTitle   | .mantine-Timeline-itemTitle   | Item title, controlled by `title` prop   |
| itemContent | .mantine-Timeline-itemContent | Item content, controlled by `children` prop |
| itemBullet  | .mantine-Timeline-itemBullet  | Item bullet                              |

#### Timeline CSS Variables

| Selector | Variable          | Description                                 |
|----------|------------------|---------------------------------------------|
| root     | --tl-bullet-size | Controls bullet width and height           |
|          | --tl-color       | Controls active bullet and line colors     |
|          | --tl-icon-color  | Controls icon color                        |
|          | --tl-line-width  | Controls width of the line between bullets |
|          | --tl-radius      | Controls bullet border-radius              |

#### Timeline Data Attributes

| Selector        | Attribute       | Condition                                    |
|----------------|----------------|----------------------------------------------|
| item, itemBullet | data-active    | Item index is `<=` Timeline `active` prop   |
| item           | data-line-active | Item index is `<` Timeline `active` prop    |

### Keyword Arguments

#### Timeline

.. kwargs::Timeline

#### TimelineItem

.. kwargs::TimelineItem
