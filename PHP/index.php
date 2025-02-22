
<?php
    include_once("Petshop.php");
    // Memproses input dari form
    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        if (isset($_POST['add'])) { // Menambah data baru
            $gambarPath = "img/" . $_POST['ID'] . ".jpg";
            move_uploaded_file($_FILES['gambar']['tmp_name'], $gambarPath);
            
            $data = new Petshop($_POST['ID'], $_POST['namaProduk'], $_POST['kategori'], $_POST['harga'], $gambarPath);
            $_SESSION['data_petshop'][] = $data;
        } elseif (isset($_POST['delete'])) { // Menghapus data berdasarkan ID
            foreach ($_SESSION['data_petshop'] as $key => $pet) {
                if ($pet->getID() == $_POST['ID']) {
                    unlink($pet->getGambar()); // Menghapus file gambar
                    unset($_SESSION['data_petshop'][$key]); // Menghapus data dari session
                    break;
                }
            }
        } elseif (isset($_POST['edit'])) { // Mengedit data yang sudah ada
            foreach ($_SESSION['data_petshop'] as $key => $pet) {
                if ($pet->getID() == $_POST['ID']) {
                    $gambarPath = $pet->getGambar();
                    if (!empty($_FILES['gambar']['name'])) { // Jika ada gambar baru, ganti
                        $gambarPath = "img/" . $_POST['ID'] . ".jpg";
                        move_uploaded_file($_FILES['gambar']['tmp_name'], $gambarPath);
                    }
                    $_SESSION['data_petshop'][$key] = new Petshop($_POST['ID'], $_POST['namaProduk'], $_POST['kategori'], $_POST['harga'], $gambarPath);
                    break;
                }
            }
        }
    }
?>
<!DOCTYPE html>
<html>
<head>
    <title>Petshop</title>
</head>
<body>
    <h1>Welcome To Noov Petshop</h1>
    <h2>Menu</h2>
    <form method="POST">
        <button type="submit" name="show">Lihat Produk</button>
        <button type="submit" name="addForm">Tambah Produk</button>
    </form>
    
    <?php if (isset($_POST['addForm'])): ?>
    <h2>Tambah Produk</h2>
    <form method="POST" enctype="multipart/form-data">
        ID: <input type="text" name="ID" required><br>
        Nama: <input type="text" name="namaProduk" required><br>
        Kategori: <input type="text" name="kategori" required><br>
        Harga: <input type="number" name="harga" required><br>
        Gambar: <input type="file" name="gambar" required><br>
        <button type="submit" name="add">Tambah</button>
    </form>
    <?php endif; ?>
    
    <?php if (isset($_POST['show']) || isset($_POST['searchBtn'])): ?>
    <h2>Daftar Produk</h2>
    <form method="POST">
        <input type="text" name="search" placeholder="Cari berdasarkan ID">
        <button type="submit" name="searchBtn">Cari</button>
    </form>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Nama</th>
            <th>Kategori</th>
            <th>Harga</th>
            <th>Gambar</th>
            <th>Aksi</th>
        </tr>
        <?php 
        $data_petshop = $_SESSION['data_petshop'];
        if (isset($_POST['searchBtn']) && !empty($_POST['search'])) {
            $search = strtolower($_POST['search']);
            $data_petshop = array_filter($_SESSION['data_petshop'], function($pet) use ($search) {
                return strpos(strtolower($pet->getID()), $search) !== false;
            });
        }
        ?>
        <?php foreach ($data_petshop as $pet): ?>
            <tr>
                <td><?= htmlspecialchars($pet->getID()) ?></td>
                <td><?= htmlspecialchars($pet->getNamaProduk()) ?></td>
                <td><?= htmlspecialchars($pet->getKategori()) ?></td>
                <td><?= htmlspecialchars($pet->getHarga()) ?></td>
                <td><img src="<?= htmlspecialchars($pet->getGambar()) ?>" width="50"></td>
                <td>
                    <form method="POST" enctype="multipart/form-data" style="display:inline;">
                        <input type="hidden" name="ID" value="<?= htmlspecialchars($pet->getID()) ?>">
                        Nama: <input type="text" name="namaProduk" value="<?= htmlspecialchars($pet->getNamaProduk()) ?>" required><br>
                        Kategori: <input type="text" name="kategori" value="<?= htmlspecialchars($pet->getKategori()) ?>" required><br>
                        Harga: <input type="number" name="harga" value="<?= htmlspecialchars($pet->getHarga()) ?>" required><br>
                        Gambar: <input type="file" name="gambar"><br>
                        <button type="submit" name="edit">Edit</button>
                    </form>
                    <form method="POST" style="display:inline;">
                        <input type="hidden" name="ID" value="<?= htmlspecialchars($pet->getID()) ?>">
                        <button type="submit" name="delete">Hapus</button>
                    </form>
                </td>
            </tr>
        <?php endforeach; ?>
    </table>
    <?php endif; ?>
</body>
</html>
