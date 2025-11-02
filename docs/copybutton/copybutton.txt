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

`CopyButton` is a ready-to-use copy button built with the Mantine Button component. It supports props for dynamic text,
icons and colors while copying plus standard Button props (size, radius, variant, etc.).

### color and copiedColor
Use the `color` and `copiedColor` props to change the button appearance based on the copied state.

```python
dmc.CopyButton(
    value="https://www.dash-mantine-components.com/",
    children="Copy URL",
    color="blue",
    copiedColor="teal"
)
```

- `color`: The button color in its default state (before copying)
- `copiedColor`: The button color after the text has been copied to the clipboard
- If `copiedColor` is not provided, the button will keep the same color after copying

### children and copiedChildren
Use `children` and `copiedChildren` to display different content based on the copied state. This is useful for changing
text, icons, or any other components.

#### Text Example
```python
dmc.CopyButton(
    value="https://mantine.dev",
    children="Copy URL",
    copiedChildren="Copied!",
    color="blue",
    copiedColor="teal"
)
```
#### Icon Example
```python
from dash_iconify import DashIconify

dmc.CopyButton(
    value="https://mantine.dev",
    children=DashIconify(icon="tabler:clipboard"),
    copiedChildren=DashIconify(icon="tabler:check"),
    color="blue",
    copiedColor="teal"
)
```

- `children`: Content displayed before copying (can be text, icons, or any components)
- `copiedChildren`: Content displayed after copying to clipboard
- If `copiedChildren` is not provided, the same `children` will be displayed after copying

## Target ID

Use `target_id` to copy text (or value prop) from another component instead of using a static `value`. This is useful when you want to copy dynamic content from the page.

```python
import dash_mantine_components as dmc
from dash import html

html.Div([
    dmc.Text("This is the text that will be copied", id="text-to-copy"),
    dmc.CopyButton(
        target_id="text-to-copy",
        children="Copy Text",
        copiedChildren="Copied!",
        color="blue",
        copiedColor="teal"
    )
])
```

## triggerCopy

Use `triggerCopy` in callbacks to programmatically copy text to the clipboard without user interaction.

```python
import dash_mantine_components as dmc
from dash import Dash, Input, Output, callback

app = Dash(__name__)

app.layout = dmc.MantineProvider([
    dmc.Button("Trigger Copy", id="trigger-btn", n_clicks=0),
    dmc.CopyButton(
        id="copy-btn",
        value="Programmatically copied!",
        children="Copy",
        copiedChildren="Copied!",
        triggerCopy=False
    )
])

@callback(
    Output("copy-btn", "triggerCopy"),
    Input("trigger-btn", "n_clicks"),
    prevent_initial_call=True
)
def trigger_copy(n):
    return True

if __name__ == "__main__":
    app.run(debug=True)
```

### Updating Value and Triggering Copy

You can update the `value` and trigger the copy in the same callback:

```python
@callback(
    Output("copy-btn", "value"),
    Output("copy-btn", "triggerCopy"),
    Input("some-input", "value"),
    prevent_initial_call=True
)
def update_and_copy(input_value):
    return input_value, True
```

## Timeout

The `timeout` prop controls how long the "copied" state is displayed (in milliseconds).

```python
dmc.CopyButton(
    value="https://mantine.dev",
    children="Copy URL",
    copiedChildren="Copied!",
    color="blue",
    copiedColor="teal",
    timeout=2000  # Show "Copied!" for 2 seconds
)
```

- Default: `1000`ms
- After the timeout expires, the button returns to its default state (showing `children` and `color`)
- Use a longer timeout if you want users to see the confirmation for more time
- Use a shorter timeout for a quicker transition back to the default state


### Security
Due to security reasons `CopyButton` components will not work in iframes and may not work with local files opened with `file://` protocol.
It will work fine with local websites that are using `http://` protocol, but when deployed it must use `https//`

Learn more about [navigator.clipboard](https://web.dev/articles/async-clipboard).

Timeout
You can provide a custom copied reset timeout:

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
