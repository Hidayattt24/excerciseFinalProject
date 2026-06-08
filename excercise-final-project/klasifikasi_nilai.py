def klasifikasi_nilai(angka):
    if angka >= 85:
        return "A"
    elif angka >= 75:
        return "B"
    elif angka >= 60:
        return "C"
    elif angka >= 45:
        return "D"
    else:
        return "E"

print("Nilai 82:", klasifikasi_nilai(82))