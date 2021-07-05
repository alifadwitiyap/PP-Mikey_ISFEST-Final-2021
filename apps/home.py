import streamlit as st

def app():
    st.markdown('## **Deskripsi Pengerjaan**')

    st.markdown("""
        Peserta diminta untuk melakukan visualisasi data dengan menggunakan 
        dataset yang digunakan pada babak penyisihan dengan sekreatif
        mungkin (selain yang diperintahkan pada challenge) serta mengerjakan 
        challenge yang diberikan.
        
        **Challenge** \n
        Buatlah presentasi dashboard data dengan ketentuan sebagai berikut:\n
        1. Buatlah visualisasi data trend dari pekerjaan/occupation pada dataset.\n
        2. Buatlah pembagian percentage masing-masing negara (Country).\n
        3. Visualisasi masing-masing kota serta percentage count dari dataset (hint:
        data di-slicing dari kolom address).\n
        4. Visualisasi pembagian umur dengan masing-masing trend dari pekerjaan
        (hint: diambil dari birth date column).\n
        5. Visualisasi waktu registrasi trend dari database, di jam berapa pendaftaran
        traffic lebih banyak?\n
        6. Visualisasi kampus (Institute) yang paling banyak mendaftar.
    """)
