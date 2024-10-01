---
name: Progress
description: Use the Progress component to give feedback to the user about the status of a task with label, sections, etc.
endpoint: /components/progress
package: dash_mantine_components
category: Feedback
---

.. toc::

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


### Limitations - Tooltips

There is a limitation in Dash that makes it challenging to style the width of some tooltip children. For more details, see [GitHub #319.](https://github.com/snehilvj/dash-mantine-components/issues/319)

Tooltip children are wrapped in a `Box` with a default style of `{'width': 'fit-content'}`, which may override the width defined in the children. To work around this, you can set the width using `boxWrapperProps`.

`boxWrapperProps` is a dictionary of style properties passed to the `Box` that wraps the tooltip children.

#### With Tooltip

In this example, the width of the `ProgressSection` is set to 100%, and the width of each section is defined using the `boxWrapperProps`.


.. exec::docs.progress.tooltip

#### With FloatingTooltip

Another even better workaround is to use `FloatingTooltips`.  In this case, set `boxWrapperProps={'display': 'contents'}`


.. exec::docs.progress.floatingtooltip


### Styles API

| Name    | Static selector           | Description                     |
|:--------|:--------------------------|:--------------------------------|
| root    | .mantine-Progress-root    | Root element                    |
| section | .mantine-Progress-section | `Progress.Section` root element |
| label   | .mantine-Progress-label   | `Progress.Label` root element   |

### Keyword Arguments

#### Progress

.. kwargs::Progress
