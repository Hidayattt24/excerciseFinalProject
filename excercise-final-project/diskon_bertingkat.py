def hitung_diskon(total_belanja):
    if total_belanja >= 1000000:
        persen_diskon = 15
    elif total_belanja >= 500000:
        persen_diskon = 10
    elif total_belanja >= 200000:
        persen_diskon = 5
    else:
        persen_diskon = 0
        
    potongan = total_belanja * (persen_diskon / 100)
    total_bayar = total_belanja - potongan
    return total_bayar, potongan

total, hemat = hitung_diskon(600000)
print(f"Bayar: {total}, Potongan: {hemat}")