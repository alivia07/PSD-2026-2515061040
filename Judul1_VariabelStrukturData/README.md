# Sistem Manajemen Inventaris Barang Kos
Deskripsi : program ini merupakan sistem manajemen inventaris barang kos. program ini dibuat untuk mengelola barang barang pada kos agar tidak berantakan. Fitur utama pada pgrogram ini yaitu bisa input barang baru, nampilin list barang sesuai urutan, hingga hapus barang jika sudah tidak di perlukan lagi. program ini efisien untuk data yang tidak terlalu banyak karena proses nambah datanya cepat (O(1)) dan tampilan mudah di mengerti oleh siapa saja yang menggunakan. algoritma struktur data yang di gunakan disini berupa list satu dimensi (1D)

<img width="1920" height="2160" alt="Sources Code_Tugas Akhir" src="https://github.com/user-attachments/assets/1990c07e-4441-4b19-ad95-ed0741f97edb" />

penjelasan alur logika :
baris  1 : Mendefinisikan fungsi, agar bisa di panggil berulang saat menampilkan kepada user 
baris 2 : Mencetak teks "1. Tambah Barang Baru" ke layar 
baris 3 : Mencetak teks "2. Cek Semua Barang" ke layar.
baris 4 : Mencetak teks "3. Hapus Barang" ke layar.
baris 5 : Mencetak teks "4. Keluar" ke layar.
baris 7 : Mendefinisikan fungsi utama 
baris 8 : Membuat list kosong dengan nama variabel "inventaris", Address memory dibuat.
baris 9 : Membuat variabel boolean "running" bernilai true
baris 11 : Mulai loop while. Selama status running masih True, program bakal terus jalan.
baris 12 : Memanggil fungsi "tampilkan_menu()" (program menjalankan baris 2-5)
baris 13 : Mulai blok try-except untuk menangkap kemungkinan terjadinya error input.
baris 14 : Minta input user dan mengubahnya menjadi integer agar bisa diproses di percabangan. simpan di pilihan.
baris 16 : Jika user memilih 1
baris 17 : Minta user menginput nama barang, (.strip() untuk hapus spasi depan-belakang.)
baris 18 :  program mengecek apakah "nama_barang" tidak kosong.
baris 19 : Tambah "nama_barang" ke akhir list inventaris.
baris 20 : Memberi tahu user bahwa user barang udah masuk list.
baris 21 : Jika "nama_barang" kosong.
baris 22 : Cetak pesan "barang tidak boleh kosong"
baris 24 : Jika user memilih 2
baris 25 : program mengecek apakah list inventaris tidak kosong.
baris 26 : program mencetak judul daftar.
baris 27 : Mulai perulangan dari 1 sampai panjang list.
baris 28 : Ambil barang dari index i-1 (karena list dimulai dari 0)
baris 29 : Program mencetak nomor urut dan nama barang.
baris 30 : Jika list kosong.
baris 31 : Cetak pesan kosong.
baris 33 : Jika user memilih 3
baris 34 : Program Mengecek apakah list tidak kosong.
baris 35 : Minta user menginput nama yang akan dihapus.
baris 36 : Program mengecek apakah nama ada di list.
baris 37 : Hapus nama pertama yang ditemukan.
baris 38 : Program Mencetak pesan sukses.
baris 39 : Jika nama tidak ditemukan.
baris 40 : Program mencetak pesan "Barang tidak Ditemukan"
baris 41 : Jika list kosong.
baris 42 : program mencetak pesan bahwa inventori masih belum terisi 
baris 44 : Jika user memilih 4
baris 45 : program mencetak pesan terimakasih
baris 46 : running di ubah menjadi false agar loop while berhenti
baris 48 : jika user memilih yang bukan 1-4
baris 49 : program mencetak pesah error pada pilihan 
baris 51 : jika input bukan angka, program menangkap adanya error
baris 52 : Program Mencetak pesan error input.
baris 54 : program mengecek apakah file dijalankan langsung 
baris 55 : memanggil fungsi main dan program mulai berjalan
