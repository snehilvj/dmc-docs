---
name: Notification
description: DMC has an excellent Notifications System, which can be used to generate client side notifications.
endpoint: /components/notification
package: dash_mantine_components
category: Feedback
---

.. toc::

### New NotificationContainer

Starting in `dash-mantine-components` v2.0.0, notifications are now handled through a single, simplified component: `NotificationContainer`.

This replaces the previous `NotificationProvider` and `Notification` pattern with a more powerful approach that is more closely
aligned with the Mantine's implementation.

Add `NotificationContainer` to your layout (it must be placed inside a `MantineProvider`):

```python
app.layout = dmc.MantineProvider([
    dmc.NotificationContainer(id="notification-container"),
    # other components...
])
```

### Migration Notice

The following components are deprecated and will be removed in a future release:

* `NotificationProvider`
* `Notification`

See the [Notification Migration Guide](/migration-notifications) for help updating your app.

### Usage notes

* `NotificationContainer` must be placed inside a `MantineProvider`.
* You should have only one `NotificationContainer` in your app; multiple containers will cause notifications to be duplicated.
* In multi-page apps, place `NotificationContainer` in the top-level `app.layout`, not inside individual pages.
* It is no longer necessary to use a separate output container (such as `html.Div`) as in versions prior to 2.0.

### Show Notifications

Use the `sendNotifications` prop on `NotificationContainer` to show or update notifications.

To display a notification, add a dictionary with `"action": "show"` to the `sendNotifications` list:

```python
sendNotifications = [{
    "action": "show",
    "id": "my-id",
    "message": "My notification message",
    # other props
}]
```

.. exec::docs.notification.show


### sendNotifications

Use the `sendNotifications` prop on `NotificationContainer` to show or  update  notifications.

`sendNotifications` is a list of dictionaries. Each dictionary represents a single notification with the following properties:

* `id` – notification ID used to update or remove notifications. A random ID is generated if not provided.
* `action` – one of `"show"`, or `"update"`
  
    * `"show"` – adds a new notification or queues it if the limit is reached
    * `"update"` – updates a notification previously shown or queued
 
* `position` – notification position. If not provided, the default from `NotificationContainer` is used.
* `withBorder` – whether the notification should have a border
* `withCloseButton` – whether the close button is visible
* `onClose` – callback triggered when the notification is unmounted
* `autoClose` – timeout in milliseconds to automatically close the notification. Set to `False` to disable.
* `message` – required notification body
* `color`, `icon`, `title`, `radius`, `className`, `style`, `loading`


### Update Notifications

To update notifications that were previously shown or queued, set `"action": "update"` and include the`id` of the notifications to update:

```python
sendNotifications = [{
    "action": "update",
    "id": "my-id",
    "message": "My updated notification message",
    # other props to update
}]
```

.. exec::docs.notification.update

### Notification Position

You can set the notification position in the `sendNotifications` dictionary. Valid values:

* `"top-left"`
* `"top-right"`
* `"top-center"`
* `"bottom-left"`
* `"bottom-right"`
* `"bottom-center"`

.. exec::docs.notification.position

You can also set a default position in the `NotificationContainer`. For example, if `position` is not set in the
`sendNotifications` dict, the following layout will display notifications in the top right corner:

```python
app.layout = dmc.MantineProvider([
    dmc.NotificationContainer(position="top-right", id="notification-container"),
])
```

### Limit and queue

To limit the number of notifications displayed at once, use the `limit` prop:

```python
dmc.NotificationContainer(limit=5)
```

Notifications beyond the limit are added to the queue and shown when others are dismissed.

.. exec::docs.notification.queue

### Hide Notifications

Use the `hideNotifications` prop to remove notifications by `id` from the state and queue.

.. exec::docs.notification.hide

### clean and cleanQueue

Use `cleanQueue` to remove all queued notifications, and `clean` to remove all notifications from both state and queue.

.. exec::docs.notification.clean

### autoClose

.. exec::docs.notification.autoclose

### Accessing Notifications API

`NotificationContainer` exposes the underlying Mantine notifications API globally in JavaScript. You can access this
in clientside callbacks using:

```js
dash_mantine_components.appNotifications
```

This object provides:

* `appNotifications.api` – the full [Mantine notifications API](https://mantine.dev/x/notifications/):

  * `.show({...})`
  * `.update({...})`
  * `.hide(id)`
  * `.clean()`
  * `.cleanQueue()`
* `appNotifications.store` – returns the current state of all active and queued notifications

The example below demonstrates how to:

* Show a notification from a clientside callback
* Display the notification store in a `html.Pre` component
* Clean all notifications on the client

.. exec::docs.notification.api

### Notifications in Multi Page apps

In multi-page apps, define `NotificationContainer` in `app.layout`—even if notifications are triggered from other pages.

This ensures the container is always mounted and available, preventing errors when navigating between pages while notifications are active.

### CSS Extensions


As of DMC 1.2.0, Notification component styles are bundled automatically, so you no longer need to include a separate CSS file.
If you're using an older version of DMC, refer to the [migration guide](/migration) for instructions on including optional stylesheets.


### Styles API

.. styles_api_text::

#### Notifications Selectors
| Selector      | Static Selector                         | Description                                      |
|--------------|--------------------------------------|--------------------------------------------------|
| `root`       | `.mantine-Notifications-root`      | Notifications container, contains all notifications |
| `notification` | `.mantine-Notifications-notification` | Single notification |

#### Notifications CSS Variables
| Selector | Variable | Description |
|----------|----------|-------------|
| `root`   | `--notifications-container-width` | Controls notifications container max-width |
| `root`   | `--notifications-z-index` | Controls notifications container z-index |


### Keyword Arguments

#### NotificationContainer

.. kwargs::NotificationContainer
