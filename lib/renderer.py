from mistune import AstRenderer, create_markdown


def create_heading_id(string):
    string = string.replace("`", "")
    return "-".join(string.lower().split())


# noinspection PyMethodMayBeStatic
class DmcRenderer(AstRenderer):
    def heading(self, children, level):
        text = "".join(children)
        return {
            "block-name": "heading",
            "text": text,
            "id": create_heading_id(text),
        }

    def paragraph(self, text):
        return {"block-name": "paragraph", "text": "".join(text)}

    def codespan(self, text):
        return f"`{text}`"

    def text(self, text):
        return text

    def block_quote(self, text):
        action = text[0]["text"]
        params = action.split(":")
        if params[0] == "apidoc" and len(params) == 2:
            return {"block-name": "apidoc", "component": params[1]}
        elif "example" in params:
            return {
                "block-name": "example",
                "file": params[1],
                "run": "no-run" not in params,
                "prism": "no-prism" not in params,
            }
        elif "dmc" in params and len(params) == 2:
            return {"block-name": "dmc", "file": params[1]}
        elif "snippet" in params and len(params) == 3:
            return {"block-name": "snippet", "file": params[1], "language": params[2]}
        else:
            raise Exception("Problem in DmcRenderer!")

    def block_text(self, text):
        return "".join(text)

    def newline(self):
        pass

    def list(self, children, ordered, level, start=None):
        return {
            "block-name": "list",
            "type": "ordered" if ordered else "unordered",
            "children": children,
        }

    def list_item(self, children, level):
        return children[0]

    def strong(self, text):
        return f"**{''.join(text)}**"

    def emphasis(self, text):
        return f"_{''.join(text)}_"

    def finalize(self, data):
        return [x for x in data if x]


markdown = create_markdown(renderer=DmcRenderer())
