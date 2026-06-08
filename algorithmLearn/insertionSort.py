def insertion_sort(arr):
    # Dimulai dari indeks ke-1 (elemen kedua)
    for i in range(1, len(arr)):
        kunci = arr[i]
        j = i - 1
        
        # Geser elemen-elemen yang lebih besar dari 'kunci' ke arah kanan
        while j >= 0 and kunci < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        # Sisipkan 'kunci' ke posisi yang benar
        arr[j + 1] = kunci
    return arr

# Uji Coba
data = [64, 34, 25, 12, 22, 11, 90]
print("Insertion Sort :", insertion_sort(data))