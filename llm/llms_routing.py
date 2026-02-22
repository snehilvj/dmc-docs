"""
LLM Middleware for Dash Apps

This module provides middleware to detect LLM (Large Language Model) crawlers
and serve pre-rendered textual documentation instead of the full Dash/React app.
It is designed for Dash apps where content is client-rendered and LLMs cannot
access it directly.

Features:
- Detects LLM crawlers via a safe, maintainable User-Agent allowlist.
- Supports a query-string override (`?llm=1`) for testing.
- Serves page-specific content from `assets/llms.json` when available.
- Falls back to a full text corpus in `assets/llms.txt` if no page-specific entry exists.
- Skips normal Dash rendering entirely for LLM requests, improving performance.
- Does not intercept standard static assets, favicons, or robots.txt.

Usage:
1. Call `register_llm_middleware(app)` after creating your Dash app instance.
2. Ensure `assets/llms.txt` and optionally `assets/llms.json` exist.
3. LLM requests will automatically receive plain-text content; humans and search engines
   continue to receive the full Dash app.

Be sure to run llm/generate_llms_text.py to update the assets/llms.txt and assets/llms.json files

Example:
    from dash import Dash
    from llm.llms_routing import register_llm_middleware

    app = Dash(__name__)
    register_llm_middleware(app)
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
    accept = (request.headers.get("Accept") or "").lower()

    # manual override for testing
    if request.args.get("llm") == "1":
        return True

    ua_match = any(k in ua for k in LLM_UA_KEYWORDS)
    wants_text = "text/plain" in accept
    no_browser_fetch = not request.headers.get("Sec-Fetch-Mode")

    if ua_match:
        return True

    # unknown UA but clearly non-browser text fetch
    if wants_text and no_browser_fetch:
        return True

    return False


def register_llm_middleware(app):
    server = app.server

    # preload once (fast, no disk I/O per request)
    llms_txt = Path("assets/llms.txt").read_text(encoding="utf-8")


    llms_json_path = Path("assets/llms.json")
    llms_json_raw = json.loads(llms_json_path.read_text(encoding="utf-8")) if llms_json_path.exists() else []

    # create a dictionary mapping endpoint → content
    llms_pages = {item["endpoint"]: item["content"] for item in llms_json_raw}

    @server.before_request
    def serve_llm_text():
        # never intercept static assets or the llm files themselves
        if request.path.startswith(("/assets", "/favicon.ico", "/robots.txt")):
            return

        if not is_llm_request():
            return  # normal Dash flow

        # page-specific content if available
        page_text = llms_pages.get(request.path)

        if page_text:
            return Response(
                page_text,
                mimetype="text/plain",
                headers={"Cache-Control": "public, max-age=3600"}
            )

        # fallback to full corpus
        return Response(
            llms_txt,
            mimetype="text/plain",
            headers={"Cache-Control": "public, max-age=3600"}
        )
