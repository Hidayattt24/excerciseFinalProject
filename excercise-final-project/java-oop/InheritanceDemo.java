// 1. Class Induk (Parent)
class Pengguna {
    String nama;
    String email;

    public void login() {
        System.out.println("🔑 " + this.nama + " berhasil masuk ke sistem.");
    }
}

// 2. Class Anak (Child) - Menggunakan keyword 'extends'
class KaderKesehatan extends Pengguna {
    public void inputDataBalita() {
        System.out.println("📝 " + this.nama + " sedang menginput data penimbangan balita.");
    }
}

public class InheritanceDemo {
    public static void main(String[] args) {
        // Objek anak otomatis mewarisi variabel 'nama' dan method 'login()' dari induknya
        KaderKesehatan kaderBudi = new KaderKesehatan();
        kaderBudi.nama = "Budi"; 
        
        kaderBudi.login();           // Memanggil fungsi warisan induk
        kaderBudi.inputDataBalita(); // Memanggil fungsi asli milik anak
    }
}