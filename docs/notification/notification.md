---
name: Notification
description: dmc has an excellent Notifications System, which can be used to generate client side notifications.
endpoint: /components/notification
package: dash_mantine_components
---

.. toc::

### Note

Wrap your layout inside NotificationsProvider to be able to use Notifications in your dash apps. If you are using MantineProvider, then NotificationsProvider must be placed inside.
You can customize the positioning of your notifications, auto close duration, etc. through this component.

```python
import dash_mantine_components as dmc

layout = dmc.MantineProvider(
    dmc.NotificationsProvider([
        # children
    ])
)
```

.. admonition::Note
    :color: yellow
    :icon: radix-icons:info-circled
    In order to show notifications in your apps, you need to wrap your layout inside a NotificationsProvider.

### Simple Example

dmc.Notification is not like your conventional dash components. They are more like "instructions" than components. 
In order to show notifications in your app, just send these instructions as children to any div in your callbacks.

.. exec::docs.notification.simple

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

#### Notification

.. kwargs::Notification

#### NotificationsProvider

.. kwargs::NotificationsProvider
