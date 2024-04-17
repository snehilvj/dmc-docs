---
name: Notification
description: dmc has an excellent Notifications System, which can be used to generate client side notifications.
endpoint: /components/notification
package: dash_mantine_components
---

.. toc::

.. admonition::Note
    :color: red
    :icon: radix-icons:info-circled
    In order to show notifications in your apps, you need to add dmc.NotificationProvider() to your app layout.

### Simple Example

To enable the Notifications System, include the `dmc.NotificationProvider()` component anywhere in your app layout. 

The `dmc.Notification` is not like your conventional dash components. They are more like "instructions" than components. 
In order to show notifications in your app, just send these instructions as children to any div in your callbacks.

.. exec::docs.notification.simple

### Customizing Notifications

Use NotificationProvider to customize the positioning of your notification, auto close duration, etc.  In the example below, the
notification will display on the bottom left side of the screen rather than the default of bottom right.

```python
import dash_mantine_components as dmc

layout = dmc.MantineProvider(
    html.Div([
        dmc.NotificationProvider(position="bottom-left"),
        # children
    ])
)
```

### Updating Notifications

Each notification is identified with an `id`. In order to update/hide a notification, use this `id` along with the 
`action` prop.

.. exec::docs.notification.update

### Styles API

| Name        | Static selector                   | Description                                                |
|:------------|:----------------------------------|:-----------------------------------------------------------|
| root        | .mantine-Notification-root        | Root element                                               |
| loader      | .mantine-Notification-loader      | Loader component, displayed only when `loading`prop is set |
| icon        | .mantine-Notification-icon        | Icon component, displayed only when `icon` prop is set     |
| body        | .mantine-Notification-body        | Notification body, contains all other elements             |
| title       | .mantine-Notification-title       | Title element, displayed only when `title` prop is set     |
| description | .mantine-Notification-description | Description displayed below the title                      |
| closeButton | .mantine-Notification-closeButton | Close button element                                       |

### Keyword Arguments

#### Notifications

.. kwargs::NotificationProvider

#### Notification

.. kwargs::Notification
