---
name: Progress
section: Feedback
head: Give user feedback for status of the task.
description: Use the Progress component to give feedback to the user about the status of a task with label, sections, etc.
component: Progress
---

##### Interactive Demo

.. exec::docs.progress.interactive
    :prism: false

##### Simple Example

Progress component has one required prop: `value` - filled bar width in %. You can change bar color by passing `color`
prop (by default theme.primaryColor will be used).

.. exec::docs.progress.simple

##### Multiple sections

Multiple sections can be displayed instead of just one single bar.

.. exec::docs.progress.sections

##### With Label

Labels can be provided for single bars as well as different sections.

.. exec::docs.progress.labels

##### Section Tooltips

Hover on the sections to see tooltips in action.

.. exec::docs.progress.tooltip

##### Size

Size controls progress bar height. Progress has predefined sizes: xs, sm, etc. Alternatively, you can use a number to
set height in px.

```python
import dash_mantine_components as dmc

dmc.Progress(size="sm")

dmc.Progress(size=20)
```

##### Radius

Radius controls border-radius of body and filled part.

```python
import dash_mantine_components as dmc

dmc.Progress(radius="lg")

dmc.Progress(radius=10)
```
