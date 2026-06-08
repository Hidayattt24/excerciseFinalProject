def jenis_segitiga(sisi1, sisi2, sisi3):
    if (sisi1 + sisi2 <= sisi3) or (sisi1 + sisi3 <= sisi2) or (sisi2 + sisi3 <= sisi1):
        return "Bukan Segitiga Valid"
        
    if sisi1 == sisi2 == sisi3:
        return "Segitiga Sama Sisi"
    elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
        return "Segitiga Sama Kaki"
    else:
        return "Segitiga Sembarang"

print("Sisi 5, 5, 5:", jenis_segitiga(5, 5, 5))