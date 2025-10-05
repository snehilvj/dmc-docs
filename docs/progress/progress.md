---
name: Progress
description: Use the Progress component to give feedback to the user about the status of a task with label, sections, etc.
endpoint: /components/progress
package: dash_mantine_components
category: Feedback
---

.. toc::
.. llms_copy::Progress

### Introduction

.. exec::docs.progress.interactive
    :code: false

### Simple Example

Progress component has one required prop: `value` - filled bar width in %. You can change bar color by passing `color`
prop (by default theme.primaryColor will be used).

.. exec::docs.progress.simple

### Size

`size` controls progress bar height. Progress has predefined sizes: xs, sm, etc.
Alternatively, you can use a number to set height in px.

```python
import dash_mantine_components as dmc

dmc.Progress(size="sm")

dmc.Progress(size=20)
```

### Radius

Radius controls border-radius of body and filled part.

```python
import dash_mantine_components as dmc

dmc.Progress(radius="lg")

dmc.Progress(radius=10)
```

### Multiple sections

Multiple sections can be displayed instead of just one single bar.

.. exec::docs.progress.sections


### Vertical orientation

.. exec::docs.progress.orientation


### With Tooltip

Use the [Tooltip target](/components/tooltip#target) prop rather than using `ProgressSection` as Tooltip children.


.. exec::docs.progress.tooltip

### With FloatingTooltip

When using `FloatingTooltips`  set `boxWrapperProps={'display': 'contents'}` for best results:

.. exec::docs.progress.floatingtooltip


### Styles API

.. styles_api_text::

#### Progress selectors

| Selector | Static selector | Description |
|----------|----------------|-------------|
| root | `.mantine-Progress-root` | Root element |
| section | `.mantine-Progress-section` | `Progress.Section` root element |
| label | `.mantine-Progress-label` | `Progress.Label` root element |

#### Progress CSS variables

| Selector | Variable | Description |
|----------|----------|-------------|
| root | `--progress-radius` | Controls `border-radius` of track and sections |
| root | `--progress-size` | Controls height of progress bar |
| root | `--progress-transition-duration` | Controls width `transition-duration` of progress bar |

#### Progress data attributes

| Selector | Attribute | Condition |
|----------|-----------|-----------|
| section | `data-striped` | `striped` or `animated` props are set |
| section | `data-animated` | `animated` prop is set |


### Keyword Arguments

#### Progress

.. kwargs::Progress
