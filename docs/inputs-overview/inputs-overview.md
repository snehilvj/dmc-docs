---
name: Inputs Overview
endpoint: /inputs-overview
description: This guide gives an overview of Input components available in Dash Mantine components.
package: dash_mantine_components
category: Inputs
order: 1  # sets order in navbar section
---

.. toc::

### Introduction to Mantine Inputs

Mantine Input components use a common base Input component giving all the inputs shared styles and features.  This helps
give your app a consistent design in your app.

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