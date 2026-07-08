import streamlit as st


def footer_home():
    st.markdown(
        """
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
            <p style="font-weight:700; color:#FFFFFF; margin:0;">Created by Ravi Ranjan</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def footer_dashboard():
    st.markdown(
        """
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
            <p style="font-weight:700; color:#111111; margin:0;">Created by Ravi Ranjan</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
