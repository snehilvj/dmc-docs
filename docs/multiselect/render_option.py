import dash_mantine_components as dmc

users_data = {
    "Emily Johnson": {
        "image": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-7.png",
        "email": "emily92@gmail.com",
    },
    "Ava Rodriguez": {
        "image": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-8.png",
        "email": "ava_rose@gmail.com",
    },
    "Olivia Chen": {
        "image": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-4.png",
        "email": "livvy_globe@gmail.com",
    },
    "Ethan Barnes": {
        "image": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-1.png",
        "email": "ethan_explorer@gmail.com",
    },
    "Mason Taylor": {
        "image": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-2.png",
        "email": "mason_musician@gmail.com",
    },
}

component = dmc.MultiSelect(
    data=list(users_data.keys()),
    label="Employees of the month",
    placeholder="Search for employee",
    maxDropdownHeight=300,
    searchable=True,
    hidePickedOptions=True,
    renderOption={
        "function": "renderUserOption",
        "options": {"users": users_data},
    },
)
