---
name: Notification
description: dmc has an excellent Notifications System, which can be used to generate client side notifications.
endpoint: /components/notification
package: dash_mantine_components
---

.. toc::

.. admonition::Note
    :color: yellow
    :icon: radix-icons:info-circled
    In order to show notifications in your apps, you need to add dmc.Notifications() to your app layout.

### Simple Example

To enable the Notifications System, include the `dmc.Notifications()` component anywhere in your app layout. 

The `dmc.Notification` is not like your conventional dash components. They are more like "instructions" than components. 
In order to show notifications in your app, just send these instructions as children to any div in your callbacks.

.. exec::docs.notification.simple

### Customizing Notifications

Use Notifications to customize the positioning of your notification, auto close duration, etc.  In the example below, the
notification will display on the bottom left side of the screen rather than the default of bottom right.

```python
import dash_mantine_components as dmc

layout = dmc.MantineProvider(
    html.Div([
        dmc.Notifications(position="bottom-left"),
        # children
    ])
)
```

### Updating Notifications

Each notification is identified with an `id`. In order to update/hide a notification, use this `id` along with the 
`action` prop.

.. exec::docs.notification.update

### Styles API

| Name        | Static selector                   | Description                                               |
|:------------|:----------------------------------|:----------------------------------------------------------|
| root        | .mantine-Notification-root        | Root element                                              |
| body        | .mantine-Notification-body        | Notification body wrapper, contains title and description |
| loader      | .mantine-Notification-loader      | Notification loader, controlled by loading prop           |
| icon        | .mantine-Notification-icon        | Notification icon on the left, controlled by icon prop    |
| title       | .mantine-Notification-title       | Notification title, controlled by title prop              |
| description | .mantine-Notification-description | Notification description, controlled by children          |
| closeButton | .mantine-Notification-closeButton | Close button                                              |

### Keyword Arguments

#### Notifications

.. kwargs::Notifications

#### Notification

.. kwargs::Notification
