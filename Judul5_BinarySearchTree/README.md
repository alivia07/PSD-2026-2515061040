 # Sistem Antrean Unit Gawat Darurat (UGD) Rumah Sakit.
Deskripsi : Sistem ini dirancang untuk mengelola antrean pasien di Unit Gawat Darurat (UGD) secara otomatis berdasarkan skor tingkat kekritisan kondisi pasien (skala 1-100) menggunakan algoritma Binary Search Tree (BST) Lanjut. Sistem bekerja dengan cara memasukkan data pasien baru ke dalam pohon antrean secara terstruktur. Ketika dokter membutuhkan pasien pengganti, sistem akan mencari pasien yang setingkat lebih kritis (Successor) atau setingkat lebih stabil (Predecessor) dari skor acuan saat itu. Di mana setelah pasien tersebut ditemukan, sistem akan langsung memanggil pasien ke ruang penanganan dan otomatis menghapus (Auto-Delete) data pasien tersebut dari antrean agar struktur pohon tetap rapi dan efisien.
<img width="1920" height="7560" alt="_9352_Screenshot 54__5888_Screenshot 55__6970_Screenshot 56__8010_Screenshot 57__3141_Screenshot 58__6888_Screenshot 59__6854_Screenshot 61" src="https://github.com/user-attachments/assets/8656a111-4fe7-43f3-a7bd-8f8d5953750b" />
  Baris 1 : mendefinisikan sebuah kelas bernama Node untuk membuat cetakan objek wadah data di dalam pohon.  
  Baris 2 : menginisialisasi objek baru saat pasien didaftarkan.  
  Baris 3 : menyimpan angka skor tingkat kekritisan pasien.  
  Baris 4 : menyimpan data kedalam variable nama pasien.  
  Baris 5 : menyiapkan cabang sebelah kiri untuk menampung pasien dengan skor lebih kecil.  
  Baris 6 : Menyiapkan cabang sebelah kanan untuk menampung pasien dengan skor lebih besar.  
  Baris 7 :  
  Baris 8 :  
  Baris 9 : mendefinisikan kelas utama bernama UGDSystemBST.  
  Baris 10 : membuat sistem antrean baru.  
  Baris 11 : penanda bahwa antrean UGD masih dalam keadaan kosong (belum ada titik root).  
  Baris 12 :  
  Baris 13 : mencari posisi kosong yang tepat bagi pasien baru.  
  Baris 14-15 : Jika posisi pohon saat itu kosong, buat node menjadi root.   
  Baris 16-17 : Jika skor pasien baru lebih kecil, node pasien ditambahkan ke bagian kiri.  
  Baris 18-19 : Jika skor pasien baru lebih besar, node pasien ditambahkan kebagian kanan.  
  Baris 20 : mengembalikan struktur node yang telah diperbarui.  
  Baris 21 :  
  Baris 22-23 : fungsi yang dipanggil dari menu luar untuk memulai pendaftaran pasien.
  Baris 24 :  
  Baris 25 : Mendeklarasikan fungsi bernama find min node.  
  Baris 26 : Membuat variabel pointer sementara.  
  Baris 27 : Melakukan perulangan (looping) selama node saat ini (current) tidak kosong.  
  Baris 28 : Menggeser posisi current satu langkah ke anak cabang sebelah kirinya.
  Baris 29 : Setelah perulangan berhenti, fungsi akan mengembalikan (return) seluruh objek Node paling kecil tersebut.
  Baris 30 :  
  Baris 31 : Mendefinisikan fungsi delete node.  
  Baris 32-33 : Kondisi dasar jika pohon kosong skor pasien tersebut tidak ditemukan di dalam sistem antrean.  
  Baris 34-35 : Jika skor yang ingin dihapus ternyata lebih kecil dari skor node saat ini, maka sistem akan belok mencari ke cabang kiri  
  Baris 36-37 : Jika skor yang ingin dihapus lebih besar dari skor node saat ini, sistem akan belok mencari ke cabang kanan.  
  Baris 38 : ketika skor yang dicari tidak lebih kecil dan tidak lebih besar, artinya skor node saat ini adalah node pasien yang tepat yang ingin dihapus.  
  Baris 39-40 : Memeriksa apakah pasien yang dihapus tidak punya anak cabang sama sekali, jika iya, hapus node dengan cara mengembalikan nilai None ke pointer di atasnya.  
  Baris 41-42 : Jika cabang kiri kosong, berarti node tersebut hanya memiliki anak cabang sebelah kanan. Sistem langsung menaikkan/mengembalikan anak kanan tersebut.  
  Baris 43-44 : Jika cabang kanan kosong, berarti node tersebut hanya memiliki anak cabang sebelah kiri. Sistem langsung menaikkan anak kiri tersebut.  
  Baris 45 : Jika node pasien yang dihapus ternyata memiliki anak di sebelah kiri dan anak di sebelah kanan.  
  Baris 46 : Sistem mencari pengganti terdekat dari cabang sebelah kanan menggunakan fungsi find min node.  
  Baris 47 : Menyalin nilai skor dari node successor ke dalam node yang mau dihapus.  
  Baris 48 : Menyalin nama pasien dari node successor ke node saat ini.  
  Baris 49 : jika data successor sudah dinaikkan ke atas, maka hapus fisik node successor yang asli yang masih tertinggal.  
  Baris 50 : Mengembalikan objek root.  
  Baris 51 :  
  Baris 52 : Mendeklarasikan fungsi bernama delete.  
  Baris 53 : Menjalankan fungsi delete node dengan memasukkan titik pangkal antrean dan skor target.  
  Baris 54 : 
  Baris 55 : Mendeklarasikan fungsi bernama level order.  
  Baris 56-58 : Kondisi awal. jika dari awal sistem mendeteksi bahwa tidak ada satu pun pasien di dalam UGD, sistem akan langsung mencetak tulisan "Antrean kosong" dan langsung keluar dari fungsi.  
  Baris 59 : Membuat sebuah list kosong bernama queue.  
  Baris 60 : Memasukkan node root (pasien paling atas) sebagai elemen pertama ke dalam list queue.  
  Baris 61 : Memulai perulangan (looping).  
  Baris 62 : Mengambil dan mengeluarkan elemen paling depan dari list queue bantuan, lalu menyimpannya ke dalam variabel sementara bernama current.  
  Baris 63 : Mencetak data pasien yang sedang disimpan oleh current ke layar monitor.  
  Baris 64-65 : Sistem Pengecekan Apakah pasien yang baru saja dicetak ini punya anak cabang di sebelah kiri. Jika ada "is not None", maka masukkan node anak kiri tersebut ke barisan paling belakang list queue.  
  Baris 66-67 : Sistem mengecek cabang sebelah kanan. Jika pasien saat ini memiliki anak cabang di sebelah kanan, masukkan node anak kanan tersebut ke barisan paling belakang list queue. 
  Baris 68 : Mencetak kata Selesai di ujung kanan barisan sebagai penutup alur.  
  Baris 69 :  
  Baris 70 : Mendeklarasikan fungsi bernama find node.   
  Baris 71-72 : Jika root is None, fungsi akan mengembalikan nilai None. dan jika root.key sama dengan key, fungsi akan mengembalikan objek Node pasien tersebut.  
  Baris 73-75 : Jika skor target yang dicari ternyata lebih kecil dari skor node saat ini (root.key), maka sudah pasti data tersebut berada di area sebelah kiri. dan Baris 75 otomatis dieksekusi jika kondisi di baris 72 tidak terpenuhi.  
  Baris 76 :  
  Baris 77 : Mendeklarasikan fungsi pencarian pasien successor.  
  Baris 78 : Memanggil fungsi find_node untuk melacak dan mengambil objek node pasien acuan tersebut.  
  Baris 79-80 : jika pasien dengan skor acuan tersebut ternyata tidak terdaftar atau tidak ditemukan di UGD, fungsi langsung berhenti.  
  Baris 81-83 : Jika pasien target memiliki anak cabang di sebelah kanan, maka pasien yang setingkat lebih kritis pasti berada di sub-pohon sebelah kanan tersebut dan akan langsung mencari node yang nilainya paling kecil (paling kiri) di dalam cabang kanan. Mengembalikan objek node pasien pengganti yang ditemukan.  
  Baris 84-85 : Jika pasien target tidak punya cabang kanan, sistem melacak dari atas pohon (root). dan menyimpannya ke variable current.  
  Baris 86 :  Melakukan perulangan.  
  Baris 87-88 : jika skor acuan dokter lebih kecil dari skor node yang sedang dilewati, berarti node saat ini berpotensi menjadi successor dan disimpan ke variable.  
  Baris 89 : sistem akan menelusuri sebelah kiri dan mencari apakah ada pasien lain yang skornya lebih mendekati skor acuan.  
  Baris 90-91 : Jika skor acuan ternyata lebih besar dari node yang dilewati, sistem langsung melangkah belok ke cabang sebelah kanan.  
  Baris 92-93 : Jika menemukan node yang nilainya sama dengan skor acuan, langsung hentikan perulangan.  
  Baris 94-95 : Jika setelah ditelusuri variabel successor tetap kosong (None), artinya pasien acuan tersebut adalah pasien dengan skor tertinggi di UGD.  
  Baris 96 : Jika ada, fungsi sukses mengembalikan objek Node pasien successor.  
  Baris 97 :  
  Baris 98 : Mendeklarasikan fungsi pencarian pasien predecessor.  
  Baris 99 : Memanggil fungsi find node untuk mencari letak objek node pasien acuan.  
  Baris 100-101 : jika pasien dengan skor acuan tersebut tidak ditemukan di UGD, fungsi langsung berhenti.  
  Baris 102 : Jika pasien target memiliki anak cabang di sebelah kiri, maka pasien yang setingkat lebih stabil pasti berada di dalam sub-pohon sebelah kiri.  
  Baris 103 : Mengeset variabel jalan current.  
  Baris 104-105 : elakukan perulangan untuk terus berjalan ke arah kanan sampai ujung.  
  Baris 106 : Mengembalikan objek node pasien predecessor.  
  Baris 107-108 : jika pasien target tidak punya cabang kiri, pelacakan dilakukan dari atas pohon (root) dan menyiapkan penunjuk jalan current = root.  
  Baris 109 : Melakukan perulangan.  
  Baris 110-112 : Jika skor acuan dokter nilainya lebih besar dari skor node yang sedang dilewati, berarti node saat ini berpotensi menjadi predecessor-nya. Simpan node ini ke variabel. sistem menelusuri sebelah kanan, mencari tahu apakah ada pasien lain yang nilainya jauh lebih mendekati skor acuan.  
  Baris 113-114 : ika skor acuan ternyata lebih kecil dari node yang dilewati, sistem langsung pergi ke cabang sebelah kiri tanpa mengubah isi variabel.  
  Baris 115-116 : Jika menemukan node yang nilainya sama persis dengan skor acuan, perulangan langsung dihentikan.  
  Baris 117-118 : Jika setelah dicari variabel predecessor tetap kosong, artinya pasien acuan tersebut adalah pasien dengan kondisi paling ringan/skor paling rendah di UGD.  
  Baris 119 : Jika ada, fungsi sukses mengembalikan objek Node pasien predecessor tersebut.  
  Baris 120 :  
  Baris 121-122 : Mendeklarasikan fungsi utama program. ugd = UGDSystemBST() berfungsi untuk membuat objek sistem antrean UGD baru yang masih kosong ke dalam variabel.  
  Baris 123 : Menyiapkan variabel penampung pilihan menu user.  
  Baris 124 : Membuat program terus berulang.  
  Baris 125-130 : perintah print untuk menampilkan secara visual daftar menu pilihan sistem UGD otomatis di layar.  
  Baris 131-132 : Membuka blok pelindung error. Sistem meminta input angka menu dari user.  
  Baris 134-135 : Jika user memasukkan huruf atau karakter selain angka program akan mencetak Input tidak valid dan langsung melompat mengulang ke awal menu utama menggunakan perintah continue.  
  Baris 136-139 : jika user memilih menu 1, sistem meminta input nama pasien dan skor kekritisannya.  
  Baris 140-141 : Memanggil fungsi insert untuk menaruh data pasien tersebut ke dalam pohon BST, lalu mencetak status sukses.  
  Baris 142-143 : try-except internal agar program tidak rusak jika user salah memasukkan tipe data dan menampilkan input tidak valid.  
  Baris 144-146 : Jika user memilih menu 2, sistem akan memanggil fungsi cetak ugd level order dengan mengirimkan parameter ugd root sebagai pangkal pohon utama.  
  Baris 147-149 : Jika memilih menu 3, dokter diminta memasukkan skor acuan pasien yang saat ini sedang ditangani.
  Baris 150 : Memanggil fungsi pencarian successor.  
  Baris 151-152 : jika data successor ditemukan, cetak nama dan skor pasien tersebut ke layar sebagai tanda panggilan.  
  Baris 153-154 : Secara otomatis langsung menghapus data fisik pasien tersebut.  
  Baris 155-158 : Menampilkan pesan gagal jika pasien tidak ditemukan, atau jika terjadi kesalahan input data.  
  Baris 159-162 : memanggil fungsi ugd find predecessor untuk mencari pasien yang kondisinya setingkat lebih ringan/stabil dari skor acuan dokter.
  Baris 163-170 : jika pasien predecessor ketemu, identitasnya akan dicetak, lalu dihapus langsung menggunakan ugd delete agar keluar dari antrean.  
  Baris 171-173 : Jika user memilih angka 5, program akan mencetak teks penutup dan menghentikan perulangan secara paksa.  
  Baris 174-175 : Menangani jika user memasukkan angka menu di luar rentang 1-5.  
  Baris 176 :  
  Baris 177 : memastikan fungsi main() berjalan jika file di eksekusi langsung.  
  Baris 178 : memanggil fungsi utama untuk memulai seluruh.  
<img width="1920" height="3240" alt="_2380_Screenshot 62__4364_Screenshot 63__2605_Screenshot 64" src="https://github.com/user-attachments/assets/50845280-3fab-4390-a33b-19f0e90fb065" />
  Penjelasan Output : pada Menu 1 dimasukkan tiga pasien (Janice: 56, Theodore: 24, Kaitlyn: 98). Menu 2 menampilkan antrean dengan traversal level-order (urutan: Janice, Theodore, Kaitlyn). Menu 3 dan Menu 4 mensimulasikan pemanggilan dan penghapusan pasien secara otomatis menggunakan In-order Successor (mengganti dengan pasien yang lebih kritis) dan In-order Predecessor (mengganti dengan pasien yang lebih stabil), lalu program dihentikan lewat Menu 5.  

  Link Youtube :  
