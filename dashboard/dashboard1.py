import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul Dashboard
st.title('Dashboard Penyewaan Sepeda')

# Load Data
day_df = pd.read_csv('data/day.csv', parse_dates=['dteday'])  # sesuaikan path jika perlu

# Menambahkan kolom bulan
day_df['bulan'] = day_df['dteday'].dt.month_name()

# Sidebar untuk memilih pertanyaan yang ingin dilihat
sidebar_option = st.sidebar.selectbox(
    'Pilih Pertanyaan yang Ingin Ditampilkan:',
    ('Penyewaan Hari Kerja vs Akhir Pekan', 'Tren Penyewaan Bulanan', 'Data Penyewaan Sepeda')
)

# Menampilkan konten sesuai pilihan di sidebar
if sidebar_option == 'Penyewaan Hari Kerja vs Akhir Pekan':
    # Rata-rata Penyewaan Hari Kerja vs Akhir Pekan
    average_weekday_rentals = day_df[day_df['workingday'] == 1]['cnt'].mean()
    average_weekend_rentals = day_df[day_df['workingday'] == 0]['cnt'].mean()

    st.subheader('Rata-rata Penyewaan Sepeda pada Hari Kerja vs Akhir Pekan')
    st.write(f"Rata-rata sepeda yang disewa pada hari kerja: {average_weekday_rentals:.0f} penyewaan.")
    st.write(f"Rata-rata sepeda yang disewa pada akhir pekan: {average_weekend_rentals:.0f} penyewaan.")

    # Membuat visualisasi bar chart
    categories = ['Hari Kerja', 'Akhir Pekan']
    average_rentals = [average_weekday_rentals, average_weekend_rentals]

    fig1, ax1 = plt.subplots()
    ax1.bar(categories, average_rentals, color=['blue', 'orange'])
    ax1.set_title('Rata-rata Penyewaan Sepeda: Hari Kerja vs Akhir Pekan')
    ax1.set_xlabel('Kategori')
    ax1.set_ylabel('Rata-rata Penyewaan')

    st.pyplot(fig1)

elif sidebar_option == 'Tren Penyewaan Bulanan':
    # Tren Penyewaan Bulanan
    rata_rata_per_bulan = day_df.groupby('bulan')['cnt'].mean().reindex([
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ]).round(0)

    st.subheader('Tren Rata-rata Penyewaan Sepeda per Bulan')
    st.write("Berikut adalah tren penyewaan sepeda bulanan di tahun 2012:")

    # Membuat visualisasi untuk tren bulanan
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    rata_rata_per_bulan.plot(kind='line', marker='o', ax=ax2)
    ax2.set_title('Tren Rata-rata Penyewaan Sepeda per Bulan')
    ax2.set_xlabel('Bulan')
    ax2.set_ylabel('Jumlah Penyewaan')
    
    st.pyplot(fig2)

elif sidebar_option == 'Data Penyewaan Sepeda':
    # Menampilkan Dataframe
    st.write('Data Penyewaan Sepeda:')
    st.dataframe(day_df.head())
