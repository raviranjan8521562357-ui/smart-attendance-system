import streamlit as st


def style_background_home():
    st.markdown(
        """
        <style>
            .stApp {
                background: #5865F2 !important;
            }

            .stApp div[data-testid="stColumn"] {
                background-color: #E0E3FF !important;
                padding: 2.5rem !important;
                border-radius: 3rem !important;
                border: 1px solid rgba(255, 255, 255, 0.22) !important;
                box-shadow: 0 18px 40px rgba(26, 35, 126, 0.16) !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_background_dashboard():
    st.markdown(
        """
        <style>
            .stApp {
                background: #E0E3FF !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_base_layout():
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

            :root {
                --sat-text: #111111;
                --sat-text-secondary: #333333;
                --sat-label: #555555;
                --sat-heading: #2D2A72;
                --sat-surface: #FFFFFF;
                --sat-surface-soft: #F7F5FF;
                --sat-primary: #5865F2;
                --sat-secondary: #EB459E;
                --sat-dark: #111111;
                --sat-border: rgba(45, 42, 114, 0.14);
            }

            #MainMenu, footer, header {
                visibility: hidden;
            }

            html, body, [class*="css"] {
                font-family: 'Outfit', sans-serif !important;
                color: var(--sat-text) !important;
            }

            .block-container {
                padding-top: 1.5rem !important;
                padding-bottom: 2rem !important;
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 1.08 !important;
                letter-spacing: 0.02em !important;
                margin-bottom: 0.4rem !important;
                color: var(--sat-heading) !important;
            }

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2.35rem !important;
                line-height: 1.02 !important;
                letter-spacing: 0.01em !important;
                margin-bottom: 0.35rem !important;
                color: var(--sat-heading) !important;
            }

            h3, h4, h5, h6 {
                font-family: 'Outfit', sans-serif !important;
                color: var(--sat-text) !important;
                letter-spacing: -0.01em !important;
            }

            p, li, div[data-testid="stMarkdownContainer"] p, div[data-testid="stMarkdownContainer"] li {
                color: var(--sat-text-secondary) !important;
                line-height: 1.5 !important;
            }

            label,
            .stTextInput label,
            .stSelectbox label,
            .stTextArea label,
            .stNumberInput label,
            .stMultiSelect label,
            .stDateInput label,
            .stTimeInput label,
            div[data-testid="stWidgetLabel"] label,
            div[data-testid="stWidgetLabel"] p {
                color: var(--sat-label) !important;
                font-weight: 700 !important;
                font-size: 0.98rem !important;
                letter-spacing: 0.01em !important;
            }

            .stCaption, small {
                color: var(--sat-label) !important;
            }

            hr, .stDivider {
                border-color: rgba(45, 42, 114, 0.12) !important;
            }

            div[data-testid="stTextInputRootElement"],
            div[data-testid="stTextArea"] textarea,
            div[data-baseweb="select"] > div,
            div[data-testid="stNumberInput"] input {
                border-radius: 1rem !important;
            }

            div[data-baseweb="select"] > div,
            div[data-testid="stTextInputRootElement"] > div,
            div[data-testid="stTextArea"] textarea {
                border: 1px solid rgba(255, 255, 255, 0.05) !important;
                box-shadow: none !important;
            }

            input, textarea {
                color: #FFFFFF !important;
                background: #2F3040 !important;
                font-size: 1rem !important;
            }

            input::placeholder, textarea::placeholder {
                color: #B9BFD9 !important;
                opacity: 1 !important;
            }

            div[data-baseweb="select"] * {
                color: #FFFFFF !important;
                font-size: 1rem !important;
            }

            div[data-baseweb="select"] > div {
                background: #2F3040 !important;
            }

            div[data-baseweb="select"] svg,
            [data-testid="stTextInputRootElement"] svg {
                fill: #FFFFFF !important;
                color: #FFFFFF !important;
            }

            button {
                border-radius: 1.5rem !important;
                background-color: var(--sat-primary) !important;
                color: #FFFFFF !important;
                padding: 0.8rem 1.35rem !important;
                border: none !important;
                transition: transform 0.2s ease, filter 0.2s ease !important;
                font-weight: 700 !important;
                font-size: 1rem !important;
                letter-spacing: 0.01em !important;
                min-height: 3.2rem !important;
                box-shadow: 0 10px 24px rgba(88, 101, 242, 0.18) !important;
            }

            button[kind="secondary"] {
                background-color: var(--sat-secondary) !important;
                box-shadow: 0 10px 24px rgba(235, 69, 158, 0.18) !important;
            }

            button[kind="tertiary"] {
                background-color: #171717 !important;
                box-shadow: 0 10px 24px rgba(17, 17, 17, 0.18) !important;
            }

            div[data-testid="stButton"] button,
            div[data-testid="stButton"] button *,
            div[data-testid="stBaseButton-secondary"] button,
            div[data-testid="stBaseButton-secondary"] button *,
            div[data-testid="stBaseButton-tertiary"] button,
            div[data-testid="stBaseButton-tertiary"] button *,
            button p, button span, button div,
            button svg {
                color: #FFFFFF !important;
                fill: #FFFFFF !important;
                font-weight: 700 !important;
            }

            button[kind="primary"] {
                color: #FFFFFF !important;
            }

            button[kind="secondary"] {
                color: #FFFFFF !important;
            }

            button[kind="tertiary"] {
                color: #FFFFFF !important;
            }

            button[kind="primary"] *, button[kind="secondary"] *, button[kind="tertiary"] * {
                color: #FFFFFF !important;
                fill: #FFFFFF !important;
            }

            button:hover {
                transform: scale(1.03);
                filter: brightness(1.03);
            }

            div[data-testid="stButton"] {
                margin-top: 0.2rem !important;
            }

            div[data-testid="stAlert"] p,
            div[data-testid="stToast"] p {
                color: inherit !important;
            }

            [data-testid="stDataFrame"] *, [data-testid="stTable"] * {
                color: var(--sat-text) !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
