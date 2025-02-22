# JANJI
Saya Ibnu Fadhilah dengan NIM 2300613 mengerjakan Tugas Praktikum 1 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

# Desain OOP
Program terdiri dari satu class, yaitu "Petshop"dengan desain sebagai berikut:

Class "Petshop"
Class ini merepresentasikan sebuah produk di petshop dengan atribut sebagai berikut:

- ID (Private)
- namaProduk (Private)
- kategori (Private)
- harga (Private)

Class "Petshop" juga terdiri dari beberapa method:

- Constructor: Menginisialisasi atribut dengan nilai default kosong atau nol.
- setData: Mengubah nilai atribut dari objek (ID, namaProduk, kategori, harga).
- reset: Mengembalikan nilai atribut ke default (kosong atau nol).
- Getter Methods: (getID(), getNamaProduk(), getKategori(), getHarga()) untuk mengambil nilai atribut.

# Alur

## Inisialisasi dan Penyimpanan Data
   Java: Menggunakan ArrayList untuk menyimpan daftar produk.
  Python: Menggunakan list (data_petshop) untuk menyimpan produk dalam bentuk objek Petshop.
  PHP: Menggunakan session ($_SESSION['data_petshop']) untuk menyimpan produk selama sesi aktif.

## Menampilkan Menu dan Interaksi Pengguna
  Pada Java (Console-Based), Python (Console-Based), dan PHP (Web-Based), program menampilkan menu dengan pilihan:

  - 1 | Show
  - 2 | Add
  - 3 | Change
  - 4 | Delete
  - 5 | Search
  - 0 | Exit
  
  Java & Python: Menggunakan scanner/input untuk menerima pilihan dari pengguna.
  PHP: Menggunakan form HTML dan button submit untuk menangani input pengguna.
 Operasi CRUD (Create, Read, Update, Delete)
  ### Menampilkan Data Produk (Show)
    Java & Python: Menampilkan daftar produk dalam format teks dengan iterasi melalui list.
    PHP: Menampilkan data dalam bentuk tabel HTML, termasuk gambar produk.
 ### Menambahkan Produk Baru (Add)
    Pengguna memasukkan:
    ID Produk (harus unik)
    Nama Produk
    Kategori Produk
    Harga Produk
    *(PHP saja) Gambar Produk
    Jika ID sudah ada → tampilkan pesan kesalahan.
    Data produk disimpan ke dalam list (Java/Python) atau session (PHP).
 ### Mengubah Data Produk (Change)
    Pengguna memasukkan ID produk yang ingin diubah.
    Jika produk ditemukan → pengguna memasukkan data baru:
    Nama, Kategori, Harga, Gambar (PHP).
    Data diperbarui dalam list/session.
    Jika produk tidak ditemukan → tampilkan pesan kesalahan.
 ### Menghapus Produk (Delete)
    Pengguna memasukkan ID produk yang ingin dihapus.
    Jika ditemukan → produk dihapus dari list/session.
    PHP saja: Jika ada gambar terkait, file gambar juga dihapus.
### Mencari Produk (Search)
    Pengguna memasukkan ID produk yang ingin dicari.
    Jika ditemukan → tampilkan informasi produk.
    Jika tidak ditemukan → tampilkan pesan kesalahan.
## Menjalankan Program
  Java & Python:
    Program berjalan dalam loop while/do-while, meminta input hingga pengguna memilih 0 | Exit.
    Program menutup scanner/input saat keluar untuk mencegah kebocoran memori.
  PHP:
    Menggunakan form submission untuk menangani permintaan pengguna.
    Menampilkan data dalam bentuk tabel dinamis yang diperbarui secara langsung setelah perubahan.

# Dokumentasi Java
1. ![Screenshot 2025-02-23 003123](https://github.com/user-attachments/assets/e0a6ae59-4ede-4df5-9beb-8ec9dfad1ebb)
2. ![Screenshot 2025-02-23 003131](https://github.com/user-attachments/assets/6f78389c-9c55-42ba-a4b5-e43c1faad594)
3. ![Screenshot 2025-02-23 003137](https://github.com/user-attachments/assets/79741d49-021f-4d6d-a5d1-6248e1c36424)
4. ![Screenshot 2025-02-23 003143](https://github.com/user-attachments/assets/770143b7-2bbf-4d18-b63c-811b88a6aece)
5. ![Screenshot 2025-02-23 003153](https://github.com/user-attachments/assets/0085569b-2afa-4f38-9a52-0b934974ed83)
6. ![Screenshot 2025-02-23 003202](https://github.com/user-attachments/assets/adc94e89-129d-4cc8-bc67-94d130eaadb7)
7. ![Screenshot 2025-02-23 003211](https://github.com/user-attachments/assets/83269f4b-b575-4067-a5ec-b23ae8e8414d)
8. ![Screenshot 2025-02-23 003218](https://github.com/user-attachments/assets/c03b9eb4-8bc6-4d28-be23-ed2a369e72f7)
9. ![Screenshot 2025-02-23 003224](https://github.com/user-attachments/assets/5a64b3be-9404-447c-a197-b464a1785535)
10. ![Screenshot 2025-02-23 003228](https://github.com/user-attachments/assets/33eed2ab-ef00-4933-b246-751cd8d3673a)
11. ![Screenshot 2025-02-23 003924](https://github.com/user-attachments/assets/ffd4595b-29e2-4a7b-bada-fa50e153af16)



# Dokumentasi Python
1. ![Screenshot 2025-02-23 003615](https://github.com/user-attachments/assets/d449f992-35e6-43fb-aa62-23582787cb03)
2. ![Screenshot 2025-02-23 003622](https://github.com/user-attachments/assets/9625a428-6385-4149-ad06-917b2b985a21)
3. ![Screenshot 2025-02-23 003632](https://github.com/user-attachments/assets/0e0e690d-d967-4cbe-9537-cc30b121ff6d)
4. ![Screenshot 2025-02-23 003639](https://github.com/user-attachments/assets/096a821b-7abf-4263-8f86-9717974513f9)
5. ![Screenshot 2025-02-23 003643](https://github.com/user-attachments/assets/69d5bf98-9066-48af-9cb3-fa7912876b37)
6. ![Screenshot 2025-02-23 003648](https://github.com/user-attachments/assets/ff40ebfc-7bcc-426d-9355-acd039d661c4)
7. ![Screenshot 2025-02-23 003658](https://github.com/user-attachments/assets/e02c90f6-8e5d-46af-9aee-eb2b2e37a803)
8. ![Screenshot 2025-02-23 003809](https://github.com/user-attachments/assets/e24aef81-5732-4ce1-9b57-eb84b8a0e5de)



# Dokumentasi PHP
1. ![Screenshot 2025-02-23 004147](https://github.com/user-attachments/assets/8fc414f6-f785-42f2-8ee6-97613a5ef383)
2. ![Screenshot 2025-02-23 004151](https://github.com/user-attachments/assets/cbee71f4-04e5-4207-8776-ec2af8e5993b)
3. ![Screenshot 2025-02-23 004222](https://github.com/user-attachments/assets/1f2e96e0-de8a-4b1b-b2d9-152b9ba4bbe0)
4. ![Screenshot 2025-02-23 004228](https://github.com/user-attachments/assets/e5af5eca-ea8c-411b-b8b7-639f0d60df8a)
5. ![Screenshot 2025-02-23 004252](https://github.com/user-attachments/assets/7720f055-ecb5-4242-95e6-70dd7ebe7c7c)
6. ![Screenshot 2025-02-23 004304](https://github.com/user-attachments/assets/3cd03fab-839e-4547-b86b-d7422bc1ca0f)
7. ![Screenshot 2025-02-23 004322](https://github.com/user-attachments/assets/84e9d66b-4f1b-4379-8e36-b2e07ade45de)
8. ![Screenshot 2025-02-23 004328](https://github.com/user-attachments/assets/5a89aee2-cb6d-4a4e-95c2-b80eafea8245)
9. ![Screenshot 2025-02-23 004437](https://github.com/user-attachments/assets/06f77f58-5241-436a-ac1c-b8a56bc87f74)

