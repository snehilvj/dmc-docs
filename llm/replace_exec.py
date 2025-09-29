import re
from pathlib import Path


def make_code_block(dotted_path: str) -> str:
    """Read the Python file corresponding to dotted_path and return a Markdown code block."""

    file_path = Path(f"../{dotted_path.replace('.', '/')}.py")

    try:
        content = file_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"```text\n# ERROR: File not found: {file_path}\n```")
        return ""

    # don't include the interactive configurator examples
    if "Configurator" in content:
        return ""

    return f"```python\n{content.strip()}\n```"


def replace_exec_directives(md: str) -> str:
    """Replace .. exec::<dotted.path> directives with code blocks, or remove if :code: false."""

    # Pattern for directives with ":code: false" (remove them)
    remove_pattern = re.compile(
        r"^\.\.\s+exec::[\w\.-]+\s*\n[ \t]+:code:\s*false\s*(?:\n\s*)*",
        re.MULTILINE
    )
    md = remove_pattern.sub('', md)

    # Pattern for simple exec directives (replace with code)
    code_pattern = re.compile(
        r'^\.\.\s+exec::([a-zA-Z0-9_.]+)\s*$',
        re.MULTILINE
    )

    def repl(match):
        dotted_path = match.group(1)
        return make_code_block(dotted_path)

    return code_pattern.sub(repl, md)
