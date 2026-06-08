def hitung_pecahan_uang(jumlah_uang):
    pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 100]
    hasil_pecahan = {}
    
    for uang in pecahan:
        if jumlah_uang >= uang:
            lembar = jumlah_uang // uang
            hasil_pecahan[uang] = lembar
            jumlah_uang = jumlah_uang % uang
            
    return hasil_pecahan

print("Pecahan 187500:", hitung_pecahan_uang(187500))