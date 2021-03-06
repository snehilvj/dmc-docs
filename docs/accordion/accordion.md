---
name: Accordion
section: Data Display
head: Divide content into collapsible sections.
description: Use the Accordion and AccordionItem components to toggle between hiding and showing large amount of content.
component: Accordion
---

##### Interactive Demo

.. exec::docs.accordion.interactive
    :prism: false

##### Simple Example

This is a basic example showing how you can use accordion. You can also pass a `description` along with the `label`.

.. exec::docs.accordion.simple

##### Customizing Icons

You can customize icons in your accordion with `icon`, `iconSize` and `iconPosition` props.

.. exec::docs.accordion.default

##### Callbacks and State Management

A `state` is associated with each Accordion component. Click on any section to see how it looks.

.. exec::docs.accordion.state

##### Multiple Items

Pass `multiple=True` flag to allow opening multiple items.

.. exec::docs.accordion.multiple

##### Gallery

.. gallery::docs.accordion.icons
    :center: false
    :label: Customizing accordion with icons
