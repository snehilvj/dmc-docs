---
name: Notification
section: Feedback
head: Show dynamic notifications and alerts to user, part of notifications system.
description: dmc has an excellent Notifications System, which can be used to generate client side notifications.
component: Notification
---

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

##### Caveats

If you are not using the `icon` prop in your Notification call, you may come across an issue where you are not able
to open a notification multiple times. This is a limitation currently. However, there's a very simple fix for it.

If you have a simple string in your `message` prop, just wrap it in a list.

```python
# instead of message = "This is a notification"
message = ["This is a notification"]
```

You can see the difference below:

.. exec::docs.notification.caveat
