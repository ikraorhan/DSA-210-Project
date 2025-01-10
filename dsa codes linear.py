import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Dosya Seçimi
Tk().withdraw()  # Tkinter arayüzünü gizle
file_path = askopenfilename(title="Bir Excel Dosyası Seçin", filetypes=[("Excel files", "*.xlsx *.xls")])

# Veriyi Okuma
df = pd.read_excel(file_path)

# Türkçe ay isimlerini İngilizceye çevirme
turkish_to_english_months = {
    "Oca": "Jan",
    "Şub": "Feb",
    "Mar": "Mar",
    "Nis": "Apr",
    "May": "May",
    "Haz": "Jun",
    "Tem": "Jul",
    "Ağu": "Aug",
    "Eyl": "Sep",
    "Eki": "Oct",
    "Kas": "Nov",
    "Ara": "Dec"
}

# Tarihleri Dönüştürme
df['Date'] = df['Date'].astype(str)
for turkish, english in turkish_to_english_months.items():
    df['Date'] = df['Date'].str.replace(turkish, english)
df['Date'] = pd.to_datetime(df['Date'], format='%d %b %Y', errors='coerce')
df = df.dropna(subset=['Date'])
df = df.sort_values(by='Date')

# 1. Grafik: Adım Sayısı Trendleri
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Steps'], color='blue', marker='o', linestyle='-', label='Adım Sayısı')
plt.title('Step Count Trends')
plt.xlabel('Date')
plt.ylabel('Step Counts')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("step_count_trend.png")  # Grafiği kaydet
plt.show()

# 2. Grafik: Ekran Süresi Trendleri
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Screen Time (hours)'], color='red', marker='o', linestyle='-', label='Ekran Süresi')
plt.title('Ekran Süresi Trendleri (Tam Tarih Aralığı)')
plt.xlabel('Tarih')
plt.ylabel('Ekran Süresi (Saat)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("screen_time_trend.png")  # Grafiği kaydet
plt.show()

