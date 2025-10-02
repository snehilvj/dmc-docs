---
name: Inputs Overview
endpoint: /inputs-overview
description: This guide gives an overview of Input components available in Dash Mantine components.
package: dash_mantine_components
category: Inputs
order: 1  # sets order in navbar section
---

.. toc::
.. llms_copy::Inputs Overview

### Introduction to Mantine Inputs

Mantine Input components use a common base Input component giving all the inputs shared styles and features.  This helps
give your app a consistent design.

.. exec::docs.inputs-overview.inputs_demo
    :code: false


### Use props to add labels and more

Input components are made up of nested elements, so you can add things like labels, description, error message, icons and more with just a prop.
Here is an example of the TextInput component:


.. exec::docs.textinput.interactive
    :code: false

### Accessibility
All Mantine components, including inputs, are built with accessibility in mind, adhering to WAI-ARIA standards.
They provide features such as proper roles, ARIA attributes, semantic HTML, and full keyboard support out of the box,
simplifying the process of creating inclusive web apps.

### Checkbox


.. exec::docs.checkbox.simple
    :code: false


.. exec::docs.checkbox.indeterminate
    :code: false

### Chip


.. exec::docs.chip.states
    :code: false

### ColorInput

.. exec::docs.colorinput.simple
    :code: false

### ColorPicker


.. exec::docs.colorpicker.simple
    :code: false


.. exec::docs.colorpicker.picker
    :code: false

### Fieldset


.. exec::docs.fieldset.interactive
    :code: false

### InputWrapper

Use [InputWrapper](/components/inputwrapper) to add label, description and error fields to custom inputs.

### JsonInput
[JsonInput](/components/jsoninput) is based on `Textarea` component, it includes json validation logic and option to format input value on blur.


.. exec::docs.jsoninput.simple
    :code: false

### NumberInput


.. exec::docs.numberinput.prefix_suffix
    :code: false

### PasswordInput

.. exec::docs.passwordinput.icon
    :code: false

### PinInput


.. exec::docs.pininput.simple
    :code: false

### RadioGroup


.. exec::docs.radiogroup.callback
    :code: false

### Rating


.. exec::docs.rating.interactive
    :code: false

### RichTextEditor


.. exec::docs.richtexteditor.usage
    :code: false

### SegmentedControl

.. exec::docs.segmentedcontrol.simple
    :code: false

### Slider

.. exec::docs.slider.interactive
    :code: false

### RangeSlider


.. exec::docs.slider.range
    :code: false

### Switch


.. exec::docs.switch.overview
    :code: false
 :code: false

### TextInput


.. exec::docs.textinput.icon
    :code: false

### TextArea


.. exec::docs.textarea.autosize
    :code: false


### Dropdown (Select) components

See the Combobox section

- [Select](/comonents/select): Single selection from a predefined list.
- [MultiSelect](components/multiselect): Multiple selections from a predefined list.
- [Autocomplete](components/autocomplete): Free text input with suggestions.
- [TagsInput](components/tagsinput): Multiple value entry (tags) with free input and suggestions. 


### Date and Time components

See the Date Picker section