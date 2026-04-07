import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from itertools import product

# ==================== 1. Definisi Variabel ====================
kejelasan_informasi = ctrl.Antecedent(np.arange(0, 101, 1), 'kejelasan_informasi')
kejelasan_persyaratan = ctrl.Antecedent(np.arange(0, 101, 1), 'kejelasan_persyaratan')
kemampuan_petugas = ctrl.Antecedent(np.arange(0, 101, 1), 'kemampuan_petugas')
ketersediaan_sarpras = ctrl.Antecedent(np.arange(0, 101, 1), 'ketersediaan_sarpras')
kepuasan_pelayanan = ctrl.Consequent(np.arange(0, 401, 1), 'kepuasan_pelayanan')

# ==================== 2. Fungsi Keanggotaan Input (sama untuk semua) ====================
for var in [kejelasan_informasi, kejelasan_persyaratan, kemampuan_petugas, ketersediaan_sarpras]:
    var['tidak_memuaskan'] = fuzz.trapmf(var.universe, [0, 0, 60, 75])
    var['cukup_memuaskan'] = fuzz.trimf(var.universe, [60, 75, 90])
    var['memuaskan'] = fuzz.trapmf(var.universe, [75, 90, 100, 100])

# ==================== 3. Fungsi Keanggotaan Output ====================
kepuasan_pelayanan['tidak_memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [0, 0, 50, 75])
kepuasan_pelayanan['kurang_memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [50, 75, 100, 150])
kepuasan_pelayanan['cukup_memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [100, 150, 250, 275])
kepuasan_pelayanan['memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [250, 275, 325, 350])
kepuasan_pelayanan['sangat_memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [325, 350, 400, 400])

# ==================== 4. Pembangkitan 81 Aturan Secara Sistematis ====================
# Pemetaan level: 0 = tidak_memuaskan, 1 = cukup_memuaskan, 2 = memuaskan
level_to_name = {0: 'tidak_memuaskan', 1: 'cukup_memuaskan', 2: 'memuaskan'}
output_map = {
    0: 'tidak_memuaskan',   # skor total 0-2 -> tidak memuaskan
    1: 'tidak_memuaskan',
    2: 'tidak_memuaskan',
    3: 'cukup_memuaskan',   # 3-4 -> cukup memuaskan
    4: 'cukup_memuaskan',
    5: 'memuaskan',         # 5-6 -> memuaskan
    6: 'memuaskan',
    7: 'sangat_memuaskan',  # 7-8 -> sangat memuaskan
    8: 'sangat_memuaskan'
}

rules = []
for (a,b,c,d) in product([0,1,2], repeat=4):
    # a: kejelasan_informasi, b: kejelasan_persyaratan, c: kemampuan_petugas, d: ketersediaan_sarpras
    total = a + b + c + d
    konsekuen = output_map[total]
    
    antecedent = (kejelasan_informasi[level_to_name[a]] &
                  kejelasan_persyaratan[level_to_name[b]] &
                  kemampuan_petugas[level_to_name[c]] &
                  ketersediaan_sarpras[level_to_name[d]])
    rule = ctrl.Rule(antecedent, kepuasan_pelayanan[konsekuen])
    rules.append(rule)

print(f'Jumlah aturan yang dibangkitkan: {len(rules)}')  # Harus 81

# ==================== 5. Sistem Kontrol dan Simulasi ====================
kepuasan_ctrl = ctrl.ControlSystem(rules)
kepuasan_sim = ctrl.ControlSystemSimulation(kepuasan_ctrl)

# Data uji
kepuasan_sim.input['kejelasan_informasi'] = 80
kepuasan_sim.input['kejelasan_persyaratan'] = 60
kepuasan_sim.input['kemampuan_petugas'] = 50
kepuasan_sim.input['ketersediaan_sarpras'] = 90

try:
    kepuasan_sim.compute()
    hasil_kepuasan = kepuasan_sim.output['kepuasan_pelayanan']
    print(f'\n=== STUDI KASUS 2: Evaluasi Kepuasan Pelayanan ===')
    print(f'Tingkat Kepuasan Pelayanan: {hasil_kepuasan:.2f} (skala 0-400)')
    
    # Interpretasi
    if hasil_kepuasan <= 75:
        kategori = "Tidak Memuaskan"
    elif hasil_kepuasan <= 150:
        kategori = "Kurang Memuaskan"
    elif hasil_kepuasan <= 275:
        kategori = "Cukup Memuaskan"
    elif hasil_kepuasan <= 350:
        kategori = "Memuaskan"
    else:
        kategori = "Sangat Memuaskan"
    print(f'Kategori: {kategori}')
    
except ValueError as e:
    print(f'Error saat komputasi: {e}')

# ==================== 6. Visualisasi Output ====================
kepuasan_pelayanan.view(sim=kepuasan_sim)
plt.title('Hasil Defuzzifikasi Kepuasan Pelayanan')
plt.show()