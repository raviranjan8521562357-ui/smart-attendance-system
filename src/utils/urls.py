from urllib.parse import urlencode, urlsplit

import streamlit as st


def resolve_app_base_url() -> str:
    app_base_url = st.secrets.get("APP_BASE_URL")
    if app_base_url:
        return str(app_base_url).rstrip("/")

    context_url = getattr(st.context, "url", "")
    if context_url:
        parsed = urlsplit(str(context_url))
        if parsed.scheme and parsed.netloc:
            return f"{parsed.scheme}://{parsed.netloc}".rstrip("/")

    headers = getattr(st.context, "headers", {}) or {}
    host = headers.get("Host") or headers.get("host")
    proto = headers.get("X-Forwarded-Proto") or headers.get("x-forwarded-proto") or "https"
    if host:
        return f"{proto}://{host}".rstrip("/")

    return "http://localhost:8501"


def build_join_url(subject_code: str) -> str:
    query = urlencode({"join-code": subject_code})
    return f"{resolve_app_base_url()}/?{query}"
