from Petshop import Petshop  # Mengimpor kelas Petshop dari file Petshop.py

data_petshop = []  # List untuk menyimpan data produk petshop

# Fungsi untuk menampilkan semua data produk

def show_data():
    if not data_petshop:
        print("Data masih kosong. Silahkan isi.")
        return
    for pet in data_petshop:
        print("+----------------------------------+")
        for key, value in pet.get_data().items():
            print(f"{key} : {value}")
        print("+----------------------------------+")

# Fungsi untuk menambahkan data produk baru

def add_data():
    ID = input("ID: ")
    if any(pet.ID == ID for pet in data_petshop):  # Cek apakah ID sudah digunakan
        print("ID sudah digunakan!")
        return
    namaProduk = input("Nama: ")
    kategori = input("Kategori: ")
    harga = int(input("Harga: "))
    data_petshop.append(Petshop(ID, namaProduk, kategori, harga))  # Tambah objek Petshop ke list
    print("Data berhasil ditambahkan!")

# Fungsi untuk mengubah data produk berdasarkan ID

def change_data():
    ID = input("Masukkan ID data yang ingin diubah: ")
    for pet in data_petshop:
        if pet.ID == ID:
            pet.namaProduk = input("Nama baru: ")
            pet.kategori = input("Kategori baru: ")
            pet.harga = int(input("Harga baru: "))
            print("Data berhasil diubah!")
            return
    print(f"Produk dengan ID {ID} tidak ditemukan!")

# Fungsi untuk menghapus data produk berdasarkan ID

def delete_data():
    ID = input("Masukkan ID data yang ingin dihapus: ")
    global data_petshop
    data_petshop = [pet for pet in data_petshop if pet.ID != ID]  # Filter list untuk menghapus produk
    print("Data berhasil dihapus!")

# Fungsi untuk mencari data produk berdasarkan ID

def search_data():
    ID = input("Masukkan ID data yang ingin dicari: ")
    for pet in data_petshop:
        if pet.ID == ID:
            print("+----------------------------------+")
            for key, value in pet.get_data().items():
                print(f"{key} : {value}")
            print("+----------------------------------+")
            return
    print(f"Produk dengan ID {ID} tidak ditemukan!")

# Fungsi utama untuk menjalankan program

def main():
    print("Welcome To Noov Petshop")
    while True:
        print("1 | Show\n2 | Add\n3 | Change\n4 | Delete\n5 | Search\n0 | Exit")
        pilihan = input("Pilih Menu: ")
        if pilihan == "1":
            show_data()
        elif pilihan == "2":
            add_data()
        elif pilihan == "3":
            change_data()
        elif pilihan == "4":
            delete_data()
        elif pilihan == "5":
            search_data()
        elif pilihan == "0":
            print("Thank You!")
            break
        else:
            print("Pilihan tidak valid!")

# Menjalankan program jika file ini dieksekusi secara langsung
if __name__ == "__main__":
    main()
