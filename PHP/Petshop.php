<?php
    // Memulai sesi untuk menyimpan data sementara
    session_start();
    if (!isset($_SESSION['data_petshop'])) {
        $_SESSION['data_petshop'] = [];
    }

    // Kelas Petshop untuk merepresentasikan produk
    class Petshop {
        private $ID;
        private $namaProduk;
        private $kategori;
        private $harga;
        private $gambar;

        // Konstruktor untuk menginisialisasi atribut
        public function __construct($ID, $namaProduk, $kategori, $harga, $gambar) {
            $this->ID = $ID;
            $this->namaProduk = $namaProduk;
            $this->kategori = $kategori;
            $this->harga = $harga;
            $this->gambar = $gambar;
        }

        // Getter untuk mengambil nilai atribut
        public function getID() {
            return $this->ID;
        }

        public function getNamaProduk() {
            return $this->namaProduk;
        }

        public function getKategori() {
            return $this->kategori;
        }

        public function getHarga() {
            return $this->harga;
        }

        public function getGambar() {
            return $this->gambar;
        }
    }

?>
