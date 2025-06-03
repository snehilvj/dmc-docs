---
name: TimePicker
description: Use the TimeInput component to capture time input from user.
endpoint: /components/timepicker
package: dash_mantine_components
category: Date Pickers
---

.. toc::

### Usage

`TimePicker` component is an alternative to [TimeInput](/components/timeinput) that offers more features, it supports 
24-hour and 12-hour formats, dropdown with hours, minutes and seconds, and more.

.. exec::docs.timepicker.simple

### With callbacks

`TimePicker` component value is a string in hh:mm:ss 24-hour format (for example 18:34:55). Empty string is used to
represent no value. The `value` props is updated when the entered value is valid. The input value is considered valid
in the following cases:

- All inputs are empty. In this case the `value` will be  an empty string.
- All inputs are filled. For example if `withSeconds` prop is set and the user entered 12:34:56, the value will be
12:34:56. But if the user entered 12:34, `value` will not be updated because seconds value is missing.
- If a complete, valid time has been entered, the value will update as the user changes any part of it (hours, minutes,
or seconds). Each digit change will immediately reflect in the updated value.

### Debounce

To control how often the input's value is updated while the user is typing, use the `debounce` prop:

- Set `debounce=True` to update the value only when the user finishes typing and moves focus away (i.e. on blur).
- Set `debounce=<milliseconds>` to update the value after a specified delay from the user's last keystroke. For example,
`debounce=300` will wait 300 milliseconds after the user stops typing before updating the value.

#### Example debounce=True
.. exec::docs.timepicker.debounce

#### Example debounce=1000
.. exec::docs.timepicker.debouncems


### With seconds
Set `withSeconds` prop to enable seconds input. Note that if this prop is used, the value is not updated until all
inputs are filled – it is not possible to enter only hours and minutes.

.. exec::docs.timepicker.withseconds

### 12-hour format
Set `format="12h"` to use 12-hour format. Note that `value` is updated only when all inputs are filled including am/pm input.


.. exec::docs.timepicker.format

### Change am/pm labels
To change am/pm labels use `amPmLabels` prop. Example of changing labels to Hindi:


.. exec::docs.timepicker.ampmlabels

### Min and max values
Set `min` and `max` props to limit available time range:

.. exec::docs.timepicker.minmax

### With dropdown
Set `withDropdown` prop to display the dropdown with hours, minutes, seconds and am/pm selects. By default,
the dropdown is visible when one of the inputs is focused.

.. exec::docs.timepicker.withdropdown

### Hours/minutes/seconds step
Use `hoursStep`, `minutesStep` and `secondsStep` props to control step for each input. These props are used to control
value by which the input is incremented or decremented when up/down arrow keys are pressed and to generate corresponding
values range in the dropdown.

.. exec::docs.timepicker.step

### Time presets
You can define time presets with `presets` prop. Presets are displayed in the dropdown and can be selected by clicking
on them. Time values for presets should be in hh:mm:ss or hh:mm 24-hour time format. Presets display value is generated
based on `format`, `amPmLabels` and `withSeconds` props.


.. exec::docs.timepicker.presets

### Time presets groups
To group presets use a list of dictionaries with label and values keys:


.. exec::docs.timepicker.presetsgroup

### Time presets range
Use the `timeRangePresets` prop to generate a range of times. It accepts a dictionary with `startTime`,
`endTime`, and `interval` keys, where all values are strings in `hh:mm:ss` format. This overrides any values provided 
directly in the `presets` prop.

.. exec::docs.timepicker.presetsrange


### Dropdown position
By default, the dropdown is displayed below the input if there is enough space; otherwise it is displayed above the 
input. You can change this behavior by setting `position` and `middlewares` props, which are passed down to the
underlying `Popover` component.

Example of dropdown that is always displayed above the input:


.. exec::docs.timepicker.dropdownposition

### Dropdown width
To change dropdown width, set `width` prop in `popoverProps`. By default, dropdown width is adjusted to fit all content.
Example of dropdown width set to the input width:

.. exec::docs.timepicker.dropdownwidth

### Clearable
Set `clearable` prop to display a clear button in the right section of the input. The clear button is visible when at
least one of the fields has value.


.. exec::docs.timepicker.clearable

### Disabled

.. exec::docs.timepicker.disabled


### Read only

.. exec::docs.timepicker.readonly

### Input Props

TimeInput supports all props from Input and InputWrapper components such as `radius`, `size`, `required`, etc.

.. exec::docs.timepicker.interactive
    :code: false

### Invalid State And Error

You can display an error with a red border and add an error message.

.. exec::docs.timepicker.error

### Accessibility

Set aria labels for hours, minutes, seconds and am/pm inputs and clear button with corresponding props:
```python
    dmc.TimePicker(
      hoursInputLabel="Hours",
      minutesInputLabel="Minutes",
      secondsInputLabel="Seconds",
      amPmInputLabel="AM/PM",
      clearButtonProps={{ 'aria-label': 'Clear time' }}
    
  )
```

### Keyboard Interactions


| Key          | Description                              |
| ------------ | ---------------------------------------- |
| `ArrowDown`  | Decrements current value by step         |
| `ArrowUp`    | Increments current value by step         |
| `Home`       | Sets current value to min possible value |
| `End`        | Sets current value to max possible value |
| `Backspace`  | Clears current value                     |
| `ArrowRight` | Moves focus to the next input            |
| `ArrowLeft`  | Moves focus to the previous input        |



### Styles API

.. styles_api_text::     


#### TimePicker Selectors

| Selector          | Static selector                         | Description                                                       |
| ----------------- | --------------------------------------- | ----------------------------------------------------------------- |
| wrapper           | `.mantine-TimePicker-wrapper`           | Root element of the Input                                         |
| input             | `.mantine-TimePicker-input`             | Input element                                                     |
| section           | `.mantine-TimePicker-section`           | Left and right sections                                           |
| root              | `.mantine-TimePicker-root`              | Root element                                                      |
| label             | `.mantine-TimePicker-label`             | Label element                                                     |
| required          | `.mantine-TimePicker-required`          | Required asterisk element, rendered inside label                  |
| description       | `.mantine-TimePicker-description`       | Description element                                               |
| error             | `.mantine-TimePicker-error`             | Error element                                                     |
| control           | `.mantine-TimePicker-control`           | Button in the dropdown used to select hours/minutes/seconds/am-pm |
| controlsList      | `.mantine-TimePicker-controlsList`      | List of buttons for hours/minutes/seconds/am-pm                   |
| controlsListGroup | `.mantine-TimePicker-controlsListGroup` | Group of `controlsList`s                                          |
| dropdown          | `.mantine-TimePicker-dropdown`          | Popover dropdown                                                  |
| fieldsRoot        | `.mantine-TimePicker-fieldsRoot`        | Wrapper for all `fieldsGroup` elements                            |
| fieldsGroup       | `.mantine-TimePicker-fieldsGroup`       | Wrapper for hours/minutes/seconds/am-pm fields                    |
| field             | `.mantine-TimePicker-field`             | Hours/minutes/seconds/am-pm input field                           |
| presetControl     | `.mantine-TimePicker-presetControl`     | Time preset button                                                |
| presetsGroup      | `.mantine-TimePicker-presetsGroup`      | Wraps preset controls and label                                   |
| presetsGroupLabel | `.mantine-TimePicker-presetsGroupLabel` | Label of the preset group                                         |
| presetsRoot       | `.mantine-TimePicker-presetsRoot`       | Wrapper for all presets content                                   |
| scrollarea        | `.mantine-TimePicker-scrollarea`        | Scroll area in the dropdown                                       |


#### TimePicker CSS Variables

| Selector | Variable              | Description                             |
| -------- | --------------------- | --------------------------------------- |
| dropdown | `--control-font-size` | Controls font-size of dropdown controls |


### Keyword Arguments

#### TimePicker

.. kwargs::TimePicker
