class Karakter:
    def __init__(self, nama, hp, attack_power):
        # Atribut Objek
        self.nama = nama
        self.hp = hp
        self.attack_power = attack_power

    def serang(self, lawan):
        # Logika Interaksi: Mengurangi HP lawan berdasarkan attack power kita
        print(f"⚔️ {self.nama} menyerang {lawan.nama} sebesar {self.attack_power} damage!")
        lawan.hp -= self.attack_power
        
        # Logika Kondisional: Cek apakah lawan sudah mati
        if lawan.hp <= 0:
            lawan.hp = 0
            print(f"💀 {lawan.nama} telah dikalahkan!")
        else:
            print(f"❤️ HP {lawan.nama} tersisa: {lawan.hp}")

# --- UJI COBA DI PAPAN TULIS ---
# 1. Membuat Object dari Class Karakter
hero = Karakter("Dayat_Knight", hp=100, attack_power=30)
monster = Karakter("Goblin_Aceh", hp=70, attack_power=10)

# 2. Jalankan Logika Pertarungan sampai salah satu mati menggunakan While Loop
print("--- PERTARUNGAN DIMULAI ---")
while hero.hp > 0 and monster.hp > 0:
    hero.serang(monster)
    if monster.hp > 0:
        monster.serang(hero)
    print("-" * 30)