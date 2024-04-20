---
name: LoadingOverlay
description: Use LoadingOverlay component to disable user interactions and indicate loading state.
endpoint: /components/loadingoverlay
package: dash_mantine_components
category: Feedback
---

.. toc::

### Simple Usage

`LoadingOverlay` renders an overlay with a loader over the parent element with relative position.
It is usually used to indicate loading state of forms.

`LoadingOverlay` rendering is controlled by `visible` prop:

.. exec::docs.loadingoverlay.simple

### Loader Props

.. exec::docs.loadingoverlay.customize

### Styles API

| Name    | Static selector                 | Description         |
|:--------|:--------------------------------|:--------------------|
| root    | .mantine-LoadingOverlay-root    | Root element        |
| overlay | .mantine-LoadingOverlay-overlay | `Overlay` component |
| loader  | .mantine-LoadingOverlay-loader  | `Loader` component  |

### Keyword Arguments

#### LoadingOverlay

.. kwargs::LoadingOverlay
