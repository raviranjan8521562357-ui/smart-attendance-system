import types

from src.utils import urls


def test_build_join_url_prefers_app_base_url_secret(monkeypatch):
    monkeypatch.setattr(urls.st, "secrets", {"APP_BASE_URL": "https://smart-attendance-system.streamlit.app/"})
    monkeypatch.setattr(urls.st, "context", types.SimpleNamespace(url="https://ignored.streamlit.app/page", headers={}))

    join_url = urls.build_join_url("CS 101")

    assert join_url == "https://smart-attendance-system.streamlit.app/?join-code=CS+101"


def test_build_join_url_falls_back_to_runtime_context_url(monkeypatch):
    monkeypatch.setattr(urls.st, "secrets", {})
    monkeypatch.setattr(
        urls.st,
        "context",
        types.SimpleNamespace(url="https://current-app.streamlit.app/?join-code=OLD", headers={}),
    )

    join_url = urls.build_join_url("MATH-9")

    assert join_url == "https://current-app.streamlit.app/?join-code=MATH-9"
