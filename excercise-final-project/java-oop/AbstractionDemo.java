// Class Abstrak tidak bisa di-instansiasi (dibuat jadi objek) langsung
abstract class MesinKopi {
    // Method abstrak tanpa isi body {}, wajib diisi detailnya oleh class anak
    public abstract void buatKopi(); 
}

// Class riil yang menerapkan/mengimplementasikan kontrak abstraksi
class MesinKopiOtomatis extends MesinKopi {
    @Override
    public void buatKopi() {
        // Detail internal sensor dan mekanik mesin disembunyikan dari user
        System.out.println("☕ Kopi Espresso hangat Anda sudah siap disajikan!");
    }
}

public class AbstractionDemo {
    public static void main(String[] args) {
        // MesinKopi mesin = new MesinKopi(); // ERROR! Java melarang membuat objek dari class abstract
        
        MesinKopi mKopi = new MesinKopiOtomatis();
        mKopi.buatKopi(); // User langsung pakai tanpa tahu kerumitan sistem di dalamnya
    }
}