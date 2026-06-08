def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Anggap elemen pertama di sisa array sebagai yang terkecil
        indeks_min = i
        
        # Cek sisa elemen di sebelah kanannya
        for j in range(i + 1, n):
            if arr[j] < arr[indeks_min]:
                indeks_min = j
                
        # Tukar elemen terkecil yang ditemukan dengan elemen di posisi i
        arr[i], arr[indeks_min] = arr[indeks_min], arr[i]
    return arr

# Uji Coba
data = [64, 34, 25, 12, 22, 11, 90]
print("Selection Sort :", selection_sort(data))