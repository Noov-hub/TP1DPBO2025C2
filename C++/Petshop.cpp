#include <iostream>
#include <string>
using namespace std;

class Petshop {
private:
    string ID;
    string namaProduk;
    string kategori;
    int harga;

public:
    // Constructor
    Petshop() : ID(""), namaProduk(""), kategori(""), harga(0) {}
    
    // Setter
    void setData(string id, string nama, string kat, int hrg) {
        ID = id;
        namaProduk = nama;
        kategori = kat;
        harga = hrg;
    }
    
    void reset() {
        ID = "";
        namaProduk = "";
        kategori = "";
        harga = 0;
    }
    
    // Getter
    string getID() { return ID; }
    string getNamaProduk() { return namaProduk; }
    string getKategori() { return kategori; }
    int getHarga() { return harga; }

        //Destructor
        ~Petshop(){}
};