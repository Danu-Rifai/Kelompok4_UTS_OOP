from dokter  import Dokter, daftar_dokter
from hewan   import Hewan
from pemilik import Pemilik
from ruang   import Ruangan, daftar_ruangan

daftar_pemilik = {
    "P001": Pemilik("P001", "Rina Kartika",  "08111234567"),
    "P002": Pemilik("P002", "Doni Prasetyo", "08229876543"),
    "P003": Pemilik("P003", "Sari Indah",    "08551122334"),
}

daftar_hewan = {
    "H001": Hewan("Mochi",  "Kucing Persia", 3, "Demam ringan",    daftar_pemilik["P001"]),
    "H002": Hewan("Rocky",  "Anjing Husky",  5, "Luka di kaki",    daftar_pemilik["P002"]),
    "H003": Hewan("Kiwi",   "Burung Parkit", 1, "Bulu rontok",     daftar_pemilik["P001"]),
    "H004": Hewan("Bubbles","Ikan Mas",      2, "Infeksi jamur",   daftar_pemilik["P003"]),
}

# data dummy
daftar_pemilik["P001"].tambah_hewan(daftar_hewan["H001"])
daftar_pemilik["P001"].tambah_hewan(daftar_hewan["H003"])
daftar_pemilik["P002"].tambah_hewan(daftar_hewan["H002"])
daftar_pemilik["P003"].tambah_hewan(daftar_hewan["H004"])

daftar_ruangan["R01"].tambah_hewan(daftar_hewan["H001"])
daftar_ruangan["R02"].tambah_hewan(daftar_hewan["H002"])
daftar_ruangan["R03"].tambah_hewan(daftar_hewan["H003"])

TARIF_RAWAT_INAP_PER_HARI = 200_000

class Sistem:

    def __init__(self, dokter, hewan, pemilik, rawat_inap: bool = False, ruangan: Ruangan = None, lama_dirawat: int = 0):
        self.dokter       = dokter
        self.hewan        = hewan
        self.pemilik      = pemilik
        self.rawat_inap   = rawat_inap     
        self.ruangan      = ruangan      
        self.lama_dirawat = lama_dirawat  

    def hitung_total_tarif(self):
        total = self.dokter.tarif
        if self.rawat_inap:
            total += TARIF_RAWAT_INAP_PER_HARI * self.lama_dirawat
        return total

    def tampilkan_info_lengkap(self):
        total = self.hitung_total_tarif()
        print()
        print("=" * 40)
        print("      LAPORAN PERAWATAN HEWAN KLINIK")
        print("=" * 40)

        # Info hewan
        print(f"  Hewan       : {self.hewan.nama} ({self.hewan.jenis})")
        print(f"  Kondisi     : {self.hewan.kondisi}")
        print(f"  Umur        : {self.hewan.umur} tahun")

        # Info pemilik
        print(f"  Pemilik     : {self.pemilik.nama}")
        print(f"  Kontak      : {self.pemilik.kontak}")

        # Info dokter
        print(f"  Dokter      : {self.dokter.nama}")
        print(f"  Spesialisasi: {self.dokter.spesialisasi}")

        # Info perawatan
        jenis_rawat = "Rawat Inap" if self.rawat_inap else "Periksa (tanpa rawat inap)"
        print(f"  Jenis Rawat : {jenis_rawat}")
        if self.rawat_inap and self.ruangan:
            print(f"  Ruangan     : {self.ruangan.nama_ruang} ({self.ruangan.kode_ruang})")
            print(f"  Lama Rawat  : {self.lama_dirawat} hari")

        # Rincian biaya
        print("-" * 40)
        print("  RINCIAN BIAYA:")
        print(f"    Tarif Periksa : Rp {self.dokter.tarif:>10,}".replace(",", "."))
        if self.rawat_inap:
            biaya_inap = TARIF_RAWAT_INAP_PER_HARI * self.lama_dirawat
            print(f"    Biaya Rawat   : Rp {biaya_inap:>10,}".replace(",", "."))
            print(f"    ({self.lama_dirawat} hari × Rp {TARIF_RAWAT_INAP_PER_HARI:,})".replace(",", "."))
        print("-" * 40)
        print(f"    TOTAL         : Rp {total:>10,}".replace(",", "."))
        print("=" * 40)

def generate_id_pemilik():
    if not daftar_pemilik:
        return "P001"
    nomor_tertinggi = max(int(k[1:]) for k in daftar_pemilik.keys())
    return f"P{nomor_tertinggi + 1:03d}"

def generate_id_hewan():
    if not daftar_hewan:
        return "H001"
    nomor_tertinggi = max(int(k[1:]) for k in daftar_hewan.keys())
    return f"H{nomor_tertinggi + 1:03d}"

def cari_atau_buat_pemilik(nama_input: str, kontak_input: str):
    for pemilik in daftar_pemilik.values():
        if (pemilik.nama.strip().lower() == nama_input.strip().lower()
                and pemilik.kontak.strip() == kontak_input.strip()):
            print(f"  v  Pemilik sudah terdaftar -> menggunakan data [{pemilik.id}] {pemilik.nama}.")
            return pemilik

    # Tidak ditemukan -> buat baru
    id_baru = generate_id_pemilik()
    p_baru  = Pemilik(id_baru, nama_input.strip(), kontak_input.strip())
    daftar_pemilik[id_baru] = p_baru
    print(f"  v  Pemilik baru dibuat -> [{id_baru}] {p_baru.nama}.")
    return p_baru

def tambah_hewan_baru():
    print("\n  === TAMBAH HEWAN BARU ===")

    # Data hewan
    nama_hewan  = input("  Nama hewan    : ").strip()
    jenis_hewan = input("  Jenis hewan   : ").strip()
    while True:
        try:
            umur_hewan = int(input("  Umur (tahun)  : "))
            if umur_hewan >= 0:
                break
            print("  x Umur tidak boleh negatif.")
        except ValueError:
            print("  x Masukan harus berupa angka.")
    kondisi_hewan = input("  Kondisi hewan : ").strip()

    # Data pemilik
    print("\n  --- Data Pemilik ---")
    nama_pemilik   = input("  Nama pemilik  : ").strip()
    kontak_pemilik = input("  Kontak pemilik: ").strip()

    # Cari atau buat pemilik
    pemilik = cari_atau_buat_pemilik(nama_pemilik, kontak_pemilik)

    # -- Simpan hewan
    id_hewan   = generate_id_hewan()
    hewan_baru = Hewan(nama_hewan, jenis_hewan, umur_hewan, kondisi_hewan, pemilik)
    daftar_hewan[id_hewan] = hewan_baru
    pemilik.tambah_hewan(hewan_baru)

    print(f"\n  v  Hewan [{id_hewan}] '{nama_hewan}' berhasil didaftarkan!")
    print(f"     Pemilik : {pemilik.nama} [{pemilik.id}]")

def pilih_dari_daftar(daftar: dict, label: str):
    kunci_list = list(daftar.keys())
    print(f"\n  Daftar {label}:")
    for i, k in enumerate(kunci_list, 1):
        obj = daftar[k]
        # tampilkan nama jika ada atribut nama
        nama = getattr(obj, "nama", k)
        print(f"    {i}. [{k}] {nama}")

    while True:
        try:
            pilihan = int(input(f"  Pilih nomor {label}: "))
            if 1 <= pilihan <= len(kunci_list):
                return daftar[kunci_list[pilihan - 1]]
            print("  ✘ Nomor tidak valid, coba lagi.")
        except ValueError:
            print("  ✘ Masukan harus berupa angka.")


def main():
    print("\n  Selamat datang di Sistem Klinik Hewan 🐾")

    while True:
        print("""
╔══════════════════════════════════╗
║       MENU KLINIK HEWAN          ║
╠══════════════════════════════════╣
║  1. Tampilkan Info Dokter        ║
║  2. Tampilkan Info Pemilik       ║
║  3. Tampilkan Info Hewan         ║
║  4. Cek Kapasitas Ruangan        ║
║  5. Buat Laporan Perawatan       ║
║  6. Tambah Hewan Baru            ║
║  0. Keluar                       ║
╚══════════════════════════════════╝""")

        pilihan = input("  Masukkan pilihan: ").strip()

        # 1. Info Dokter
        if pilihan == "1":
            dokter = pilih_dari_daftar(daftar_dokter, "Dokter")
            dokter.tampilkan_info_dokter()

        # 2. Info Pemilik
        elif pilihan == "2":
            pemilik = pilih_dari_daftar(daftar_pemilik, "Pemilik")
            pemilik.tampilkan_info_pemilik()

        # 3. Info Hewan 
        elif pilihan == "3":
            hewan = pilih_dari_daftar(daftar_hewan, "Hewan")
            hewan.tampilkan_info_hewan()

        # 4. Cek Kapasitas Ruangan 
        elif pilihan == "4":
            ruangan = pilih_dari_daftar(daftar_ruangan, "Ruangan")
            ruangan.cek_kapasitas()

        # 5. Laporan Perawatan
        elif pilihan == "5":
            print("\n  === BUAT LAPORAN PERAWATAN ===")
            dokter  = pilih_dari_daftar(daftar_dokter, "Dokter")
            hewan   = pilih_dari_daftar(daftar_hewan,  "Hewan")
            pemilik = hewan.pemilik   # otomatis dari data hewan

            # Tanya: rawat inap atau tidak?
            print("\n  Jenis Perawatan:")
            print("    1. Periksa saja (tanpa rawat inap)")
            print("    2. Rawat inap")
            while True:
                jenis = input("  Pilih jenis perawatan (1/2): ").strip()
                if jenis in ("1", "2"):
                    break
                print("  ✘ Masukkan 1 atau 2.")

            if jenis == "1":
                sesi = Sistem(dokter, hewan, pemilik, rawat_inap=False)
            else:
                ruangan = pilih_dari_daftar(daftar_ruangan, "Ruangan")
                while True:
                    try:
                        lama = int(input("  Lama dirawat (hari): "))
                        if lama > 0:
                            break
                        print("  ✘ Lama rawat harus lebih dari 0.")
                    except ValueError:
                        print("  ✘ Masukan harus berupa angka.")
                sesi = Sistem(dokter, hewan, pemilik,
                              rawat_inap=True, ruangan=ruangan, lama_dirawat=lama)

            sesi.tampilkan_info_lengkap()

        # 6. Tambah Hewan Baru
        elif pilihan == "6":
            tambah_hewan_baru()
            
        elif pilihan == "0":
            print("\n  Terima kasih, sampai jumpa! 🐾\n")
            break

        else:
            print("  ✘ Pilihan tidak dikenal, silakan coba lagi.")


if __name__ == "__main__":
    main()
    