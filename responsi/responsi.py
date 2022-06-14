import pandas as pd

url = "https://data.jakarta.go.id/dataset/data-penerbitan-akta-kelahiran-tahun-2021"
df = pd.read_csv(url)

# menampilkan data
print(df)

# menampilkan data 5 dari awal/atas
print(df.head(5))

# menampilkan data dengan hanya kolom nama_kota
df['nama_kota']

# menampilkan data hanya dengan nama kota == JAKARTA TIMUR
data = df[df.nama_kota=='JAKARTA TIMUR']
data

# menampilkan data kolom 1 sampai 3
data = df.iloc[:,1:4]
data