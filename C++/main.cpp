#include <iostream>
#include <string>
#include "Petshop.cpp"

using namespace std;

void showData(Petshop DataPetshop[], int n) {
    bool kosong = true;
    for (int i = 0; i < n; i++) {
        if (!DataPetshop[i].getID().empty()) {
            cout << "+----------------------------------+\n";
            cout << "ID             : " << DataPetshop[i].getID() << "\n";
            cout << "Nama Produk    : " << DataPetshop[i].getNamaProduk() << "\n";
            cout << "Kategori       : " << DataPetshop[i].getKategori() << "\n";
            cout << "Harga          : " << DataPetshop[i].getHarga() << "\n";
            cout << "+----------------------------------+\n";
            kosong = false;
        }
    }
    if (kosong) cout << "Data masih kosong. Silahkan isi.\n";
}

void addData(Petshop DataPetshop[], int &data, int n) {
    if (data >= n) {
        cout << "Data sudah penuh!\n";
        return;
    }
    string ID, namaProduk, kategori;
    int harga;

    cout << "ID: "; cin >> ID;
    for (int i = 0; i < data; i++) {
        if (DataPetshop[i].getID() == ID) {
            cout << "ID sudah digunakan!\n";
            return;
        }
    }
    cout << "Nama: "; cin >> namaProduk;
    cout << "Kategori: "; cin >> kategori;
    cout << "Harga: "; cin >> harga;
    
    DataPetshop[data].setData(ID, namaProduk, kategori, harga);
    data++;
    cout << "Data berhasil ditambahkan!\n";
}

void changeData(Petshop DataPetshop[], int data) {
    string ID;
    cout << "Masukkan ID data yang ingin diubah: "; cin >> ID;
    for (int i = 0; i < data; i++) {
        if (DataPetshop[i].getID() == ID) {
            string namaProduk, kategori;
            int harga;
            cout << "Nama baru: "; cin >> namaProduk;
            cout << "Kategori baru: "; cin >> kategori;
            cout << "Harga baru: "; cin >> harga;
            DataPetshop[i].setData(ID, namaProduk, kategori, harga);
            cout << "Data berhasil diubah!\n";
            return;
        }
    }
    cout << "Produk dengan ID " << ID << " tidak ditemukan!\n";
}

void deleteData(Petshop DataPetshop[], int &data) {
    string ID;
    cout << "Masukkan ID data yang ingin dihapus: "; cin >> ID;
    for (int i = 0; i < data; i++) {
        if (DataPetshop[i].getID() == ID) {
            for (int j = i; j < data - 1; j++) {
                DataPetshop[j] = DataPetshop[j + 1];
            }
            DataPetshop[data - 1].reset();
            data--;
            cout << "Data berhasil dihapus!\n";
            return;
        }
    }
    cout << "Produk dengan ID " << ID << " tidak ditemukan!\n";
}

void searchData(Petshop DataPetshop[], int data) {
    string ID;
    cout << "Masukkan ID data yang ingin dicari: "; cin >> ID;
    for (int i = 0; i < data; i++) {
        if (DataPetshop[i].getID() == ID) {
            cout << "+----------------------------------+\n";
            cout << "ID             : " << DataPetshop[i].getID() << "\n";
            cout << "Nama Produk    : " << DataPetshop[i].getNamaProduk() << "\n";
            cout << "Kategori       : " << DataPetshop[i].getKategori() << "\n";
            cout << "Harga          : " << DataPetshop[i].getHarga() << "\n";
            cout << "+----------------------------------+\n";
            return;
        }
    }
    cout << "Produk dengan ID " << ID << " tidak ditemukan!\n";
}

int main() {
    int n;
    cout << "Welcome To Noov Petshop\n";
    cout << "Infokan berapa Data yang ingin dimasukkan banh: "; cin >> n;
    Petshop DataPetshop[n];
    int pilihan, data = 0;

    do {
        cout << "1 | Show\n2 | Add\n3 | Change\n4 | Delete\n5 | Search\n0 | Exit\n";
        cout << "Pilih Menu: "; cin >> pilihan;
        switch (pilihan) {
            case 1: showData(DataPetshop, n); break;
            case 2: addData(DataPetshop, data, n); break;
            case 3: changeData(DataPetshop, data); break;
            case 4: deleteData(DataPetshop, data); break;
            case 5: searchData(DataPetshop, data); break;
            case 0: cout << "Thank You!\n"; break;
            default: cout << "Pilihan tidak valid!\n";
        }
    } while (pilihan != 0);
    return 0;
}
