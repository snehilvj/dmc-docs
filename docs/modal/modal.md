---
name: Modal
description: Use Modal component to show a dialog box or a popup window on the top of the current page.
endpoint: /components/modal
package: dash_mantine_components
category: Overlay
---

.. toc::
.. llms_copy::Modal

### Simple Example

This is a basic example of dmc.Modal. You can also customize it by setting the desired `radius` or `padding`.

.. exec::docs.modal.simple

### Different Sizes

Set the size of the modal using the `size` prop.

.. exec::docs.modal.sizes

### Vertically Centered Modal

To vertically center the modal, set `centered=True`.

.. exec::docs.modal.vertical

### Modal With Scroll

.. exec::docs.modal.scroll

### Modal Stack

Use `ModalStack` component to render multiple modals at the same time. `ModalStack` keeps track of opened modals, 
manages `z-index` values, focus trapping and `closeOnEscape` behavior.

Differences from using multiple Modal components:

- `ModalStack` children must be `ManagedModal` components
- `ModalStack` manages `z-index` values – modals that are opened later will always have higher `z-index` value disregarding their order in the DOM
- `ModalStack` disables focus trap and `Escape` key handling for all modals except the one that is currently opened
- Modals that are not currently visible are present in the DOM but are hidden with `opacity: 0` and `pointer-events: none`
- Only one overlay is rendered at a time


.. exec::docs.modal.modalstack


### Styles API

.. styles_api_text::

| Name    | Static selector        | Description                                                           |
|:--------|:-----------------------|:----------------------------------------------------------------------|
| root    | .mantine-Modal-root    | Root element                                                          |
| inner   | .mantine-Modal-inner   | Element used to center modal, has fixed position, takes entire screen |
| content | .mantine-Modal-content | `Modal.Content` root element                                          |
| header  | .mantine-Modal-header  | Contains title and close button                                       |
| overlay | .mantine-Modal-overlay | Overlay displayed under the `Modal.Content`                           |
| title   | .mantine-Modal-title   | Modal title (h2 tag), displayed in the header                         |
| body    | .mantine-Modal-body    | Modal body, displayed after header                                    |
| close   | .mantine-Modal-close   | Close button                                                          |

### Keyword Arguments

#### Modal

.. kwargs::Modal


#### ModalStack

.. kwargs::ModalStack

#### ManagedModal

> Note:  ManagedModal is for use in the ModalStack component. id is required.  open/closed state is controlled by ModalStack.

.. kwargs::ManagedModal