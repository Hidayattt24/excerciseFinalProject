def ke_huruf_besar(teks):
    hasil = ""
    
    for karakter in teks:
        # 1. Cek apakah karakter tersebut adalah huruf kecil (a sampai z)
        if 'a' <= karakter <= 'z':
            # ord() = mengambil angka ASCII dari huruf
            # chr() = mengubah angka ASCII kembali menjadi huruf
            angka_ascii = ord(karakter) - 32
            hasil += chr(angka_ascii)
        else:
            # Jika sudah huruf besar atau simbol, biarkan saja
            hasil += karakter
            
    return hasil

# Contoh Penggunaan saat demo:
print(ke_huruf_besar("dayat USK 2026"))  # Output: DAYAT USK 2026