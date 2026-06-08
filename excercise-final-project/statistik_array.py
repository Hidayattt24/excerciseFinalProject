def statistik_array(arr):
    if len(arr) == 0: return 0, 0, 0
    nilai_min = arr[0]
    nilai_max = arr[0]
    total = 0
    
    for angka in arr:
        if angka < nilai_min: nilai_min = angka
        if angka > nilai_max: nilai_max = angka
        total += angka
        
    rata_rata = total / len(arr)
    return nilai_min, nilai_max, rata_rata

print("Statistik [5, 3, 9, 1]:", statistik_array([5, 3, 9, 1]))