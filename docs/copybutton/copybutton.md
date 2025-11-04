---
name: Copy Button
description: Copies given text to clipboard.  A DMC alternative to dcc.Clipboard.
endpoint: /components/copybutton
package: dash_mantine_components
category: Buttons
---

.. toc::
.. llms_copy::Copy Button

### Introduction

`CopyButton` is a ready-to-use clipboard button built with the Mantine `Button` component.
It supports props for dynamic text, icons and colors while copying plus all standard Button props.


.. exec::docs.copybutton.interactive
    :code: false



### Colors

Use `color` and `copiedColor` props to change the button’s appearance before and after copying.

.. exec::docs.copybutton.color

### Copy State Display 

Use `children` and `copiedChildren` to change what’s displayed before and after copying.  You can use text, icons, or any Dash components.

.. exec::docs.copybutton.children

### Copy from another component
Use `target_id` to copy text (or value prop) from another component instead of using a static value. No callback required!

.. exec::docs.copybutton.targetid

### Copy in a callback


Update the `value` and set `triggerCopy=True` in a callback to copy text programmatically. In this example, the `CopyButton` is hidden, and copying happens when a dropdown value changes.

.. exec::docs.copybutton.triggercopy

### Timeout

The `timeout` prop controls how long the "copied" state is displayed (in milliseconds). The default is 1000ms.


.. exec::docs.copybutton.timeout

### Custom Copy Button

Create a custom copy button using a JavaScript function. This example uses an `ActionIcon` and `Tooltip` that respond to the copied state.

.. functions_as_props::


.. exec::docs.copybutton.customcopy
    :code: false

.. sourcetabs::docs/copybutton/customcopy.py, assets/examples-js/custom_copy.js
    :defaultExpanded: true
    :withExpandedButton: true 



### Security
Due to security reasons `CopyButton` components will not work in iframes and may not work with local files opened with `file://` protocol.  

It will work with local websites using `http://` protocol, but when deployed it must use `https//` (secure).

Learn more about [navigator.clipboard](https://web.dev/articles/async-clipboard).


### Styles API

.. styles_api_text::

#### CopyButton Selectors

| Selector | Static selector          | Description                                        |
|----------|---------------------------|----------------------------------------------------|
| root     | .mantine-Button-root      | Root element                                       |
| loader   | .mantine-Button-loader    | Loader component, displayed only when `loading` prop is set |
| inner    | .mantine-Button-inner     | Contains all other elements, child of the root element |
| section  | .mantine-Button-section   | Left and right sections of the button             |
| label    | .mantine-Button-label     | Button children                                   |

#### CopyButton CSS Variables

| Selector | Variable                  | Description                                       |
|----------|---------------------------|---------------------------------------------------|
| root     | --button-bg               | Controls background                               |
|          | --button-bd               | Controls border                                   |
|          | --button-hover            | Controls background when hovered                 |
|          | --button-color            | Controls text color                               |
|          | --button-hover-color      | Controls text color when hovered                 |
|          | --button-radius           | Controls border-radius                            |
|          | --button-height           | Controls height of the button                     |
|          | --button-padding-x        | Controls horizontal padding of the button         |
|          | --button-fz               | Controls font-size of the button                  |
|          | --button-justify          | Controls `justify-content` of the inner element   |

#### CopyButton Data Attributes

| Selector       | Attribute             | Condition               | Value                           |
|----------------|------------------------|--------------------------|---------------------------------|
| root           | data-disabled          | `disabled` prop is set   | –                               |
| root, label    | data-loading           | `loading` prop is set    | –                               |
| root           | data-block             | `fullWidth` prop is set  | –                               |
| root           | data-with-left-section | `leftSection` is set     | –                               |
| root           | data-with-right-section| `rightSection` is set    | –                               |
| section        | data-position          | –                        | Section position: left or right |


### Keyword Arguments
.. style_props_text::

#### CopyButton

.. kwargs::CopyButton

#### CustomCopyButton

.. kwargs::CustomCopyButton
