import streamlit as st
import pandas as pd
import plotly.express as px
from iso3166 import countries
import numpy as np

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

    df_top = df[df["country"].isin(best_country) & df['occupation'].isin(best_occupations)]
    df_occupations = df_top.groupby(["country", "occupation"])["country"].agg(["count"])

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
    occupation = sorted(occupation.items(), key=lambda item: item[1], reverse=True)
    occupation = pd.DataFrame(list(occupation), columns=["Pekerjaan", "Jumlah"])

    fig = px.bar(occupation, x="Jumlah", y="Pekerjaan", color="Pekerjaan", text='Jumlah', orientation="h")
    fig.update_layout(
        xaxis=dict(
            tickmode='linear',
            dtick=1
        ),
        showlegend=False,
        height=600,
        width=900,
        title=f"Tren Pekerjaan Pendaftar Berdasarkan Negara {choose_country}",
    )
    st.plotly_chart(fig)


def tren_institusi(df):
    st.markdown("### **2. Tren Pekerjaan Berdasarkan 10 Institusi Teratas**")
    st.code('''
    best_country = df["country"].value_counts()[:5].index
    best_occupations = df["occupation"].value_counts().index
    
    df_top = df[df["country"].isin(best_country) & df['occupation'].isin(best_occupations)]
    df_occupations = df_top.groupby(["country", "occupation"])["country"].agg(["count"])
    ''', language='python')

    best_institution = df["institute"].value_counts()[:10].index
    best_occupations = df["occupation"].value_counts().index

    df_top = df[df["institute"].isin(best_institution) & df['occupation'].isin(best_occupations)]
    df_occupations = df_top.groupby(["institute", "occupation"])["institute"].agg(["count"])

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

    choose_institute = st.selectbox('Silahkan Pilih Negara', best_institution)

    occupation = df_top.loc[lambda df: df_top['institute'] == choose_institute]
    occupation = dict(occupation.occupation.value_counts())
    occupation = sorted(occupation.items(), key=lambda item: item[1], reverse=True)
    occupation = pd.DataFrame(list(occupation), columns=["Pekerjaan", "Jumlah"])

    fig = px.bar(occupation, x="Jumlah", y="Pekerjaan", color="Pekerjaan", text='Jumlah', orientation="h")
    fig.update_layout(
        xaxis=dict(
            tickmode='linear',
            dtick=1
        ),
        showlegend=False,
        height=500,
        width=900,
        title=f"Tren Pekerjaan Pendaftar Berdasarkan Institusi {choose_institute}",
    )
    st.plotly_chart(fig)

def app():
    df = load_df()

    st.markdown("## **Non-Challenge Exploration**")

    tren_pekerjaan(df)
    tren_institusi(df)          

    st.markdown("### **3. Persebaran Pendaftar Berdasarkan Negara Pada Peta**")
    st.code('''
    def rename(country):
        try:
            return countries.get(country).alpha3
        except:
            return (np.nan)

    def rename_country(country):
        try:
            return countries.get(country).name
        except:
            return (np.nan)

    df['country_code'] = df['country'].apply(rename)
    df = df.dropna()

    country_df = pd.DataFrame(data=[df['country_code'].value_counts().index, df['country_code'].value_counts().values], index=['country', 'count']).T
    country_df['count'] = pd.to_numeric(country_df['count'])
    country_df['country_name'] = country_df['country'].apply(rename_country)
    ''', language='python')

    def rename(country):
        try:
            return countries.get(country).alpha3
        except:
            return (np.nan)

    def rename_country(country):
        try:
            return countries.get(country).name
        except:
            return (np.nan)

    df['country_code'] = df['country'].apply(rename)
    df = df.dropna()

    country_df = pd.DataFrame(data=[df['country_code'].value_counts().index, df['country_code'].value_counts().values], index=['country', 'count']).T
    country_df['count'] = pd.to_numeric(country_df['count'])
    country_df['country_name'] = country_df['country'].apply(rename_country)
    
    st.write(country_df)

    st.code('''
    fig = px.scatter_geo(country_df, locations="country", size='count', hover_name="country", color='country', projection="natural earth")
    fig.update_layout(
        showlegend=True,
        height=600,
        width=900,
        title=f"Persebaran Pendaftar Berdasarkan Negara",
    )
    ''', language='python')

    fig = px.scatter_geo(country_df, locations="country", size='count', hover_name="country_name", color='country_name', projection="natural earth")
    fig.update_layout(
        showlegend=True,
        height=600,
        width=1000,
        title=f"Persebaran Pendaftar Berdasarkan Negara",
    )
    st.plotly_chart(fig)
