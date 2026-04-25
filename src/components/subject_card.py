import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
<div style="
    background: #FFFFFF;
    border-left: 8px solid #EB459E;
    padding: 28px;
    border-radius: 22px;
    border: 1px solid rgba(45, 42, 114, 0.18);
    margin-bottom: 20px;
    box-shadow: 0 16px 32px rgba(45, 42, 114, 0.08);
">
    <h3 style="
        margin: 0 0 0.35rem 0;
        color: #111111;
        font-size: 1.75rem;
        font-weight: 800;
        line-height: 1.2;
    ">{name}</h3>
    <p style="
        color: #333333;
        margin: 0.65rem 0 1rem 0;
        font-size: 1.02rem;
        font-weight: 500;
    ">
        Code:
        <span style="
            background: #E0E3FF;
            color: #2D2A72;
            padding: 3px 10px;
            border-radius: 999px;
            font-weight: 800;
        ">{code}</span>
        <span style="color: #555555;"> | Section: {section}</span>
    </p>
"""

    if stats:
        html += '<div style="display:flex; gap:10px; flex-wrap:wrap;">'
        for icon, label, value in stats:
            html += (
                '<div style="'
                'background: #F7F5FF;'
                ' color: #333333;'
                ' padding: 8px 14px;'
                ' border-radius: 999px;'
                ' font-size: 0.95rem;'
                ' border: 1px solid rgba(88, 101, 242, 0.14);'
                '">'
                f'<span style="font-weight: 700; color: #2D2A72;">{icon}</span>'
                f'<b style="color: #111111;"> {value}</b>'
                f'<span style="color: #555555;"> {label}</span>'
                '</div>'
            )
        html += "</div>"

    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
