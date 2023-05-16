import streamlit as st
import pandas as pd
import io


def load_data():
    data = pd.read_csv('./dqthon-participants.csv')
    return data


def app():
    # Load Dataset
    df = load_data()

    # Show Dataset
    st.markdown("### **Import Dataset DQthon**")
    st.code('''
    import pandas as pd
    df = pd.read_csv('dqthon-participants.csv')
    df.sample(10)''', language='python')

    st.write(df.sample(10))

    # Dataset Description
    st.markdown("\n### **Deskripsi Field Dataset**")
    st.write("Berikut merupakan penjelasan detail dari masing-masing field yang ada pada dataset.")
    st.markdown('''
        | Field               | Deskripsi   |
        | --------------------| ------------|
        | participant_id      | Kode unik yang diberikan kepada pengguna berupa kumpulan ``integer``  |
        | first_name          | Nama depan pengguna berupa ``string``                                 |
        | last_name           | Nama belakang pengguna berupa ``string``                              |
        | birth_date          | Tanggal lahir pengguna berupa ``datetime``                            |
        | address             | Alamat tempat tinggal pengguna berupa ``string``                      |
        | phone_number        | Nomor telepon pengguna berupa  ``integer``                            |
        | country             | Negara tempat tinggal pengguna berupa ``string``                      |
        | institute           | Institusi asal pengguna berupa ``string``                             |
        | occupation          | Pekerjaan pengguna berupa ``string``                                  |
        | register_time       | Waktu registrasi yang dilakukan oleh pengguna berupa ``timestamp``    |
    ''')

    # Checking Null Value
    st.markdown("### **Mengecek Data Kosong**")
    st.code('''df.isna().sum()''', language='python')
    st.write(df.isna().sum())

    st.markdown("### **Mengecek Nilai Unik Data Kategorikal**")

    st.code(''' categorical = df.select_dtypes(include=[object]).columns.tolist()''', language='python')
    categorical = df.select_dtypes(include=[object]).columns.tolist()
    st.write(categorical)

    st.code(''' 
    for cat in categorical:
        st.write(f'Jumlah Value Uniqe {cat} : {len(df[cat].value_counts())}')
        st.write(df[cat].value_counts().head(10))
    ''', language='python')
    for cat in categorical:
        st.write(f'Jumlah Value Uniqe {cat} : {len(df[cat].value_counts())}')
        st.write(df[cat].value_counts().head(10))

    # for cat in categorical:
    #     st.write(df[cat].value_counts())
