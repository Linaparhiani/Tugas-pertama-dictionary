

# Fungsi untuk menambahkan transaksi
def tambah_transaksi():
    try:
        id_transaksi = input("Masukkan ID Transaksi: ").strip()
        id_produk = input("Masukkan ID Produk: ").strip()
        jumlah = int(input("Masukkan Jumlah Produk: "))
        
        transaksi = {
            "ID Transaksi": id_transaksi,
            "ID Produk": id_produk,
            "Jumlah": jumlah
        }
        transaksi_list.append(transaksi)
        print(f"Transaksi {id_transaksi} berhasil ditambahkan!\n")
    except ValueError:
        print("Input tidak valid. Pastikan jumlah berupa angka.\n")

# Fungsi untuk menampilkan semua transaksi
def tampilkan_transaksi():
    if not transaksi_list:
        print("Belum ada data transaksi.\n")
        return
    
    print("Data Transaksi:")
    for i, transaksi in enumerate(transaksi_list, start=1):
        print(f"{i}. ID Transaksi: {transaksi['ID Transaksi']}, ID Produk: {transaksi['ID Produk']}, Jumlah: {transaksi['Jumlah']}")
    print()

# Menu utama
while True:
    print("Menu:")
    print("1. Tambah Transaksi")
    print("2. Tampilkan Transaksi")
    print("3. Keluar")
    
    pilihan = input("Pilih menu (1/2/3): ").strip()
    
    if pilihan == "1":
        tambah_transaksi()
    elif pilihan == "2":
        tampilkan_transaksi()
    elif pilihan == "3":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.\n")
