import re
from textwrap import dedent
import dash_mantine_components as dmc

from lib.constants import PROPS_TO_EXCLUDE


def filter_kwargs(kwargs_text: str) -> str:
    """
    Remove kwargs entries whose property names are in `PROPS_TO_EXCLUDE`.
    """
    # Regex matches a prop block starting with "- propName" and including its indented lines
    pattern = re.compile(
        r"(?m)^- ([\w-]+).*?(?=^\s*-\s|\Z)",  # lookahead stops at next '- prop' or EOF
        re.DOTALL
    )

    filtered_blocks = []
    for match in pattern.finditer(kwargs_text):
        prop_name = match.group(1)
        block = match.group(0)
        if prop_name not in PROPS_TO_EXCLUDE:
            filtered_blocks.append(block.rstrip())

    return "\n\n".join(filtered_blocks)



def generate_kwargs_block(name: str) -> str:

    component = getattr(dmc, name)
    component_doc = component.__doc__
    docs = component_doc.split("Keyword arguments:")[-1]
    filtered = filter_kwargs(dedent(docs))
    return filtered

def replace_kwargs(md: str) -> str:
    """
    Find .. kwargs::<Name> and replace with generated content.
    """
    pattern = re.compile(r"^\.\. kwargs::\s*([A-Za-z0-9_.-]+)\s*$", re.MULTILINE)

    def replacer(match):
        name = match.group(1)
        return generate_kwargs_block(name)

    return pattern.sub(replacer, md)
