---
name: Notification
description: DMC has an excellent Notifications System, which can be used to generate client side notifications.
endpoint: /components/notification
package: dash_mantine_components
category: Feedback
---

.. toc::
.. llms_copy::Notification

### New NotificationContainer

As of DMC v2.0.0, notifications are handled by a single component:  `NotificationContainer`.

This replaces the previous `NotificationProvider`   +  `Notification` approach with one that is more aligned with 
Mantine's implementation.


### Getting Started

Add `NotificationContainer` to your layout:

```python
app.layout = dmc.MantineProvider([
    dmc.NotificationContainer(id="notification-container"),
    # other components...
])
```

* `NotificationContainer` must be placed inside a `MantineProvider`.
* You should have only one `NotificationContainer` in your app; multiple containers will cause notifications to be duplicated.
* In multi-page apps, place `NotificationContainer` in the top-level `app.layout`, not inside individual pages.
* It is no longer necessary to use a separate output container (such as `html.Div`) as in versions prior to 2.0.

### Migration Guide

The following components are deprecated and will be removed in a future release:

* `NotificationProvider`
* `Notification`

See the [Notification Migration Guide](/migration-notifications) for help updating your app.


### Show Notifications

To display a notification, use the `sendNotifications` prop on the `NotificationContainer`.
It accepts a list of dictionaries, where each dict represents a notification.

```python

dmc.NotificationContainer(
    id="notification-container",
    sendNotifications=[{
        "action": "show",
        "id": "my-id",
        "message": "This is a notification",
        # other props like title, color, icon, etc.
    }]
)
```

.. exec::docs.notification.show


### Update Notifications

To update notifications that were previously shown or queued, set `action="update"` and include the`id` of the notifications to update:

```python
sendNotifications = [{
    "action": "update",
    "id": "my-id",
    "message": "My updated notification message",
    # other props to update
}]
```

.. exec::docs.notification.update


### sendNotifications prop

Each dictionary in `sendNotifications` can include:

* `id` – notification ID used to update or remove notifications. A random ID is generated if not provided.
* `action` – one of `"show"`, or `"update"`
  
    * `"show"` – adds a new notification or queues it if the limit is reached
    * `"update"` – updates a notification previously shown or queued
* `message` – required notification body 
* `position` – notification position. If not provided, the default from `NotificationContainer` is used.
* `withBorder` – whether the notification should have a border
* `withCloseButton` – whether the close button is visible
* `autoClose` – timeout in milliseconds to automatically close the notification. Set to `False` to disable.
* `color` -Controls notification line or icon color, key of `theme.colors` or any valid CSS color, `theme.primaryColor` by default.
* `icon` - Notification icon, replaces color line.
* `title` - Notification title, displayed before body.
* `radius` -  Key of `theme.radius` or any valid CSS value to set `border-radius`, `theme.defaultRadius` by default
*  `loading`- Replaces colored line or icon with Loader component.
*  `className`, `style`, `loading`


### Notification Position
You can set position per-notification in the `sendNotifications` dictionary. 
```python
sendNotifications = [
  {
    "action": "show",
    "id": "my-id",
    "message": "Positioned top-left",
    "position": "top-left"
  }
]
```

Valid position values:

* `"top-left"`
* `"top-right"`
* `"top-center"`
* `"bottom-left"`
* `"bottom-right"`
* `"bottom-center"`

.. exec::docs.notification.position

You can also set a default position in the `NotificationContainer`. 

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

### Use in Clientside Callbacks

`NotificationContainer` exposes the underlying Mantine notifications API globally in JavaScript. You can access this
in clientside callbacks using:

```js
dash_mantine_components.appNotifications
```

You can use the the full [Mantine notifications API](https://mantine.dev/x/notifications/):

- Show: `appNotifications.api.show({...})`

- Update: `appNotifications.api.update({...})`

- Hide: `appNotifications.api.hide("id")`

- Clean: `appNotifications.api.clean()`

- Clean queue: `appNotifications.api.cleanQueue()`

- View state: `appNotifications.store`


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



#### Notification Selectors


| Selector    | Static Selector                     | Description                                            |
| ----------- | ----------------------------------- | ------------------------------------------------------ |
| root        | `.mantine-Notification-root`        | Root element                                           |
| loader      | `.mantine-Notification-loader`      | Loader component, displayed only when `loading` is set |
| icon        | `.mantine-Notification-icon`        | Icon component, displayed only when `icon` is set      |
| body        | `.mantine-Notification-body`        | Notification body, contains all other elements         |
| title       | `.mantine-Notification-title`       | Title element, displayed only when `title` is set      |
| description | `.mantine-Notification-description` | Description displayed below the title                  |
| closeButton | `.mantine-Notification-closeButton` | Close button element                                   |



#### Notification CSS Variables

| Selector | Variable                | Description                                    |
| -------- | ----------------------- | ---------------------------------------------- |
| root     | `--notification-radius` | Controls border-radius                         |
| root     | `--notification-color`  | Controls icon color or notification line color |



#### Notification Data Attributes

| Selector    | Attribute          | Condition                |
| ----------- | ------------------ | ------------------------ |
| root        | `data-with-icon`   | `icon` prop is set       |
| root        | `data-with-border` | `withBorder` prop is set |
| description | `data-with-title`  | `title` prop is set      |




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
