class Pemilik:
    def __init__(self, id, nama, kontak):
        self.id = id
        self.nama = nama
        self.kontak = kontak
        self.hewan_peliharaan = []  

    def tambah_hewan(self, hewan):
        """Daftarkan hewan ke pemilik ini."""
        self.hewan_peliharaan.append(hewan)

    def tampilkan_info_pemilik(self):
        print("=" * 35)
        print("         INFORMASI PEMILIK")
        print("=" * 35)
        print(f"  ID Pemilik : {self.id}")
        print(f"  Nama       : {self.nama}")
        print(f"  Kontak     : {self.kontak}")
        if self.hewan_peliharaan:
            print(f"  Hewan      : ", end="")
            print(", ".join(h.nama for h in self.hewan_peliharaan))
        else:
            print("  Hewan      : (belum ada)")
        print("=" * 35)
        