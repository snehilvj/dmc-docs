import re


def replace_other_directives(md: str) -> str:
    remove_pattern = re.compile(
        r"^\.\.\s+[^\n]+(?:\n[ \t]+[^\n]+)*\n*",
        re.MULTILINE
    )
    md = remove_pattern.sub('', md)
    return md
