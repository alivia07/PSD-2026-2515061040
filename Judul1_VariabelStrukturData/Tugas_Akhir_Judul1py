def tampilkan_menu():
    print("1. Tambah Barang Baru")
    print("2. Cek Semua Barang")
    print("3. Hapus Barang")
    print("4. Keluar")

def main():
    inventaris = []  
    running = True
    
    while running:
        tampilkan_menu()
        try:
            pilihan = int(input("Pilih menu (1-4): "))
            
            if pilihan == 1:
                nama_barang = input("Masukkan nama barang: ").strip()
                if nama_barang:
                    inventaris.append(nama_barang)
                    print(f"'{nama_barang}' berhasil ditambahkan ke inventaris.")
                else:
                    print("Nama barang tidak boleh kosong!")
            
            elif pilihan == 2:
                if inventaris:
                    print("Daftar inventaris barang kos:")
                    for i in range(1, len(inventaris) + 1):
                         barang = inventaris[i - 1]  
                         print(f"{i}. {barang}")
                else:
                    print("Inventaris masih kosong.")
            
            elif pilihan == 3:
                if inventaris:
                    nama_hapus = input("Masukkan nama barang yang akan dihapus: ").strip()
                    if nama_hapus in inventaris:
                        inventaris.remove(nama_hapus)
                        print(f"'{nama_hapus}' berhasil dihapus dari inventaris.")
                    else:
                        print("Barang tidak ditemukan!")
                else:
                    print("Inventaris masih kosong.")
            
            elif pilihan == 4:
                print("Terima kasih!")
                running = False
            
            else:
                print("Pilihan tidak valid! Pilih 1-4.")
                
        except ValueError:
            print("Masukkan angka yang valid (1-4)!")

if __name__ == "__main__":
    main()
