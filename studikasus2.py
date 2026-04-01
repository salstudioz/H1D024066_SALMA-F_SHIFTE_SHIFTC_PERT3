import numpy as np

# =============================================
# STUDI KASUS 2 - LOGIKA FUZZY
# Pelayanan Masyarakat - Tingkat Kepuasan
# =============================================

# ------ INPUT ------
kejelasan_informasi = 80
kejelasan_persyaratan = 60
kemampuan_petugas = 50
ketersediaan_sarpras = 90

print("=" * 65)
print("STUDI KASUS 2 - KEPUASAN PELAYANAN MASYARAKAT (FUZZY)")
print("=" * 65)
print(f"Input:")
print(f"  Kejelasan Informasi    : {kejelasan_informasi}")
print(f"  Kejelasan Persyaratan  : {kejelasan_persyaratan}")
print(f"  Kemampuan Petugas      : {kemampuan_petugas}")
print(f"  Ketersediaan Sarpras   : {ketersediaan_sarpras}")
print()

# ==========================================
# Membership Functions Variabel Input
# Universe [0 - 100] untuk semua input
# Berdasarkan grafik:
#   Tidak Memuaskan : turun dari 0 ke 75 (puncak 0, nol di 75)
#   Cukup Memuaskan : segitiga (60, 75, 90)
#   Memuaskan       : naik dari 75 ke 100 (puncak 100)
# ==========================================

def mu_tidak(x):
    """Tidak Memuaskan: 1 di 0-60, turun ke 0 di 75"""
    if x <= 60: return 1.0
    elif x <= 75: return (75 - x) / 15
    else: return 0.0

def mu_cukup(x):
    """Cukup Memuaskan: segitiga puncak di 75 (60→75→90)"""
    if x <= 60: return 0.0
    elif x <= 75: return (x - 60) / 15
    elif x <= 90: return (90 - x) / 15
    else: return 0.0

def mu_memuaskan(x):
    """Memuaskan: naik dari 75 ke 90, plateau di 90+"""
    if x <= 75: return 0.0
    elif x <= 90: return (x - 75) / 15
    else: return 1.0

# ==========================================
# STEP 1: FUZZIFIKASI
# ==========================================
print("=" * 65)
print("STEP 1: FUZZIFIKASI")
print("=" * 65)

# Kejelasan Informasi = 80
ki = kejelasan_informasi
mu_ki_tidak    = mu_tidak(ki)
mu_ki_cukup    = mu_cukup(ki)
mu_ki_memuaskan = mu_memuaskan(ki)
print(f"Kejelasan Informasi = {ki}")
print(f"  μ Tidak Memuaskan  = {mu_ki_tidak:.4f}")
print(f"  μ Cukup Memuaskan  = {mu_ki_cukup:.4f}")
print(f"  μ Memuaskan        = {mu_ki_memuaskan:.4f}")
print()

# Kejelasan Persyaratan = 60
kp = kejelasan_persyaratan
mu_kp_tidak    = mu_tidak(kp)
mu_kp_cukup    = mu_cukup(kp)
mu_kp_memuaskan = mu_memuaskan(kp)
print(f"Kejelasan Persyaratan = {kp}")
print(f"  μ Tidak Memuaskan  = {mu_kp_tidak:.4f}")
print(f"  μ Cukup Memuaskan  = {mu_kp_cukup:.4f}")
print(f"  μ Memuaskan        = {mu_kp_memuaskan:.4f}")
print()

# Kemampuan Petugas = 50
km = kemampuan_petugas
mu_km_tidak    = mu_tidak(km)
mu_km_cukup    = mu_cukup(km)
mu_km_memuaskan = mu_memuaskan(km)
print(f"Kemampuan Petugas = {km}")
print(f"  μ Tidak Memuaskan  = {mu_km_tidak:.4f}")
print(f"  μ Cukup Memuaskan  = {mu_km_cukup:.4f}")
print(f"  μ Memuaskan        = {mu_km_memuaskan:.4f}")
print()

# Ketersediaan Sarpras = 90
ks = ketersediaan_sarpras
mu_ks_tidak    = mu_tidak(ks)
mu_ks_cukup    = mu_cukup(ks)
mu_ks_memuaskan = mu_memuaskan(ks)
print(f"Ketersediaan Sarpras = {ks}")
print(f"  μ Tidak Memuaskan  = {mu_ks_tidak:.4f}")
print(f"  μ Cukup Memuaskan  = {mu_ks_cukup:.4f}")
print(f"  μ Memuaskan        = {mu_ks_memuaskan:.4f}")
print()

# ==========================================
# STEP 2: EVALUASI ATURAN FUZZY
# ==========================================
print("=" * 65)
print("STEP 2: EVALUASI ATURAN FUZZY (Inferensi Mamdani)")
print("=" * 65)

# Aturan 1-13
rules = [
    # (KI, KP, KM, KS, output)
    (mu_ki_tidak,     mu_kp_tidak,     mu_km_tidak,     mu_ks_tidak,     "Tidak Memuaskan"),
    (mu_ki_tidak,     mu_kp_tidak,     mu_km_tidak,     mu_ks_cukup,     "Tidak Memuaskan"),
    (mu_ki_tidak,     mu_kp_tidak,     mu_km_tidak,     mu_ks_memuaskan, "Tidak Memuaskan"),
    (mu_ki_tidak,     mu_kp_tidak,     mu_km_cukup,     mu_ks_tidak,     "Tidak Memuaskan"),
    (mu_ki_tidak,     mu_kp_tidak,     mu_km_cukup,     mu_ks_cukup,     "Tidak Memuaskan"),
    (mu_ki_tidak,     mu_kp_tidak,     mu_km_cukup,     mu_ks_memuaskan, "Cukup Memuaskan"),
    (mu_ki_tidak,     mu_kp_tidak,     mu_km_memuaskan, mu_ks_tidak,     "Tidak Memuaskan"),
    (mu_ki_tidak,     mu_kp_tidak,     mu_km_memuaskan, mu_ks_cukup,     "Cukup Memuaskan"),
    (mu_ki_tidak,     mu_kp_tidak,     mu_km_memuaskan, mu_ks_memuaskan, "Cukup Memuaskan"),
    (mu_ki_cukup,     mu_kp_cukup,     mu_km_cukup,     mu_ks_memuaskan, "Memuaskan"),
    (mu_ki_cukup,     mu_kp_cukup,     mu_km_memuaskan, mu_ks_memuaskan, "Memuaskan"),
    (mu_ki_cukup,     mu_kp_memuaskan, mu_km_memuaskan, mu_ks_memuaskan, "Sangat Memuaskan"),
    (mu_ki_memuaskan, mu_kp_memuaskan, mu_km_memuaskan, mu_ks_memuaskan, "Sangat Memuaskan"),
]

alphas = {"Tidak Memuaskan": [], "Kurang Memuaskan": [], 
          "Cukup Memuaskan": [], "Memuaskan": [], "Sangat Memuaskan": []}

for i, (a, b, c, d, output) in enumerate(rules, 1):
    alpha = min(a, b, c, d)
    alphas[output].append(alpha)
    print(f"Aturan {i:2d}: min({a:.4f}, {b:.4f}, {c:.4f}, {d:.4f}) = {alpha:.4f} → {output}")

print()
print("Agregasi per Output:")
alpha_tidak   = max(alphas["Tidak Memuaskan"])   if alphas["Tidak Memuaskan"]   else 0
alpha_kurang  = max(alphas["Kurang Memuaskan"])  if alphas["Kurang Memuaskan"]  else 0
alpha_cukup   = max(alphas["Cukup Memuaskan"])   if alphas["Cukup Memuaskan"]   else 0
alpha_memuaskan = max(alphas["Memuaskan"])       if alphas["Memuaskan"]         else 0
alpha_sangat  = max(alphas["Sangat Memuaskan"])  if alphas["Sangat Memuaskan"]  else 0

print(f"  α Tidak Memuaskan  = {alpha_tidak:.4f}")
print(f"  α Kurang Memuaskan = {alpha_kurang:.4f}")
print(f"  α Cukup Memuaskan  = {alpha_cukup:.4f}")
print(f"  α Memuaskan        = {alpha_memuaskan:.4f}")
print(f"  α Sangat Memuaskan = {alpha_sangat:.4f}")
print()

# ==========================================
# STEP 3: DEFUZZIFIKASI (COG)
# ==========================================
print("=" * 65)
print("STEP 3: DEFUZZIFIKASI (Centroid of Gravity)")
print("=" * 65)

# Kepuasan Pelayanan [0 - 400] - 5 himpunan
# Dari grafik: Tidak (0-75), Kurang (50-150), Cukup (100-250), Memuaskan (200-350), Sangat (275-400)
# Estimasi segitiga:
# Tidak Memuaskan  : (0, 0, 75) → puncak di 0 turun ke 75
# Kurang Memuaskan : (50, 100, 150)
# Cukup Memuaskan  : (100, 175, 250)
# Memuaskan        : (250, 300, 350)  --> sekitar 275-350
# Sangat Memuaskan : (325, 400, 400)  --> puncak di 400

x = np.linspace(0, 400, 4001)

def kp_tidak(xi):
    if xi <= 0: return 1.0
    elif xi <= 75: return (75 - xi) / 75
    else: return 0.0

def kp_kurang(xi):
    if xi <= 50: return 0.0
    elif xi <= 100: return (xi - 50) / 50
    elif xi <= 150: return (150 - xi) / 50
    else: return 0.0

def kp_cukup(xi):
    if xi <= 100: return 0.0
    elif xi <= 175: return (xi - 100) / 75
    elif xi <= 250: return (250 - xi) / 75
    else: return 0.0

def kp_memuaskan(xi):
    if xi <= 250: return 0.0
    elif xi <= 300: return (xi - 250) / 50
    elif xi <= 350: return (350 - xi) / 50
    else: return 0.0

def kp_sangat(xi):
    if xi <= 325: return 0.0
    elif xi <= 400: return (xi - 325) / 75
    else: return 1.0

mu_agg = np.zeros(len(x))
for i, xi in enumerate(x):
    vals = [
        min(kp_tidak(xi), alpha_tidak),
        min(kp_kurang(xi), alpha_kurang),
        min(kp_cukup(xi), alpha_cukup),
        min(kp_memuaskan(xi), alpha_memuaskan),
        min(kp_sangat(xi), alpha_sangat),
    ]
    mu_agg[i] = max(vals)

numerator = np.sum(x * mu_agg)
denominator = np.sum(mu_agg)

if denominator == 0:
    hasil = 0
else:
    hasil = numerator / denominator

print(f"COG Numerator  (∑ x·μ) = {numerator:.4f}")
print(f"COG Denominator (∑ μ)  = {denominator:.4f}")
print()
print("=" * 65)
print(f"HASIL: Nilai Kepuasan Pelayanan = {hasil:.2f}")

# Interpretasi
if hasil < 75:
    label = "Tidak Memuaskan"
elif hasil < 150:
    label = "Kurang Memuaskan"
elif hasil < 250:
    label = "Cukup Memuaskan"
elif hasil < 325:
    label = "Memuaskan"
else:
    label = "Sangat Memuaskan"

print(f"Kategori              : {label}")
print("=" * 65)