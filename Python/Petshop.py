class Petshop:
    # Konstruktor untuk inisialisasi atribut produk petshop
    def __init__(self, ID="", namaProduk="", kategori="", harga=0):
        self.ID = ID  # ID produk
        self.namaProduk = namaProduk  # Nama produk
        self.kategori = kategori  # Kategori produk
        self.harga = harga if harga >= 0 else 0  # Harga produk, tidak boleh negatif

    # Metode untuk mengubah data produk
    def set_data(self, ID, namaProduk, kategori, harga):
        self.ID = ID
        self.namaProduk = namaProduk
        self.kategori = kategori
        self.harga = harga if harga >= 0 else 0

    # Metode untuk mereset atribut ke nilai default
    def reset(self):
        self.ID = ""
        self.namaProduk = ""
        self.kategori = ""
        self.harga = 0

    # Metode untuk mendapatkan data dalam bentuk dictionary
    def get_data(self):
        return {
            "ID": self.ID,
            "Nama Produk": self.namaProduk,
            "Kategori": self.kategori,
            "Harga": self.harga,
        }
    
    # Metode untuk menampilkan representasi string objek
    def __str__(self):
        return f"Petshop(ID={self.ID}, Nama={self.namaProduk}, Kategori={self.kategori}, Harga={self.harga})"
    
    # Metode untuk representasi debugging
    def __repr__(self):
        return self.__str__()
