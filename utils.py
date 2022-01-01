def parse_apidocs(docs):
    header, api = docs.split("Keyword arguments:")
    desc = "\n".join(header.split("\n")[1:])
    return desc, api.strip()
