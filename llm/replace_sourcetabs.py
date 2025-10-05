import re
from pathlib import Path

def get_language_from_suffix(file_path: Path) -> str:
    """Return appropriate language for fenced code block based on file extension."""
    ext = file_path.suffix.lower()
    if ext == ".py":
        return "python"
    if ext in (".js", ".mjs"):
        return "javascript"
    if ext in (".ts", ".tsx"):
        return "typescript"
    if ext in (".css",):
        return "css"
    return ""  # fallback, renders as plain text

def read_file_content(file_path: Path) -> str:
    """Read file content and format as code block."""
    if not file_path.exists():
        print(f"```text\n# ERROR: File not found: {file_path}\n```")
        return ""
    lang = get_language_from_suffix(file_path)
    content = file_path.read_text(encoding="utf-8").rstrip()
    if lang == "":
        return content
    return f"```{lang}\n{content}\n```"

def replace_sourcetabs(md: str) -> str:
    """
    Replace .. sourcetabs::file1, file2, ...
    with code blocks containing the file contents.
    """
    pattern = re.compile(
        r"^\.\. sourcetabs::([^\n]+)(?:\n\s*:[^\n]+)*",
        re.MULTILINE
    )

    def replacer(match):
        base_dir = Path("..").resolve()
        files_str = match.group(1).strip()
        file_paths = [Path(base_dir) / f.strip() for f in files_str.split(",")]
        code_blocks = [read_file_content(fp) for fp in file_paths]
        return "\n\n".join(code_blocks)

    return pattern.sub(replacer, md)


# Example usage:
if __name__ == "__main__":
    md = """
### Example

.. sourcetabs::docs/dashprops/slider_label.py, assets/examples-js/celcius_label.js
    :defaultExpanded: true
    :withExpandedButton: true
    :display: none
"""

    new_md = replace_sourcetabs(md)
    print(new_md)
