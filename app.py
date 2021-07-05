import streamlit as st
from multiapp import MultiApp
from apps import home, data, challenge, non_challenge

st.set_page_config(page_title='PP Mikey - ISFEST 2021 Final', layout='wide')
st.markdown("## **ISFEST 2021 : Final Data Competition - PP Mikey Team**")
st.markdown(
    f"""
        <style>
            .stSelectbox{{
                max-width: 400px!important;
            }}
        </style>
        """,
    unsafe_allow_html=True,
)
# Router
app = MultiApp()
app.add_app("🏠 Halaman Utama", home.app)
app.add_app("📈 Exploratory Data Analysis", data.app)
app.add_app("🏆 Challenge Exploration", challenge.app)
app.add_app("📊 Non-Challenge Exploration", non_challenge.app)
app.run()
