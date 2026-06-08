def bubble_sort(arr):
    n = len(arr)
    # Perulangan untuk seluruh elemen array
    for i in range(n):
        # Elemen terakhir sudah pasti di posisi yang benar, jadi batas kanan berkurang (-i-1)
        for j in range(0, n - i - 1):
            # Jika angka sebelah kiri lebih besar dari sebelah kanan
            if arr[j] > arr[j + 1]:
                # Tukar posisi datanya
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Uji Coba
data = [64, 34, 25, 12, 22, 11, 90]
print("Bubble Sort    :", bubble_sort(data))