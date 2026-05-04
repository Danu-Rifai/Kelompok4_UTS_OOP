class Hewan:
    def __init__(self, nama, jenis, umur, kondisi, pemilik):
        self.nama = nama
        self.jenis = jenis
        self.umur = umur
        self.kondisi = kondisi
        self.pemilik = pemilik 

    def tampilkan_info_hewan(self):
        print("=" * 35)
        print("       INFORMASI HEWAN PELIHARAAN")
        print("=" * 35)
        print(f"  Nama Hewan : {self.nama}")
        print(f"  Jenis      : {self.jenis}")
        print(f"  Umur       : {self.umur} tahun")
        print(f"  Kondisi    : {self.kondisi}")
        print(f"  Pemilik    : {self.pemilik.nama}")
        print("=" * 35)