---
name: Modal
description: Use Modal component to show a dialog box or a popup window on the top of the current page.
endpoint: /components/modal
package: dash_mantine_components
---

.. toc::

### Simple Example

This is a basic example of dmc.Modal. You can also customize it by setting the desired `radius` or `padding`.

.. exec::docs.modal.simple

### Different Sizes

Set the size of the modal using the `size` prop.

.. exec::docs.modal.sizes

### Vertically Centered Modal

To vertically center the modal, set `centered=True`.

.. exec::docs.modal.vertical

### Modal With Overflow

You can control modal vertical overflow behavior by setting `overflow` prop.

.. exec::docs.modal.overflow

### Styles API

| Name    | Static selector        | Description                                                           |
|:--------|:-----------------------|:----------------------------------------------------------------------|
| root    | .mantine-Modal-root    | Root element                                                          |
| inner   | .mantine-Modal-inner   | Element used to center modal, has fixed position, takes entire screen |
| content | .mantine-Modal-content | Modal.Content root element                                            |
| header  | .mantine-Modal-header  | Contains title and close button                                       |
| overlay | .mantine-Modal-overlay | Overlay displayed under the Modal.Content                             |
| title   | .mantine-Modal-title   | Modal title (h2 tag), displayed in header                             |
| body    | .mantine-Modal-body    | Modal body, displayed after header                                    |
| close   | .mantine-Modal-close   | Close button                                                          |

### Keyword Arguments

#### Modal

.. kwargs::Modal
