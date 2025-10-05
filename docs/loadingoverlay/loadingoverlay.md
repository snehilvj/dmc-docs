---
name: LoadingOverlay
description: Use LoadingOverlay component to disable user interactions and indicate loading state.
endpoint: /components/loadingoverlay
package: dash_mantine_components
category: Feedback
---

.. toc::
.. llms_copy::LoadingOverlay

### Simple Usage

`LoadingOverlay` renders an overlay with a loader over the parent element with relative position.
It is usually used to indicate loading state of forms.

`LoadingOverlay` rendering is controlled by `visible` prop:

.. exec::docs.loadingoverlay.simple

### Loader Props

.. exec::docs.loadingoverlay.customize

### Custom LoadingOverlay

`loaderProps` (dict) - Supports a key of "variant" with values of oval, bars, dots or custom as in this example, also custom supports a children key as in this dmc.Image with a custom .gif loading screen.

.. exec::docs.loadingoverlay.customimageoverlay

### Styles API

.. styles_api_text::

| Name    | Static selector                 | Description         |
|:--------|:--------------------------------|:--------------------|
| root    | .mantine-LoadingOverlay-root    | Root element        |
| overlay | .mantine-LoadingOverlay-overlay | `Overlay` component |
| loader  | .mantine-LoadingOverlay-loader  | `Loader` component  |

### Keyword Arguments

#### LoadingOverlay

.. kwargs::LoadingOverlay


