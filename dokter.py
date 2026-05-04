class Dokter:
    def __init__(self, nama, spesialisasi, tarif):
        self.nama = nama
        self.spesialisasi = spesialisasi
        self.tarif = tarif

    def tampilkan_info_dokter(self):
        print("=" * 35)
        print("         INFORMASI DOKTER")
        print("=" * 35)
        print(f"  Nama Dokter  : {self.nama}")
        print(f"  Spesialisasi : {self.spesialisasi}")
        print(f"  Tarif Periksa: Rp {self.tarif:,}".replace(",", "."))
        print("=" * 35)

daftar_dokter = {
    "Dr. Ani Susanti" : Dokter("Dr. Ani Susanti",  "Kulit & Bulu",  150_000),
    "Dr. Budi Santoso": Dokter("Dr. Budi Santoso", "Bedah Hewan",   200_000),
    "Dr. Citra Dewi"  : Dokter("Dr. Citra Dewi",   "Gigi & Mulut",  120_000),
}
