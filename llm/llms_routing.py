"""
LLM Middleware for Dash Apps (with Markdown + extension support)
Creates sitemap.xml
"""

import json
from pathlib import Path
from flask import Response, request


LLM_UA_KEYWORDS = (
    "gptbot",
    "chatgpt-user",
    "claudebot",
    "anthropic-ai",
    "perplexitybot",
    "perplexity-ai",
    "ccbot",
    "amazonbot",
    "bytespider",
)

def is_llm_request():
    ua = (request.headers.get("User-Agent") or "").lower()

    # manual override for testing
    if request.args.get("llm") == "1":
        return True

    return any(k in ua for k in LLM_UA_KEYWORDS)


def wants_markdown():
    accept = (request.headers.get("Accept") or "").lower()
    return "text/markdown" in accept


def extract_format(path):
    if path.endswith(".md"):
        return path[:-3] or "/", "md"
    if path.endswith(".txt"):
        return path[:-4] or "/", "txt"
    return None, None


def register_llm_middleware(app):
    server = app.server

    # preload assets once
    llms_txt = Path("assets/llms.txt").read_text(encoding="utf-8")

    llms_json_path = Path("assets/llms.json")
    llms_json_raw = (
        json.loads(llms_json_path.read_text(encoding="utf-8"))
        if llms_json_path.exists()
        else []
    )

    # map endpoint → content
    llms_pages = {item["endpoint"]: item["content"] for item in llms_json_raw}


    @server.route("/sitemap.xml")
    def sitemap():
        base = "https://www.dash-mantine-components.com"

        urls = []

        for endpoint in llms_pages.keys():
            # skip non-pages if needed
            if endpoint in ("/404",):
                continue

            urls.append(f"""
        <url>
            <loc>{base}{endpoint}</loc>
        </url>
    """)

        xml = f"""<?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    {''.join(urls)}
    </urlset>"""

        return Response(xml, content_type="application/xml")

    @server.before_request
    def serve_llm_text():
        # skip static
        if request.path.startswith(("/assets", "/favicon.ico", "/robots.txt")):
            return

        # --- 1) explicit .md / .txt requests ---
        base_path, fmt = extract_format(request.path)
        if fmt:
            page_text = llms_pages.get(base_path, llms_txt)

            content_type = "text/markdown" if fmt == "md" else "text/plain"

            return Response(
                page_text,
                content_type=content_type,
                headers={"Cache-Control": "public, max-age=3600"},
            )

        # --- 2) Accept: text/markdown negotiation ---
        if wants_markdown():
            page_text = llms_pages.get(request.path, llms_txt)

            return Response(
                page_text,
                content_type="text/markdown",
                headers={"Cache-Control": "public, max-age=3600"},
            )

        # --- 3) LLM UA detection fallback ---
        if not is_llm_request():
            return  # normal Dash flow

        page_text = llms_pages.get(request.path, llms_txt)

        return Response(
            page_text,
            content_type="text/plain",
            headers={"Cache-Control": "public, max-age=3600"},
        )