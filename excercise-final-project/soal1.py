## Buatlah sebuah program yang melakukan input sebuah bilangan n dimana n <= 100 dan kemudian tampilkan bilangan dari 1 hingga n yang habis dibagi 3 atau habis dibagi 7.
def cetak_kelipatan_3_atau_7(n):
    # Batasan sesuai soal: n <= 100
    if n > 100:
        print("Input tidak boleh lebih dari 100!")
        return
        
    print(f"Bilangan 1-{n} yang habis dibagi 3 atau 7:")
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 7 == 0:
            print(i, end=" ")
    print() # Membuat baris baru di akhir

# Uji Coba Fungsi
cetak_kelipatan_3_atau_7(25)