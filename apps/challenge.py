import streamlit as st
import pandas as pd
import datetime
import plotly.express as px
from datetime import *


@st.cache(allow_output_mutation=True)
def load_data():
    df = pd.read_csv('https://raw.githubusercontent.com/ShinyQ/Dataset-DQThon/main/dqthon-participants.csv')
    return df

def convert_percent(percent):
    return str(round(percent, 2)) + "%"


def trend_pekerjaan(df):
    st.markdown("### **1. Tren Pekerjaan Peserta**")
    st.code("""
    occupation = dict(df.occupation.value_counts())
    occupation = sorted(occupation.items(), key=lambda item: item[1], reverse=True)
    occupation = pd.DataFrame(list(occupation), columns=["Pekerjaan", "Jumlah"])
    """, language='python')

    occupation = dict(df.occupation.value_counts())
    occupation = sorted(occupation.items(), key=lambda item: item[1], reverse=True)
    occupation = pd.DataFrame(list(occupation), columns=["Pekerjaan", "Jumlah"])
    st.write(occupation)

    st.code("""
    occupation = occupation.head(10)
    fig = px.bar(occupation, x="Jumlah", y="Pekerjaan", color="Pekerjaan", text="Jumlah", orientation="h")
    fig.update_layout(
        xaxis=dict(
            tickmode='linear',
            dtick=20
        ),
        showlegend=False,
        height=500,
        width=900,
        title="Tren 10 Besar Pekerjaan Peserta",
    )
    """, language='python')

    occupation = occupation.head(10)
    fig = px.bar(occupation, x="Jumlah", y="Pekerjaan", color="Pekerjaan", text="Jumlah", orientation="h")
    fig.update_layout(
        xaxis=dict(
            tickmode='linear',
            dtick=20
        ),
        showlegend=False,
        height=500,
        width=900,
        title="Tren 10 Besar Pekerjaan Peserta",
    )

    st.plotly_chart(fig, use_container_width=False)


def trend_negara(df):
    st.markdown("### **2. Persentase Masing-Masing Negara**")
    st.code("""
    country = dict(df.country.value_counts())
    country = sorted(country.items(), key=lambda item: item[1], reverse=True)
    country = pd.DataFrame(list(country), columns=["Negara", "Jumlah"])

    country["Persentase"] = country["Jumlah"] / len(df) * 100
    country["Persentase"] = country["Persentase"].apply(convert_percent)
    """, language='python')

    country = dict(df.country.value_counts())
    country = sorted(country.items(), key=lambda item: item[1], reverse=True)
    country = pd.DataFrame(list(country), columns=["Negara", "Jumlah"])
    country["Persentase"] = country["Jumlah"] / len(df) * 100
    country["Persentase"] = country["Persentase"].apply(convert_percent)

    st.write(country)

    country = country.head(10)
    fig = px.bar(country, x="Jumlah", y="Negara", color="Negara", text="Jumlah", orientation="h")
    fig.update_layout(
        xaxis=dict(
            tickmode='linear',
            dtick=2
        ),
        showlegend=False,
        height=500,
        width=900,
        title="Tren 10 Besar Negara",
    )
    st.plotly_chart(fig)
    
    fig = px.pie(country, values='Jumlah', names='Negara', title='Persentase 10 Terbesar Negara Pendaftar')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(
        height=500,
        width=900,
        title="Tren 10 Besar Negara",
    )
    st.plotly_chart(fig)


def trend_kota(df):
    st.markdown("### **3. Persentase Masing-Masing Kota**")
    st.code(r'''
    df['city'] = df.address.str.extract(r'(?:\r\n?|\n)(.+?),')
    city = dict(df.city.value_counts())
    city = sorted(city.items(), key=lambda item: item[1], reverse=True)
    city = pd.DataFrame(list(city), columns=["Kota", "Jumlah"])
    city["Persentase"] = city["Jumlah"] / len(df) * 100
    city["Persentase"] = city["Persentase"].apply(convert_percent)
    ''', language='python')

    df['city'] = df.address.str.extract(r'(?:\r\n?|\n)(.+?),')
    city = dict(df.city.value_counts())
    city = sorted(city.items(), key=lambda item: item[1], reverse=True)
    city = pd.DataFrame(list(city), columns=["Kota", "Jumlah"])
    city["Persentase"] = city["Jumlah"] / len(df) * 100
    city["Persentase"] = city["Persentase"].apply(convert_percent)
    st.write(city)

    city = city.head(10)
    fig = px.bar(city, x="Jumlah", y="Kota", color="Kota", text="Jumlah", orientation="h")
    fig.update_layout(
        xaxis=dict(
            tickmode='linear',
            dtick=5
        ),
        showlegend=False,
        height=500,
        width=900,
        title="Tren Kota Pendaftar",
    )

    st.plotly_chart(fig)

    fig = px.pie(df, values=city['Jumlah'], names=city['Kota'], title='Persentase Kota 10 Terbesar Kota Pendaftar')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(
        height=500,
        width=900,
        title="Tren 10 Besar Negara",
    )
    st.plotly_chart(fig)

def app():
    # Load Dataset
    df = load_data()

    st.markdown("## **Challenge Exploration**")
    
    trend_pekerjaan(df)
    trend_negara(df)
    trend_kota(df)
    
    st.markdown("### **4. Pembagian Umur Berdasarkan Pekerjaan**")
    st.code('''
    def get_age(born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    umur = pd.to_datetime(df["birth_date"]).apply(get_age)
    df["umur"] = umur
    df["umur"].astype("int")

    choose_age = st.selectbox('Silahkan Pilih Umur', tuple([i for i in range(18, 32)]))

    age = df.loc[lambda df: df['umur'] == int(choose_age)]
    age = dict(age.occupation.value_counts())
    age = sorted(age.items(), key=lambda item: item[1], reverse=True)
    age = pd.DataFrame(list(age), columns=["Pekerjaan", "Jumlah"])
    ''', language='python')

    def get_age(born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    umur = pd.to_datetime(df["birth_date"]).apply(get_age)
    df["umur"] = umur
    df["umur"].astype("int")

    st.markdown(
        f"""
        <style>
            .stSlider{{
                max-width: 300px!important;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    choose_age = st.slider('Silahkan Pilih Umur', 18, 32, 18)

    age = df.loc[lambda df: df['umur'] == choose_age]
    age = dict(age.occupation.value_counts())
    age = sorted(age.items(), key=lambda item: item[1], reverse=True)
    age = pd.DataFrame(list(age), columns=["Pekerjaan", "Jumlah"])

    fig = px.bar(age, x="Jumlah", y="Pekerjaan", color="Pekerjaan", text="Jumlah", orientation="h")
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

    st.markdown("### **5. Tren Waktu Registrasi Pengguna**")
    st.code('''
    def get_age(born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    
    df["Umur"] = pd.to_datetime(df["birth_date"]).apply(get_age)
    umur = df.groupby(["occupation", "Umur"])["occupation"].agg(["count"])
    ''', language='python')

    def convertToRealDate(timestamp):
        dt_object = datetime.fromtimestamp(timestamp)
        return dt_object

    df["realDate"] = df["register_time"].apply(convertToRealDate)
    df["hour"] = df["realDate"].dt.hour
    df["minute"] = df["realDate"].dt.minute
    df["seconds"] = df["realDate"].dt.second
    df["hour"].unique()

    df["minute:sec"] = df["minute"].astype("str") + ":" + df["seconds"].astype("str")
    groupedMinuteSec = df.groupby("minute:sec")["seconds"].agg(["count"])

    fig = px.line(data_frame=groupedMinuteSec, x=groupedMinuteSec.index.get_level_values(0), y='count')
    fig.update_layout(
        yaxis=dict(
            tickmode='linear',
            dtick=5
        ),
        showlegend=False,
        height=500,
        width=1200,
        title="Tren Waktu Registrasi",
    )

    st.write(fig)

    st.markdown("### **6. Jumlah Pendaftar Berdasarkan Kampus**")
    st.code('''
    def get_age(born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    df["Umur"] = pd.to_datetime(df["birth_date"]).apply(get_age)
    umur = df.groupby(["occupation", "Umur"])["occupation"].agg(["count"])
    ''', language='python')

    institute = dict(df.institute.value_counts())
    institute = sorted(institute.items(), key=lambda item: item[1], reverse=True)
    institute = pd.DataFrame(list(institute), columns=["Institusi", "Jumlah"])
    st.write(institute)

    institute = institute.head(15)
    fig = px.bar(institute, x="Jumlah", y="Institusi", text="Jumlah", color="Institusi", orientation="h")
    fig.update_layout(
        xaxis=dict(
            tickmode='linear',
            dtick=2
        ),
        showlegend=False,
        height=600,
        width=900,
        title="Tren Institusi",
    )

    st.plotly_chart(fig, sharing="streamlit")
