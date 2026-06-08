class DompetDigital {
    public String pemilik;
    private double saldo; // PRIVATE: Dikunci agar tidak bisa diakses dari luar

    // Constructor untuk inisialisasi data awal
    public DompetDigital(String pemilik, double saldoAwal) {
        this.pemilik = pemilik;
        this.saldo = saldoAwal;
    }

    // GETTER: Fungsi untuk melihat saldo secara aman
    public double getSaldo() {
        return this.saldo;
    }

    // SETTER: Fungsi untuk mengubah saldo dengan LOGIKA VALIDASI
    public void isiSaldo(double jumlah) {
        if (jumlah > 0) {
            this.saldo += jumlah;
            System.out.println("💰 Berhasil top up Rp " + jumlah);
        } else {
            System.out.println("❌ Jumlah top up harus lebih dari 0!");
        }
    }
}

public class EncapsulationDemo {
    public static void main(String[] args) {
        DompetDigital dompet = new DompetDigital("Dayat", 50000);

        // System.out.println(dompet.saldo); // ERROR! Java akan menolak karena saldo bersifat private
        
        System.out.println("Saldo awal : " + dompet.getSaldo()); // Akses lewat Getter
        dompet.isiSaldo(25000);                                  // Ubah lewat Setter
        System.out.println("Saldo akhir: " + dompet.getSaldo());
    }
}