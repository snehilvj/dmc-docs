---
name: TimeInput
section: Inputs
head: Capture time input from user.
description: Use the TimeInput component to capture time input from user.
component: TimeInput
styles: time-input
---

##### Simple Example

This is a simple example of the TimeInput. You can enter a valid time string or use the date object from datetime 
library.

Use the `format` prop to specify 12 or 24 hour display and the `withSeconds` prop to display seconds.

.. exec::docs.timeinput.simple

##### Input Props

TimeInput supports all props from Input and InputWrapper components such as `radius`, `size`, `required`, etc.

.. exec::docs.timeinput.input
    :prism: false

##### Invalid State And Error

You can display an error with a red border and add an error message.

.. exec::docs.timeinput.error
