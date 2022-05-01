from os import environ

import dash_mantine_components as dmc
import requests


def create_contributors_list():
    resp = requests.get(
        "https://api.github.com/repos/snehilvj/dash-mantine-components/contributors",
        headers={"authorization": f"token {environ['CONTRIB_TOKEN']}"},
    )
    contributors = resp.json()
    print(contributors)

    children = []
    for user in contributors:
        avatar = dmc.Avatar(src=user["avatar_url"])
        children.append(avatar)

    return dmc.AvatarsGroup(children, limit=3, size=50)


component = create_contributors_list()
