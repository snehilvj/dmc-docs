---
name: NumberInput
section: Inputs & Buttons
head: Capture number input from user.
description: Use NumberInput to provide a field for entering numbers in your app with ability to set min, max and step.
component: NumberInput
---

##### Simple Example

.. exec-block::docs.numberinput.simple

##### Increment/decrement on hold

Set `stepHoldDelay` and `stepHoldInterval` props to define behavior when increment/decrement controls are clicked and 
held.

.. exec-block::docs.numberinput.hold

##### Decimal steps

To use decimal steps set following props:
* `step` – decimal number, e.g. 0.05
* `precision` – amount of significant digits

.. exec-block::docs.numberinput.decimal

##### With Icon

You can use DashIconify to add icon to the NumberInput.

.. exec-block::docs.numberinput.icon
