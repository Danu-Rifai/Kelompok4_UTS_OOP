class Ruangan:
    def __init__(self, kode_ruang, kapasitas_ruang, nama_ruang):
        self.kode_ruang = kode_ruang
        self.kapasitas_ruang = kapasitas_ruang
        self.nama_ruang = nama_ruang
        self.hewan_dirawat = []

    def tambah_hewan(self, hewan):
        if len(self.hewan_dirawat) < self.kapasitas_ruang:
            self.hewan_dirawat.append(hewan)
            print(f"{hewan.nama} masuk ke {self.nama_ruang}")
        else:
            print("Ruangan penuh!")

    def cek_kapasitas(self):
        print(f"{self.nama_ruang} ({len(self.hewan_dirawat)}/{self.kapasitas_ruang})")
        print("-" * 30)