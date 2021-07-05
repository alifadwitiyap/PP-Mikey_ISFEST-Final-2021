from matplotlib.pyplot import legend
import streamlit as st
import pandas as pd
import plotly.express as px


def load_df():
    df = pd.read_csv('https://raw.githubusercontent.com/ShinyQ/Dataset-DQThon/main/dqthon-participants.csv')
    return df


def tren_pekerjaan(df):
    st.markdown("### **1. Tren Pekerjaan Berdasarkan 5 Negara Teratas**")
    st.code('''
    best_country = df["country"].value_counts()[:5].index
    best_occupations = df["occupation"].value_counts().index
    
    df_top = df[df["country"].isin(best_country) & df['occupation'].isin(best_occupations)]
    df_occupations = df_top.groupby(["country", "occupation"])["country"].agg(["count"])
    ''', language='python')

    best_country = df["country"].value_counts()[:5].index
    best_occupations = df["occupation"].value_counts().index

    df_top = df[df["country"].isin(
        best_country) & df['occupation'].isin(best_occupations)]
    df_occupations = df_top.groupby(["country", "occupation"])[
        "country"].agg(["count"])

    st.write(df_occupations)

    st.code('''
    occupation = df_top.loc[lambda df: df_top['country'] == choose_country]
    occupation = dict(occupation.occupation.value_counts())
    occupation = sorted(occupation.items(), key=lambda item: item[1], reverse=True)
    occupation = pd.DataFrame(list(occupation), columns=["Pekerjaan", "Jumlah"])

    fig = px.bar(occupation, x="Jumlah", y="Pekerjaan", color="Pekerjaan", orientation="h")
    fig.update_layout(
        xaxis=dict(
            tickmode='linear',
            dtick=1
        ),
        showlegend=False,
        height=500,
        width=900,
        title=f"Tren Pekerjaan Pendaftar Berdasarkan Negara {choose_country}",
    )
    ''', language='python')

    choose_country = st.selectbox('Silahkan Pilih Negara', best_country)

    occupation = df_top.loc[lambda df: df_top['country'] == choose_country]
    occupation = dict(occupation.occupation.value_counts())
    occupation = sorted(occupation.items(),
                        key=lambda item: item[1], reverse=True)
    occupation = pd.DataFrame(list(occupation), columns=[
                              "Pekerjaan", "Jumlah"])

    fig = px.bar(occupation, x="Jumlah", y="Pekerjaan",
                 color="Pekerjaan", orientation="h")
    fig.update_layout(
        xaxis=dict(
            tickmode='linear',
            dtick=1
        ),
        showlegend=False,
        height=500,
        width=900,
        title=f"Tren Pekerjaan Pendaftar Berdasarkan Negara {choose_country}",
    )
    st.plotly_chart(fig)

def app():
    df = load_df()

    st.markdown("## **Non-Challenge Exploration**")

    tren_pekerjaan(df)

    
