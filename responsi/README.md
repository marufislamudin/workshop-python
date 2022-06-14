# RESPONSI

## import package pandas untuk mengambil data

``` python
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as pd
```

## mendownload data dari url 
menggunakan  fungsi pd.read_csv untuk mengambil data yang ada pada link.

```python
>>> url = "https://data.jakarta.go.id/dataset/25ab0d30441a7ca1ad0e8b195be4dedc/resource/c1b0af737c9609d61cc58d9786a9c200/download/Data-Jumlah-Penerbitan-Akta-Kelahiran-Penduduk-DKI-Jakarta-Triwulan-1-Januari-sampai-Maret-Tahun-2021.csv1"
>>> df = pd.read_csv(url)
```

## menampilkan data
menampilkan data dengan memanggil df tempat untuk menyimpan data.

```python
>>> df
     tahun  triwulan           nama_kota   nama_kecamatan nama_kelurahan  jenis_kelamin  jumlah
0     2021         1  KAB.ADM.KEP.SERIBU  KEP. SERIBU UTR     P. PANGGANG     Laki-Laki      27
1     2021         1  KAB.ADM.KEP.SERIBU  KEP. SERIBU UTR       P. KELAPA     Laki-Laki      14
2     2021         1  KAB.ADM.KEP.SERIBU  KEP. SERIBU UTR      P. HARAPAN     Laki-Laki       8
3     2021         1  KAB.ADM.KEP.SERIBU  KEP. SERIBU SLT  P. UNTUNG JAWA     Laki-Laki       3
4     2021         1  KAB.ADM.KEP.SERIBU  KEP. SERIBU SLT       P. TIDUNG     Laki-Laki      19
..     ...       ...                 ...              ...             ...           ...     ...
529   2021         1       JAKARTA TIMUR         CIPAYUNG          MUNJUL     Perempuan     142
530   2021         1       JAKARTA TIMUR         CIPAYUNG            SETU     Perempuan      60
531   2021         1       JAKARTA TIMUR         CIPAYUNG      BAMBU APUS     Perempuan      86
532   2021         1       JAKARTA TIMUR         CIPAYUNG    LUBANG BUAYA     Perempuan     157
533   2021         1       JAKARTA TIMUR         CIPAYUNG           CEGER     Perempuan      92

[534 rows x 7 columns]
>>>
```

## Menampilkan 5 data dari atas
Menggunakan fungsi 

```python
>>> print(df.head(5))
   tahun  triwulan           nama_kota   nama_kecamatan nama_kelurahan  jenis_kelamin  jumlah
0   2021         1  KAB.ADM.KEP.SERIBU  KEP. SERIBU UTR     P. PANGGANG     Laki-Laki      27
1   2021         1  KAB.ADM.KEP.SERIBU  KEP. SERIBU UTR       P. KELAPA     Laki-Laki      14
2   2021         1  KAB.ADM.KEP.SERIBU  KEP. SERIBU UTR      P. HARAPAN     Laki-Laki       8
3   2021         1  KAB.ADM.KEP.SERIBU  KEP. SERIBU SLT  P. UNTUNG JAWA     Laki-Laki       3
4   2021         1  KAB.ADM.KEP.SERIBU  KEP. SERIBU SLT       P. TIDUNG     Laki-Laki      19
>>>
```

## Menampilkan kolom tertentu
langsung memanggil nama kolom nama_kota

```python
>>> df['nama_kota']
0      KAB.ADM.KEP.SERIBU
1      KAB.ADM.KEP.SERIBU
2      KAB.ADM.KEP.SERIBU
3      KAB.ADM.KEP.SERIBU
4      KAB.ADM.KEP.SERIBU
              ...
529         JAKARTA TIMUR
530         JAKARTA TIMUR
531         JAKARTA TIMUR
532         JAKARTA TIMUR
533         JAKARTA TIMUR
Name: nama_kota, Length: 534, dtype: object
>>>
```

## Menampilkan kolom 1 sampai 3
menggunakan fungsi ilon untuk memotong kolom pada dataframe. `df.iloc[:,1:4]]`
[*baris*,*kolom*]

```python
>>> data = df.iloc[:,1:4]
>>> data
     triwulan           nama_kota   nama_kecamatan
0           1  KAB.ADM.KEP.SERIBU  KEP. SERIBU UTR
1           1  KAB.ADM.KEP.SERIBU  KEP. SERIBU UTR
2           1  KAB.ADM.KEP.SERIBU  KEP. SERIBU UTR
3           1  KAB.ADM.KEP.SERIBU  KEP. SERIBU SLT
4           1  KAB.ADM.KEP.SERIBU  KEP. SERIBU SLT
..        ...                 ...              ...
529         1       JAKARTA TIMUR         CIPAYUNG
530         1       JAKARTA TIMUR         CIPAYUNG
531         1       JAKARTA TIMUR         CIPAYUNG
532         1       JAKARTA TIMUR         CIPAYUNG
533         1       JAKARTA TIMUR         CIPAYUNG

[534 rows x 3 columns]
>>>
```