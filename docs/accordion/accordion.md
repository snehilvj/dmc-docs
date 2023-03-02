---
name: Accordion
section: Data Display
head: Divide content into collapsible sections.
description: Use the Accordion and AccordionX components to toggle between hiding and showing large amount of content.
component: Accordion, AccordionMultiple, AccordionControl, AccordionItem, AccordionPanel
styles: true
---

##### Interactive Demo

.. exec::docs.accordion.interactive
    :prism: false

##### Simple Example

This is a basic example showing how you can compose an accordion using dmc's Accordion and AccordionX components.  

.. exec::docs.accordion.simple

##### Customizing chevron

You can use [dash-iconify](/dash-iconify) to change the chevron icon.

.. exec::docs.accordion.chevron

##### With icons

You can customize icons in your accordion with `icon`, `iconSize` and `iconPosition` props.

.. exec::docs.accordion.icons

##### Callbacks and State Management

A `state` is associated with each Accordion component. Click on any section to see how it looks.

.. exec::docs.accordion.state

##### Multiple Items

Use dmc.AccordionMultiple to allow opening multiple items.

.. exec::docs.accordion.multiple

##### Custom Accordion Label

.. exec::docs.accordion.label

##### Styles API

.. exec::docs.accordion.styles
