---
name: Alert
section: Feedback
head: Attract user attention with important static message.
description: Use Alerts to attract user attention with static messages.
component: Alert
---

##### Interactive Demo

.. exec-block::docs.alert.interactive
    :prism: false

##### Simple Example

Create an alert with the main message (`children`), the `title`, and the `color`.

.. exec-block::docs.alert.simple

##### Different colors

Set the color using `color` argument.

.. exec-block::docs.alert.colors

##### Dismissible Alerts

The alerts can be closed either programmatically by toggling the `hide` property or by clicking on the close button on the alert if enabled with `withCloseButton=True`.

.. exec-block::docs.alert.dismissible

##### Automatic Dismissal

The alerts can also be timed out using the `duration` prop which accepts time in milliseconds.

.. exec-block::docs.alert.auto
