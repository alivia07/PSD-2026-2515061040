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
  Baris 31 : 
  Baris 32 : 
  Baris 33 : 
  Baris 34 : 
  Baris 35 : 
