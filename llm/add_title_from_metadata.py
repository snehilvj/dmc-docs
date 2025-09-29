

def add_title_from_metadata(page: dict) -> str:
    description = page.get("description","")
    name = page["name"]
    category = page.get("category", "")
    content = page.get("content","")

    updated_content = f"\n\n## {name}  \n{description}  \nCategory: {category}  \n\n{content}"
    return updated_content