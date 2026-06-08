def apakah_kabisat(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    return False

def jumlah_hari_per_bulan(bulan, tahun):
    hari_normal = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if bulan == 2 and apakah_kabisat(tahun):
        return 29
    return hari_normal[bulan]

print("Hari Februari 2024:", jumlah_hari_per_bulan(2, 2024))