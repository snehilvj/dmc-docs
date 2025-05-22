---
name: Notification
description: DMC has an excellent Notifications System, which can be used to generate client side notifications.
endpoint: /components/notification
package: dash_mantine_components
category: Feedback
---

.. toc::


Add `NotificationContainer()` component in your application. Note that:

- It is required to place `NotificationContainer` component inside `MantineProvider`
- You do not need to wrap your application with `NotificationNotification()` component – it is a regular component
- You should not have multiple `NotificationContainer()` components – if you do that, your notifications will be duplicated
- In a multi page app, the `NotificationContainer()` should be in the main `app.layout`
- It is unnecessary to have a separate output container like in DMC < 2.0

```python

app.layout = dmc.MantineProvider(
    [
        dmc.NotificationContainer(id="notification-container"),
        # other
        
    ]
)

```



### sendNotifications

Use the `sendNotifications` prop in the `NotificationContainer` to show, hide or update the notification component.

`sendNotifications` is a list of dictionaries with the following properties:

- `id` – notification id, it is used to update and remove notifications, by default id is randomly generated
- `action`-  One of "show", "hide", or "update"
- `position` – notification position, by default the value from the position prop of the Notifications component is used
- `withBorder` – determines whether notification should have a border
- `withCloseButton` – determines whether the close button should be visible
- `onClose` – calls when notification is unmounted
- `autoClose` – defines timeout in ms on which notification will be automatically closed, use false to disable auto close
- `message` – required notification body
- `color`, `icon`, `title`, `radius`, `className`, `style`, `loading`

The "action" prop in the `sendNotifications` dict can be "show", "hide" or "update"

- `show` – adds given notification to the notifications list or queue, depending on the current state and limit
- `hide` – removes notification with given id from the notifications state and queue
- `update` – updates notification that was previously added to the state or queue


#### Show Notifications
To display a notification, add an item to the `sendNotifications` list with `"action": "show"`.

Each item in the list is a dictionary describing a single notification:

```python
sendNotifications = [{
    "action": "show",
    "id": "my-id",
    "message":  "My notification message",
    # other props
}]
```

.. exec::docs.notification.show


#### Update Notifications

To update a notifications that were previously shown or queued, set `"action": "update"` and include the same id used earlier.
```python
sendNotifications = [{
    "action": "update",
    "id": "my-id",
    "message":  "My updated notification message",
    # other props to update
}]
```

.. exec::docs.notification.update



### Notification Position

You can define notification position in `sendNotification` dictionary. Possible position values:

- "top-left"
- "top-right"
- "top-center"
- "bottom-left" 
- "bottom-right"
- "bottom-center"

.. exec::docs.notification.position


The default position can be defined on the `NotificationContainer` component. In the following example, notifications will be
displayed in the top right corner of the screen if position is not defined in the `senddNotifications` prop in the callback:



```python

app.layout = dmc.MantineProvider(
    [
        dmc.NotificationContainer(position="top-right", id="notification-container"),
     
    ]
)

```

### Limit and queue
You can limit maximum number of notifications that are displayed at a time by setting limit prop on `NotificationContainer`:

```python
 dmc.NotificationContainer(limit=5),
```
All notifications added after the limit was reached are added to the queue and displayed when notification from current state is hidden.


.. exec::docs.notification.queue


### Hide Notifications

use `hideNotifications` to specify a list of notification ids to remove from the  state and queue.

.. exec::docs.notification.hide


### clean and cleanQueue

Use `cleanQueue` to  remove all notifications from the queue and `clean` to remove all notifications both from the state and queue:


.. exec::docs.notification.clean


### autoClose



.. exec::docs.notification.autoclose

###  Accessing Notifications API

The `NotificationsContainer` exposes the underlying Mantine notifications API directly to JavaScript. This makes it
easy to control notifications in Dash clientside callbacks.

You can access the API via:

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
* `appNotifications.store` – returns the current state of all notifications (active + queued)



The example below demonstrates how to:

* Show a notification from a clientside callback
* Display the notification store into a Dash `html.Pre` component
* Clean all notifications from the client

.. exec::docs.notification.api


### Notifications in Multi Page apps

When using notifications in a multi-page app, ensure that `NotificationContainer` is defined in `app.layout`—even if
the notification is triggered from a different page.  

By keeping the notification container in `app.layout`, it remains available across all pages, preventing errors when a
user navigates away while a notification is still visible and later updated.  


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

#### NotificationProvider

.. kwargs::NotificationProvider

#### Notification

.. kwargs::Notification
