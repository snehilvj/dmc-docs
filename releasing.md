Maintainer Notes:

- Update versions in `migration.md` `utils.constants`
- Update dependencies requirements.txt
- run llm/generate_llms_txt.py.  Push changes to assets/llms.txt
- Changes to the `main` branch are deployed automatically on Render. Check logs on Render.com if the [dmc-docs site](https://www.dash-mantine-components.com/) does not update


Publishing to Plotly Cloud

1.  Log into Plotly Cloud
2. From the command line:
```bash
plotly app publish --name dmc-v2

```
