class Ruangan:
    def __init__(self, kode_ruang, kapasitas_ruang, nama_ruang):
        self.kode_ruang      = kode_ruang
        self.kapasitas_ruang = kapasitas_ruang
        self.nama_ruang      = nama_ruang
        self.hewan_dirawat   = []

    def tambah_hewan(self, hewan):
        """Masukkan hewan ke ruangan jika masih ada kapasitas."""
        if len(self.hewan_dirawat) < self.kapasitas_ruang:
            self.hewan_dirawat.append(hewan)
            print(f"  ✔  {hewan.nama} berhasil masuk ke {self.nama_ruang}.")
        else:
            print(f"  ✘  Ruangan '{self.nama_ruang}' penuh! Kapasitas: {self.kapasitas_ruang}.")

    def cek_kapasitas(self):
        print("=" * 35)
        print("         INFORMASI RUANGAN")
        print("=" * 35)
        print(f"  Kode Ruang : {self.kode_ruang}")
        print(f"  Nama Ruang : {self.nama_ruang}")
        print(f"  Kapasitas  : {len(self.hewan_dirawat)}/{self.kapasitas_ruang}")
        if self.hewan_dirawat:
            print(f"  Hewan      : ", end="")
            print(", ".join(h.nama for h in self.hewan_dirawat))
        print("=" * 35)


# Data dummy ruangan
daftar_ruangan = {
    "R01": Ruangan("R01", 3, "Ruang Rawat Umum"),
    "R02": Ruangan("R02", 2, "Ruang Rawat VIP"),
    "R03": Ruangan("R03", 1, "Ruang ICU Hewan"),
}
