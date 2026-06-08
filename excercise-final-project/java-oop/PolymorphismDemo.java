class Dokumen {
    public void cetakFormat() {
        System.out.println("Mencetak dokumen umum...");
    }
}

class DokumenPDF extends Dokumen {
    @Override // Menandakan fungsi ini menimpa/mengubah fungsi milik induk
    public void cetakFormat() {
        System.out.println("📄 Mencetak dokumen dalam bentuk format .pdf");
    }
}

class DokumenExcel extends Dokumen {
    @Override
    public void cetakFormat() {
        System.out.println("📊 Mencetak dokumen dalam bentuk tabel .xlsx");
    }
}

public class PolymorphismDemo {
    public static void main(String[] args) {
        // Membuat array bertipe induk 'Dokumen' yang menampung objek-objek anak yang berbeda
        Dokumen[] kumpulanFile = { new DokumenPDF(), new DokumenExcel() };

        // Dipanggil dengan nama fungsi yang sama, tapi hasilnya berbeda sesuai objeknya
        for (Dokumen file : kumpulanFile) {
            file.cetakFormat();
        }
    }
}