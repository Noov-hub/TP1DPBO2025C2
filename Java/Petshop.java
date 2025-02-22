// Kelas Petshop merepresentasikan produk yang dijual di petshop
class Petshop {
    // Deklarasi atribut private agar hanya bisa diakses melalui metode getter dan setter
    private String ID;
    private String namaProduk;
    private String kategori;
    private int harga;

    // Konstruktor default untuk menginisialisasi atribut dengan nilai awal
    public Petshop() {
        this.ID = "";
        this.namaProduk = "";
        this.kategori = "";
        this.harga = 0;
    }

    // Metode untuk mengatur data produk
    public void setData(String ID, String namaProduk, String kategori, int harga) {
        this.ID = ID;
        this.namaProduk = namaProduk;
        this.kategori = kategori;
        this.harga = harga;
    }

    // Metode untuk mereset data produk kembali ke nilai awal
    public void reset() {
        this.ID = "";
        this.namaProduk = "";
        this.kategori = "";
        this.harga = 0;
    }

    // Metode getter untuk mendapatkan nilai atribut private
    public String getID() { return ID; }
    public String getNamaProduk() { return namaProduk; }
    public String getKategori() { return kategori; }
    public int getHarga() { return harga; }
}
