# sistem management printer (Printer Spooling)
Deskripsi : Sistem ini dirancang untuk mengelola urutan pencetakan dokumen menggunakan struktur data Queue dengan prinsip FIFO (First In First Out). Sistem bekerja dengan cara menampung setiap permintaan cetak yang masuk ke dalam antrean berdasarkan waktu kedatangannya, di mana dokumen yang pertama kali masuk akan diproses terlebih dahulu oleh mesin printer.
<img width="1920" height="2160" alt="_399_Screenshot 32__7904_Screenshot 33" src="https://github.com/user-attachments/assets/edbcc86e-596b-407a-96f6-6fe575128383" />
<img width="1920" height="2160" alt="_6926_Screenshot 34__6030_Screenshot 35" src="https://github.com/user-attachments/assets/79bf1882-3fd7-4eb7-bab5-2c2f86bb16e5" />
  baris 1 : mendefisikan antrian dari printer
  baris 2 : fungsi inisialisasi dengan kapasitas batas 100
  baris 3 : menyimpan nilai batas maksimal kedalam variable self.maxn
  baris 4 : membuat list kosong sebanyak MAXN
  baris 5 : menandakan indeks depan ke-1 (belum ada dokumen yang keluar)
  baris 6 : menandakan indeks belakang ke-1 (belum ada dokumen yang masuk)
  baris 7 : 
  baris 8 : fungsi pengecekan apakah antrean kosong.
  baris 9 : Mengembalikan True jika indeks depan masih di posisi awal (-1).
  baris 10 : 
  baris 11 : fungsi pengecekan apakah kapasitas sudah penuh
  baris 12 : pengembalian untuk cek apakah indeks belakang sudah berada di ujung array
  baris 13 : 
  baris 14 : Fungsi untuk memasukkan dokumen ke antrian
  baris 15 : Cek apakah antrean sudah penuh.
  baris 16 : Jika penuh, beri peringatan
  baris 17 : Keluar dari fungsi
  baris 18 : pengecekan apakah ini dokumen pertama yang dimasukkan.
  baris 19 : jika benar, geser element depan ke indeks 0
  baris 20 : geser element belakang ke indeks 0
  baris 21 : Jika sudah ada isi sebelumnya.
  baris 22 : Geser indeks belakang satu langkah ke depan
  baris 23 : Simpan nama dokumen ke dalam list pada posisi belakang yang baru.
  baris 24 : mencetak laporan sukses
  baris 25 : 
  baris 26 : fungsi untuk mencetak (mengeluarkan) dokumen paling depan
  baris 27 : pengecekan apakah ada dokumen yang bisa dicetak
  baris 28 : jika tidak ada, beri tahu user bahwa antrian kosong
  baris 29 : keluar dari fungsi
  baris 30 : Tampilkan dokumen yang sedang diproses.
  baris 31 : pengecekan apakah ini dokumen terakhir dalam antrean.
  baris 32 : Jika iya, reset indeks depan ke -1.
  baris 33 : Reset indeks belakang ke -1
  baris 34 : Jika masih ada dokumen lain di belakangnya.
  baris 35 : geser elemen satu langkah ke dokumen berikutnya
  baris 36 : 
  baris 37 : Fungsi untuk melihat dokumen terdepan tanpa mencetaknya.
  baris 38 : pengecekan apakah antrian kosong
  baris 39 : beri tahu user jika antrian kosong
  baris 40 : keluar program
  baris 41 : tampilkan dokumen di posisi depan
  baris 42 : 
  baris 43 : Fungsi untuk melihat semua daftar antrean.
  baris 44 : pengecekan apakah antrian kosong
  baris 45 : beri tahu user jika tidak ada dokumen
  baris 46 : keluar program
  baris 47 : tampilkan "isi antrian print"
  baris 48 : Mulai penelusuran dari indeks paling depan.
  baris 49 : Mulai perulangan tak terbatas
  baris 50 : Cetak nama dokumen pada indeks ke-i.
  baris 51 : Jika sudah sampai di dokumen paling belakang.
  baris 52 : berhenti melakukan perulangan
  baris 53 : Geser penelusuran ke indeks selanjutnya
  baris 54 : Tambahkan baris baru di akhir tampilan.
  baris 55 : 
  baris 56 : mendefinisikan fungsi utama
  baris 57 : membuat objek antrian printer
  baris 58 : inisialisasi variable pilihan menu
  baris 59 : ulangi terus menu selama user belum memilih 5
  baris 60 : Menampilkan teks menu di layar.
  baris 61 : Menampilkan teks menu di layar.  
  baris 62 : Menampilkan teks menu di layar.
  baris 63 : Menampilkan teks menu di layar.
  baris 64 : Menampilkan teks menu di layar.
  baris 65 : Menampilkan teks menu di layar.
  baris 66 : Blok untuk mencegah kode yang berpotensi error.
  baris 67 : Mengambil input user
  baris 68 : Jika user memasukkan selain angka
  baris 69 : cetak beri peringatan eror
  baris 70 : kembali ke awal
  baris 71 : 
  baris 72 : jika user memilih menu 1
  baris 73 : mencoba ambil input nama dokumen
  baris 74 : meminta input nama dokumen dari user
  baris 75 : Masukkan nama file tadi ke fungsi enqueue
  baris 76 : jika terjadi error
  baris 77 : beri tahu user input tidak valid
  baris 78-79 : jika pilih menu 2, jalankan fungsi dequeue
  baris 80-81 : jika pilih menu 3, jalankan fungsi peek
  baris 82-83 : jika pilih menu 4, jalankan fungsi display
  baris 84-85 : jika polih menu 5, tampilkan pesan selesai
  baris 86 : jika user memasukkan angka selain 1-5
  baris 87 : beri tahu user bahwa pilihan tidak valid
  baris 88 : 
  baris 89 : 
  baris 90 : 
  
