class Petshop {
    private String ID;
    private String namaProduk;
    private String kategori;
    private int harga;

    public Petshop() {
        this.ID = "";
        this.namaProduk = "";
        this.kategori = "";
        this.harga = 0;
    }

    public void setData(String ID, String namaProduk, String kategori, int harga) {
        this.ID = ID;
        this.namaProduk = namaProduk;
        this.kategori = kategori;
        this.harga = harga;
    }

    public void reset() {
        this.ID = "";
        this.namaProduk = "";
        this.kategori = "";
        this.harga = 0;
    }

    public String getID() { return ID; }
    public String getNamaProduk() { return namaProduk; }
    public String getKategori() { return kategori; }
    public int getHarga() { return harga; }
}
