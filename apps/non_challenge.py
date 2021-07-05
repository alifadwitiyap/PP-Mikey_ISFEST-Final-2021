from matplotlib.pyplot import legend
import streamlit as st
import pandas as pd
import plotly.express as px


def load_df():
    df = pd.read_csv('https://raw.githubusercontent.com/ShinyQ/Dataset-DQThon/main/dqthon-participants.csv')
    return df

def app():
    df = load_df()

    st.markdown("## **Non-Challenge Exploration**")

    choose_age = st.selectbox('Silahkan Pilih Universitas', ["A", "B"])

    age = df.loc[lambda df: df['umur'] == choose_age]
    age = dict(age.occupation.value_counts())
    age = sorted(age.items(), key=lambda item: item[1], reverse=True)
    age = pd.DataFrame(list(age), columns=["Pekerjaan", "Jumlah"])

    fig = px.bar(age, x="Jumlah", y="Pekerjaan",
                 color="Pekerjaan", text="Jumlah", orientation="h")
    fig.update_layout(
        xaxis=dict(
            tickmode='linear',
            dtick=2
        ),
        showlegend=False,
        height=500,
        width=900,
        title=f"Tren Pekerjaan Berdasarkan Umur {choose_age}",
    )

    st.plotly_chart(fig)
