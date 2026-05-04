class Pemilik(Id, nama, kontak, hewan_peliharaan=[]):
    def __init__(self, id, nama, kontak):
        self.id = id
        self.nama = nama
        self.kontak = kontak
        self.hewan_peliharaan = []
        
    def tampilkan_info_pemilik(self):
        print(self.id, self.nama, self.kontak)