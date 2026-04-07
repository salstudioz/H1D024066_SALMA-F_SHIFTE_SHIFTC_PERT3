```markdown
# Implementasi Logika Fuzzy Mamdani – Studi Kasus Udin Pet Shop & Evaluasi Kepuasan Pelayanan

Repositori ini berisi implementasi **sistem inferensi fuzzy Mamdani** menggunakan Python dan pustaka `scikit-fuzzy` untuk dua studi kasus:

1. **Optimasi Stok Makanan Hewan (Udin Pet Shop)**  
   Menentukan jumlah stok optimal berdasarkan 4 input: barang terjual, permintaan, harga per item, dan profit.

2. **Evaluasi Kepuasan Pelayanan Masyarakat**  
   Menghitung indeks kepuasan pelayanan berdasarkan 4 dimensi: kejelasan informasi, kejelasan persyaratan, kemampuan petugas, dan ketersediaan sarpras.

## 📁 Struktur File

```
├── studi_kasus_1_udin_petshop.py
├── studi_kasus_2_kepuasan_pelayanan.py
└── README.md
```

## ⚙️ Prasyarat

Pastikan Python 3.7+ terinstal, kemudian install pustaka yang dibutuhkan:

```bash
pip install numpy scikit-fuzzy matplotlib
```

##  Cara Menjalankan

### Studi Kasus 1 – Udin Pet Shop
```bash
python studi_kasus_1_udin_petshop.py
```
**Output contoh:**  
`Jumlah Stok Makanan Rekomendasi: 834.XX unit`  
(Muncul juga plot kurva output hasil defuzzifikasi)

### Studi Kasus 2 – Kepuasan Pelayanan
```bash
python studi_kasus_2_kepuasan_pelayanan.py
```
**Output contoh:**  
```
Tingkat Kepuasan Pelayanan: 214.82 (skala 0-400)
Kategori: Cukup Memuaskan
```
(Muncul plot kurva output)

##  Penjelasan Singkat

### Studi Kasus 1
- **Input:**  
  `barang_terjual` (0-100), `permintaan` (0-300), `harga_item` (0-100.000), `profit` (0-4.000.000)  
- **Output:**  
  `stok_makanan` (0-1000 unit) dengan himpunan `sedang` dan `banyak`.  
- **Aturan:** 6 aturan IF-THEN (contoh: jika penjualan tinggi, permintaan tinggi, harga murah, profit tinggi → stok banyak).  
- **Data uji:** `[80, 255, 25000, 3500000]` → menghasilkan stok ~834 unit.

### Studi Kasus 2
- **Input (masing-masing 0-100):**  
  `kejelasan_informasi`, `kejelasan_persyaratan`, `kemampuan_petugas`, `ketersediaan_sarpras`  
  Masing‑masing memiliki 3 himpunan: *tidak memuaskan*, *cukup memuaskan*, *memuaskan*.  
- **Output:**  
  `kepuasan_pelayanan` (0-400) dengan 5 kategori: *tidak memuaskan*, *kurang memuaskan*, *cukup memuaskan*, *memuaskan*, *sangat memuaskan*.  
- **Aturan:** 81 aturan (3⁴) dibangkitkan secara otomatis berdasarkan total skor.  
- **Data uji:** `[80, 60, 50, 90]` → menghasilkan skor ~214,82 (cukup memuaskan).

