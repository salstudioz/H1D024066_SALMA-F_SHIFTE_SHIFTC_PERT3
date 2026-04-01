import numpy as np

# =============================================
# STUDI KASUS 1 - LOGIKA FUZZY MAMDANI
# Udin Pet Shop - Optimasi Stok Makanan Hewan
# =============================================

# ------ INPUT ------
barang_terjual = 80
permintaan = 255
harga_per_item = 25000
profit = 3500000

print("=" * 60)
print("STUDI KASUS 1 - UDIN PET SHOP (FUZZY MAMDANI)")
print("=" * 60)
print(f"Input:")
print(f"  Barang Terjual : {barang_terjual} unit")
print(f"  Permintaan     : {permintaan} unit")
print(f"  Harga per Item : Rp {harga_per_item:,}")
print(f"  Profit         : Rp {profit:,}")
print()

# ==========================================
# STEP 1: FUZZIFIKASI
# ==========================================
print("=" * 60)
print("STEP 1: FUZZIFIKASI")
print("=" * 60)

# --- Barang Terjual [0 - 100] ---
# Rendah: turun dari 0 ke 30 (1 di 0, 0 di 30)
# Sedang: segitiga (20, 50, 80)
# Tinggi: naik dari 60 ke 100 (0 di 60, 1 di 100)
def bt_rendah(x):
    if x <= 0: return 1.0
    elif x <= 30: return (30 - x) / 30
    else: return 0.0

def bt_sedang(x):
    if x <= 20: return 0.0
    elif x <= 50: return (x - 20) / 30
    elif x <= 80: return (80 - x) / 30
    else: return 0.0

def bt_tinggi(x):
    if x <= 60: return 0.0
    elif x <= 100: return (x - 60) / 40
    else: return 1.0

mu_bt_rendah = bt_rendah(barang_terjual)
mu_bt_sedang = bt_sedang(barang_terjual)
mu_bt_tinggi = bt_tinggi(barang_terjual)
print(f"Barang Terjual = {barang_terjual}")
print(f"  μ Rendah = {mu_bt_rendah:.4f}")
print(f"  μ Sedang = {mu_bt_sedang:.4f}")
print(f"  μ Tinggi = {mu_bt_tinggi:.4f}")
print()

# --- Permintaan [0 - 300] ---
# Rendah: turun 0→100 (1 di 0, 0 di 100)
# Sedang: segitiga (50, 150, 250)
# Tinggi: naik 200→300 (0 di 200, 1 di 300)
def p_rendah(x):
    if x <= 0: return 1.0
    elif x <= 100: return (100 - x) / 100
    else: return 0.0

def p_sedang(x):
    if x <= 50: return 0.0
    elif x <= 150: return (x - 50) / 100
    elif x <= 250: return (250 - x) / 100
    else: return 0.0

def p_tinggi(x):
    if x <= 200: return 0.0
    elif x <= 300: return (x - 200) / 100
    else: return 1.0

mu_p_rendah = p_rendah(permintaan)
mu_p_sedang = p_sedang(permintaan)
mu_p_tinggi = p_tinggi(permintaan)
print(f"Permintaan = {permintaan}")
print(f"  μ Rendah = {mu_p_rendah:.4f}")
print(f"  μ Sedang = {mu_p_sedang:.4f}")
print(f"  μ Tinggi = {mu_p_tinggi:.4f}")
print()

# --- Harga per Item [0 - 100000] ---
# Murah: turun 0→30000
# Sedang: segitiga (20000, 50000, 80000)
# Mahal: naik 70000→100000
def h_murah(x):
    if x <= 0: return 1.0
    elif x <= 30000: return (30000 - x) / 30000
    else: return 0.0

def h_sedang(x):
    if x <= 20000: return 0.0
    elif x <= 50000: return (x - 20000) / 30000
    elif x <= 80000: return (80000 - x) / 30000
    else: return 0.0

def h_mahal(x):
    if x <= 70000: return 0.0
    elif x <= 100000: return (x - 70000) / 30000
    else: return 1.0

mu_h_murah = h_murah(harga_per_item)
mu_h_sedang = h_sedang(harga_per_item)
mu_h_mahal = h_mahal(harga_per_item)
print(f"Harga per Item = Rp {harga_per_item:,}")
print(f"  μ Murah = {mu_h_murah:.4f}")
print(f"  μ Sedang = {mu_h_sedang:.4f}")
print(f"  μ Mahal = {mu_h_mahal:.4f}")
print()

# --- Profit [0 - 4000000] ---
# Rendah: turun 0→1500000
# Sedang: segitiga (1000000, 2000000, 3000000)
# Tinggi: naik 2500000→4000000
def pr_rendah(x):
    if x <= 0: return 1.0
    elif x <= 1500000: return (1500000 - x) / 1500000
    else: return 0.0

def pr_sedang(x):
    if x <= 1000000: return 0.0
    elif x <= 2000000: return (x - 1000000) / 1000000
    elif x <= 3000000: return (3000000 - x) / 1000000
    else: return 0.0

def pr_tinggi(x):
    if x <= 2500000: return 0.0
    elif x <= 4000000: return (x - 2500000) / 1500000
    else: return 1.0

mu_pr_rendah = pr_rendah(profit)
mu_pr_sedang = pr_sedang(profit)
mu_pr_tinggi = pr_tinggi(profit)
print(f"Profit = Rp {profit:,}")
print(f"  μ Rendah = {mu_pr_rendah:.4f}")
print(f"  μ Sedang = {mu_pr_sedang:.4f}")
print(f"  μ Tinggi = {mu_pr_tinggi:.4f}")
print()

# ==========================================
# STEP 2: EVALUASI ATURAN FUZZY (Inferensi)
# ==========================================
print("=" * 60)
print("STEP 2: EVALUASI ATURAN FUZZY (Inferensi Mamdani)")
print("=" * 60)

# Aturan 1: BT Tinggi AND P Tinggi AND H Murah AND Pr Tinggi → Stok Banyak
r1 = min(mu_bt_tinggi, mu_p_tinggi, mu_h_murah, mu_pr_tinggi)
print(f"Aturan 1: min({mu_bt_tinggi:.4f}, {mu_p_tinggi:.4f}, {mu_h_murah:.4f}, {mu_pr_tinggi:.4f}) = {r1:.4f} → Stok Banyak")

# Aturan 2: BT Tinggi AND P Tinggi AND H Murah AND Pr Sedang → Stok Sedang
r2 = min(mu_bt_tinggi, mu_p_tinggi, mu_h_murah, mu_pr_sedang)
print(f"Aturan 2: min({mu_bt_tinggi:.4f}, {mu_p_tinggi:.4f}, {mu_h_murah:.4f}, {mu_pr_sedang:.4f}) = {r2:.4f} → Stok Sedang")

# Aturan 3: BT Tinggi AND P Sedang AND H Murah AND Pr Sedang → Stok Sedang
r3 = min(mu_bt_tinggi, mu_p_sedang, mu_h_murah, mu_pr_sedang)
print(f"Aturan 3: min({mu_bt_tinggi:.4f}, {mu_p_sedang:.4f}, {mu_h_murah:.4f}, {mu_pr_sedang:.4f}) = {r3:.4f} → Stok Sedang")

# Aturan 4: BT Sedang AND P Tinggi AND H Murah AND Pr Sedang → Stok Sedang
r4 = min(mu_bt_sedang, mu_p_tinggi, mu_h_murah, mu_pr_sedang)
print(f"Aturan 4: min({mu_bt_sedang:.4f}, {mu_p_tinggi:.4f}, {mu_h_murah:.4f}, {mu_pr_sedang:.4f}) = {r4:.4f} → Stok Sedang")

# Aturan 5: BT Sedang AND P Tinggi AND H Murah AND Pr Tinggi → Stok Banyak
r5 = min(mu_bt_sedang, mu_p_tinggi, mu_h_murah, mu_pr_tinggi)
print(f"Aturan 5: min({mu_bt_sedang:.4f}, {mu_p_tinggi:.4f}, {mu_h_murah:.4f}, {mu_pr_tinggi:.4f}) = {r5:.4f} → Stok Banyak")

# Aturan 6: BT Rendah AND P Rendah AND H Sedang AND Pr Sedang → Stok Sedang
r6 = min(mu_bt_rendah, mu_p_rendah, mu_h_sedang, mu_pr_sedang)
print(f"Aturan 6: min({mu_bt_rendah:.4f}, {mu_p_rendah:.4f}, {mu_h_sedang:.4f}, {mu_pr_sedang:.4f}) = {r6:.4f} → Stok Sedang")
print()

# Agregasi: ambil max untuk setiap output
stok_sedang_alpha = max(r2, r3, r4, r6)
stok_banyak_alpha = max(r1, r5)
print(f"Agregasi Output:")
print(f"  α Stok Sedang = max({r2:.4f}, {r3:.4f}, {r4:.4f}, {r6:.4f}) = {stok_sedang_alpha:.4f}")
print(f"  α Stok Banyak = max({r1:.4f}, {r5:.4f}) = {stok_banyak_alpha:.4f}")
print()

# ==========================================
# STEP 3: DEFUZZIFIKASI (Centroid/COG)
# ==========================================
print("=" * 60)
print("STEP 3: DEFUZZIFIKASI (Centroid of Gravity)")
print("=" * 60)

# Stok Makanan [0 - 1000]
# Sedang: segitiga puncak di 500 (0→500→1000 dengan peak di 500, tapi lihat grafik:
#   dari grafik, Sedang tampak puncak di ~500, Banyak naik dari ~500 ke 1000)
# Estimasi dari grafik: Sedang sekitar (0, 500, 1000) atau (100,500,900)?
# Berdasarkan grafik yang menunjukkan 2 set: Sedang dan Banyak di [0-1000]
# Sedang: trapezoid/segitiga dari 0→200→600→800 atau sekitar puncak di 400-500
# Banyak: naik dari 600→1000
# Estimasi standar berdasarkan grafik yang terlihat:
# Sedang: puncak di 400 (0,0) -> (200,1) -> (600,1) -> (800,0) - trapezoid
# Banyak: (600,0) -> (1000,1) - shoulder

# Dari grafik yang terlihat di dokumen (Sedang puncak di tengah, Banyak shoulder kanan):
# Sedang: triangular (0, 500, 1000) -- simplified
# Banyak: shoulder (500, 1000)

# Sampling universe [0-1000]
x = np.linspace(0, 1000, 1001)

def stok_sedang_mf(x):
    if x <= 0: return 0.0
    elif x <= 500: return x / 500
    elif x <= 1000: return (1000 - x) / 500
    else: return 0.0

def stok_banyak_mf(x):
    if x <= 500: return 0.0
    elif x <= 1000: return (x - 500) / 500
    else: return 1.0

# Clipping dengan alpha cut
mu_sedang_clip = np.array([min(stok_sedang_mf(xi), stok_sedang_alpha) for xi in x])
mu_banyak_clip = np.array([min(stok_banyak_mf(xi), stok_banyak_alpha) for xi in x])

# Agregasi (union = max)
mu_agg = np.maximum(mu_sedang_clip, mu_banyak_clip)

# Defuzzifikasi COG
numerator = np.sum(x * mu_agg)
denominator = np.sum(mu_agg)

if denominator == 0:
    hasil = 0
else:
    hasil = numerator / denominator

print(f"Stok Makanan Sedang: α = {stok_sedang_alpha:.4f}")
print(f"Stok Makanan Banyak: α = {stok_banyak_alpha:.4f}")
print()
print(f"Defuzzifikasi COG:")
print(f"  Numerator  (∑ x·μ) = {numerator:.4f}")
print(f"  Denominator (∑ μ)  = {denominator:.4f}")
print()
print("=" * 60)
print(f"HASIL: Jumlah Stok Makanan = {hasil:.2f} unit")
print("=" * 60)