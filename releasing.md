Maintainer Notes:

- Update versions in `migration.md` `lib.constants`
- Update dependencies in pyproject.toml and requirements.txt
- run `poetry update ` and push changes to `poetry.lock`
- run llm/generate_llms_txt.py.  Push changes to assets/llms.txt
- Changes are deployed automatically. Check logs on Render.com if the [dmc-docs site](https://www.dash-mantine-components.com/) does not update