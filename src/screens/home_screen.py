import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():
    header_home()
    style_background_home()
    style_base_layout()

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """
            <div class="portal-card-copy">
                <h3>I'm Student</h3>
                <p>Use face login, join subjects, and track your attendance from one place.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)
        if st.button(
            "Student Portal",
            type="primary",
            icon=":material/arrow_outward:",
            icon_position="right",
        ):
            st.session_state["login_type"] = "student"
            st.rerun()

    with col2:
        st.markdown(
            """
            <div class="portal-card-copy">
                <h3>I'm Teacher</h3>
                <p>Create subjects, run attendance workflows, and review class records clearly.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=145)
        if st.button(
            "Teacher Portal",
            type="primary",
            icon=":material/arrow_outward:",
            icon_position="right",
        ):
            st.session_state["login_type"] = "teacher"
            st.rerun()

    footer_home()
