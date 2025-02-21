from Petshop import Petshop

data_petshop = []

def show_data():
    if not data_petshop:
        print("Data masih kosong. Silahkan isi.")
        return
    for pet in data_petshop:
        print("+----------------------------------+")
        for key, value in pet.get_data().items():
            print(f"{key} : {value}")
        print("+----------------------------------+")

def add_data():
    ID = input("ID: ")
    if any(pet.ID == ID for pet in data_petshop):
        print("ID sudah digunakan!")
        return
    namaProduk = input("Nama: ")
    kategori = input("Kategori: ")
    harga = int(input("Harga: "))
    data_petshop.append(Petshop(ID, namaProduk, kategori, harga))
    print("Data berhasil ditambahkan!")

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

def delete_data():
    ID = input("Masukkan ID data yang ingin dihapus: ")
    global data_petshop
    data_petshop = [pet for pet in data_petshop if pet.ID != ID]
    print("Data berhasil dihapus!")

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

if __name__ == "__main__":
    main()
