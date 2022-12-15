---
name: Notification
section: Feedback
head: Show dynamic notifications and alerts to user, part of notifications system.
description: dmc has an excellent Notifications System, which can be used to generate client side notifications.
component: Notification, NotificationsProvider
props: false
---

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

##### Simple Example

dmc.Notification is not like your conventional dash components. They are more like "instructions" than components. 
In order to show notifications in your app, just send these instructions as children to any div in your callbacks.

.. exec::docs.notification.simple

##### Updating Notifications

Each notification is identified with an `id`. In order to update/hide a notification, use this `id` along with the 
`action` prop.

.. exec::docs.notification.update

