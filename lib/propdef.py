import json
from collections import defaultdict
from pathlib import Path

import dash_mantine_components as dmc

GITHUB_REPO_PREFIX = "https://github.com/snehilvj/dash-mantine-components/blob/master/"

# noinspection PyProtectedMember
filepath = Path(dmc._current_path).joinpath("metadata.json")
raw = json.loads(filepath.read_text())

propdef = defaultdict(dict)

props_to_exclude = [
    "unstyled",
    "m",
    "my",
    "mx",
    "mt",
    "mb",
    "ml",
    "mr",
    "p",
    "py",
    "px",
    "pt",
    "pb",
    "pl",
    "pr",
]

propdefs_to_exclude = """
- m (number; optional):
    margin props.

- mb (number; optional):
    margin props.

- ml (number; optional):
    margin props.

- mr (number; optional):
    margin props.

- mt (number; optional):
    margin props.

- mx (number; optional):
    margin props.

- my (number; optional):
    margin props.

- p (number; optional):
    padding props.

- pb (number; optional):
    padding props.

- pl (number; optional):
    padding props.

- pr (number; optional):
    padding props.

- pt (number; optional):
    padding props.

- px (number; optional):
    padding props.

- py (number; optional):
    padding props.

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.
"""


for path, values in raw.items():
    key = values.pop("displayName")
    propdef[key]["description"] = values.pop("description")
    newdef = []
    for prop, descr in values["props"].items():
        if prop not in props_to_exclude:
            prop_type = descr["type"]["raw"]
            newdef.append([prop, prop_type, descr["description"]])
    propdef[key]["props"] = newdef
    propdef[key]["github"] = GITHUB_REPO_PREFIX + path
