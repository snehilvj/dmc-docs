---
name: Alert
description: Use Alerts to attract user attention with static messages.
endpoint: /components/alert
package: dash_mantine_components
---

.. toc::

### Introduction

.. exec::docs.alert.interactive
    :code: false

### Simple Example

Create an alert with the main message (`children`), the `title`, and the `color`.

.. exec::docs.alert.simple

### Different colors

Set the color using `color` argument.

.. exec::docs.alert.colors

### Dismissible Alerts

The alerts can be closed either programmatically by toggling the `hide` property or by clicking on the close button on the alert if enabled with `withCloseButton=True`.

.. exec::docs.alert.dismissible

### Automatic Dismissal

The alerts can also be timed out using the `duration` prop which accepts time in milliseconds.

.. exec::docs.alert.auto

### Styles API

| Name        | Static selector            | Description                                   |
|:------------|:---------------------------|:----------------------------------------------|
| root        | .mantine-Alert-root        | Root element                                  |
| wrapper     | .mantine-Alert-wrapper     | Wraps body and icon                           |
| body        | .mantine-Alert-body        | Body element, wraps title and message         |
| title       | .mantine-Alert-title       | Title element, contains label and icon        |
| label       | .mantine-Alert-label       | Title label                                   |
| message     | .mantine-Alert-message     | Alert message, defined by children            |
| icon        | .mantine-Alert-icon        | Icon wrapper                                  |
| closeButton | .mantine-Alert-closeButton | Close button, defined by withCloseButton prop |

### Keyword Arguments

#### Alert

.. kwargs::Alert
