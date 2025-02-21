class Petshop:
    def __init__(self, ID="", namaProduk="", kategori="", harga=0):
        self.ID = ID
        self.namaProduk = namaProduk
        self.kategori = kategori
        self.harga = harga

    def set_data(self, ID, namaProduk, kategori, harga):
        self.ID = ID
        self.namaProduk = namaProduk
        self.kategori = kategori
        self.harga = harga

    def reset(self):
        self.__init__()

    def get_data(self):
        return {
            "ID": self.ID,
            "Nama Produk": self.namaProduk,
            "Kategori": self.kategori,
            "Harga": self.harga,
        }