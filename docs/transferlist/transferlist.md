---
name: TransferList
section: Inputs
head: Move items between two lists.
description: Use TransferList to move items between two lists.
component: TransferList
styles: transfer-list
---

##### Simple Usage

.. exec::docs.transferlist.simple

##### Transferring only found items

By default, dmc.TransferList transfers all items when you click the "transfer all" button.
By setting the `transferAllMatchingFilter` prop to true, dmc.TransferList will only transfer the items that match the current filter.

.. exec::docs.transferlist.filter
    :prism: false

```python
import dash_mantine_components as dmc

dmc.TransferList(
    value=...,
    transferAllMatchingFilter=True
)
```

##### Empty search VS empty list

You can specify a `placeholder` prop, which will be used in place of the `nothingFound` when a list is completely empty, and no query is set.

.. exec::docs.transferlist.placeholder
    :prism: false

```python
import dash_mantine_components as dmc

dmc.TransferList(
    value=...,
    nothingFound="Nothing found",
    placeholder="No item left"
)
```

##### Custom wording for each list

`placeholder`, `nothingFound` and `searchPlaceholder` props can take a tuple of values instead of a single value to customize each list independently.

.. exec::docs.transferlist.custom
    :prism: false

```python
import dash_mantine_components as dmc

dmc.TransferList(
    value=...,
    searchPlaceholder=['Search item to add...', 'Search item to remove...'],
    nothingFound=['Cannot find item to add', 'Cannot find item to remove'],
    placeholder=['No item left to add', 'No item left ro remove']
)
```

##### Grouping items

.. exec::docs.transferlist.grouping
