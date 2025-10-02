---
name: debounce prop
endpoint: /debounce
description:  Learn how to use the debounce prop in Dash Mantine Components to control when input values update. Reduce callback load and improve performance in text inputs, dropdowns, pickers, and more.
category: Dash
---


.. toc::
.. llms_copy::debounce prop


### About the debounce prop


The `debounce` prop delays the update of a component's value until the user stops interacting, reducing callback
frequency for inputs.


To control how often the input's value is updated while the user is typing, use the `debounce` prop:

- `debounce=False` Is the default and it will update as the user interacts with the input.
- Set `debounce=True` to update the value only when the user finishes typing and moves focus away (i.e. on blur).
- Set `debounce=<milliseconds>` to update the value after a specified delay from the user's last keystroke. For example,
`debounce=300` will wait 300 milliseconds after the user stops typing before updating the value.


####  debounce=False
.. exec::docs.timepicker.simple


####  debounce=True
.. exec::docs.timepicker.debounce

#### debounce=1000
.. exec::docs.timepicker.debouncems


### Example with TextInput

This example uses `debounce=True`.  Note that the comments are updated only after the user has
finished entering data.

.. exec::docs.dashprops.debounce-textinput

### Supported Components
The `debounce` prop is supported by many DMC input components, including:

- TextInput

- Textarea

- NumberInput

- PasswordInput

- JsonInput

- Select, MultiSelect, Autocomplete

- DateInput, DateTimePicker, DatePickerInput

- MonthPickerInput, YearPickerInput, TimeInput, TimePicker

- RichTextEditor


For the `Slider` and `RangeSlider`  use [updatemode](/components/slider#update-mode)

### Usage Tips

- Use `debounce=True` for forms where you only care about the final value after the user finishes typing, for example, email fields, names, comments.

- Use `debounce=300` or higher for search boxes or filters that trigger live updates (for example,  querying a table or filtering a plot). This prevents the app from firing a callback on every keystroke and keeps things responsive.

- Combine with `n_submit` or `n_blur` if you want finer control over when inputs send updates.

