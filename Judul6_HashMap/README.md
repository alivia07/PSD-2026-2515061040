# Sistem Pengarsipan Berkas Map Fisik pada Filing Cabinet
Deskripsi : Sistem ini dirancang untuk mengelola dan mengarsipkan dokumen fisik klien secara terstruktur berdasarkan inisial nama menggunakan algoritma Hash Map dengan metode Separate Chaining. Sistem bekerja dengan cara memasukkan berkas baru ke dalam salah satu dari 10 laci abjad yang ditentukan langsung oleh fungsi hash melalui huruf pertama nama klien. Ketika terjadi tabrakan (collision) akibat adanya nama dengan inisial yang sama, sistem akan menangani kendala tersebut dengan menyusun berkas-berkas itu berjejer ke belakang di dalam laci yang sama membentuk struktur antrean berantai (linked list).
  Baris 1: Mendefinisikan sebuah kelas bernama Node untuk membuat objek  
  Baris 2: Fungsi def untuk membuat node baru yang menerima 3 parameter  
  Baris 3: Menyimpan ID unik klien ke dalam properti key milik node.  
  Baris 4: Menyimpan nama berkas klien ke dalam properti value milik node.  
  Baris 5: Mengatur pointer next ke berkas berikutnya.  
  Baris 8: Mendefinisikan kelas utama untuk sistem Filing Cabinet.  
  Baris 9: fungsi def untuk membuat kabinet baru dengan ukuran default 10 laci.  
  Baris 10: Menyimpan angka kapasitas laci (10) ke dalam variabel   
  Baris 11: Membuat array (table) berisi 10 slot kosong  
  Baris 13: Fungsi untuk menghitung indeks laci berdasarkan key angka.  
  Baris 14: Rumus matematika modulo untuk memastikan ID angka diubah menjadi indeks laci.  
  Baris 16: Fungsi untuk memasukkan berkas baru ke dalam laci kabinet.  
  Baris 17: Memanggil fungsi hash untuk menentukan nomor laci   
  Baris 18: Menunjuk berkas yang berada di urutan paling depan  
  Baris 19: Melakukan perulangan selama laci tersebut tidak kosong untuk mengecek isinya.  
  Baris 20: Memeriksa apakah berkas dengan ID tersebut sudah pernah disimpan sebelumnya.  
  Baris 21: Jika ID sudah ada, sistem hanya memperbarui nama berkas saja.  
  Baris 22: Keluar dari fungsi bila proses sudah selesai.  
  Baris 23: Jika ID tidak cocok, geser melihat berkas di belakangnya.  
  Baris 24: Jika setelah ditelusuri ID-nya benar-benar baru, buat objek berkas baru.  
  Baris 25: Gandengkan berkas baru ini agar menunjuk ke berkas yang sebelumnya ada di urutan depan laci.  
  Baris 26: Letakkan berkas baru di urutan paling depan di dalam laci  
  Baris 28: Fungsi untuk mencari berkas berdasarkan ID.  
  Baris 29: Menghitung rumus hash untuk tahu berkas tersebut disimpan di laci nomor berapa.  
  Baris 30: Membuka laci yang tepat dan melihat berkas urutan pertama.  
  Baris 31: Melakukan perulangan untuk menelusuri rantai berkas dari depan ke belakang.  
  Baris 32: Memeriksa apakah ID berkas yang sedang dilihat cocok dengan ID yang dicari.  
  Baris 33: Jika cocok, kembalikan seluruh data berkas tersebut ke pemanggil.  
  Baris 34: Jika belum cocok, geser memeriksa berkas berantai di belakangnya.  
  Baris 35: Jika laci sudah diperiksa sampai habis dan tetap tidak ketemu, kembalikan nilai kosong.  
  Baris 37: Fungsi untuk menghapus berkas berdasarkan ID.  
  Baris 38: Menghitung indeks lokasi laci tempat berkas disimpan.  
  Baris 39: Menunjuk berkas pertama di laci tersebut.  
  Baris 40: Membuat variabel pembantu prev untuk mencatat berkas sebelumnya  
  Baris 41: Mulai menelusuri rantai berkas di dalam laci.  
  Baris 42: Jika menemukan berkas dengan ID yang cocok   
  Baris 43: Memeriksa apakah berkas yang mau dihapus berada di urutan paling depan.  
  Baris 44: Jika di urutan depan, pindah posisi depan laci langsung ke berkas urutan kedua  
  Baris 45: Kondisi jika berkas yang dihapus berada di tengah atau di belakang rantai.  
  Baris 46: Hubungkan tali berkas sebelumnya  langsung melompati berkas saat ini ke berkas setelahnya.  
  Baris 47: Keluar dari fungsi dan mengembalikan nilai True  
  Baris 48: Jika belum cocok, simpan posisi berkas saat ini ke variabel prev.  
  Baris 49: Geser maju current untuk memeriksa berkas berikutnya.  
  Baris 50: Jika laci habis ditelusuri dan berkas tidak ada, keluar dan kembalikan nilai False.  
  Baris 52: Fungsi untuk mencetak display data isi laci.  
  Baris 53: Mencetak baris teks awal  
  Baris 54: Melakukan perulangan sebanyak 10 kali untuk mengunjungi Laci 0 sampai Laci 9.  
  Baris 55: Mencetak tulisan label nomor laci tanpa membuat baris baru.  
  Baris 56: Mengambil data berkas pertama di laci ke-i.  
  Baris 57: Selama masih berkas di laci tidak kosong  
  Baris 58: Cetak ID dan nama berkasnya ke samping.  
  Baris 59: Geser ke berkas gandengan di belakangnya.  
  Baris 60: Jika rantai sudah habis atau lacinya kosong, print tulisan kosong
  Baris 63: Mendefinisikan fungsi main() utama.  
  Baris 64: Membuat objek kabinet baru bernama cabinet dengan memanggil kelas FilingCabinetHashMap.  
  Baris 66-74: Memasukkan code unik dan nama berkas.  
  Baris 75: Memanggil fungsi visualisasi isi kabinet untuk dicetak ke terminal.  
  Baris 77: Meminta input dari user, mengubahnya jadi integer dan disimpan di variabel x.  
  Baris 78: Melakukan pencarian data x ke dalam sistem kabinet dan hasilnya disimpan di variabel hasil.  
  Baris 79: Memeriksa apakah data hasil pencarian ditemukan.  
  Baris 80: Jika ketemu, cetak ID beserta isi nama berkasnya.  
  Baris 81: Kondisi jika data hasil pencarian kosong.  
  Baris 82: Cetak informasi bahwa data ID tersebut tidak ditemukan di sistem.  
  Baris 80: Sintaks standar Python untuk mendeteksi bahwa file ini dijalankan secara langsung.  
  Baris 81: Memanggil dan menjalankan fungsi main().  
