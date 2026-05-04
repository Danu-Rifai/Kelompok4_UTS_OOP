class Hewan:
    def _init_(self, nama, jenis, umur, kondisi, pemilik):
        self.nama = nama
        self.jenis = jenis
        self.umur = umur
        self.kondisi = kondisi
        self.pemilik = pemilik

    def tampilkan_info_hewan(self):
        print("Nama Hewan :", self.nama)
        print("Jenis      :", self.jenis)
        print("Umur       :", self.umur)
        print("Kondisi    :", self.kondisi)
        print("Pemilik    :", self.pemilik.nama)