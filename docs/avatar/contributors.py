from os import environ

import dash_mantine_components as dmc
import requests


def create_contributors_list():
    resp = requests.get(
        "https://api.github.com/repos/snehilvj/dash-mantine-components/contributors",
        headers={"authorization": f"token {environ['CONTRIB_TOKEN']}"},
    )
    contributors = resp.json()

    children = []
    for user in contributors:
        avatar = dmc.Avatar(src=user["avatar_url"], radius="xl")
        children.append(avatar)

    return dmc.AvatarGroup(children, id="avatar-group")


component = create_contributors_list() if "CONTRIB_TOKEN" in environ else None
