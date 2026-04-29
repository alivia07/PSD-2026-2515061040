# Sistem Antrian Ticket Konser
Deskripsi : Sistem ini dirancang sebagai solusi digital untuk mengelola ketidakteraturan urutan penonton pada saat proses penukaran tiket konser. Masalah utama yang diselesaikan adalah efisiensi pemanggilan antrean, di mana penonton seringkali datang secara acak, namun petugas memerlukan urutan yang rapi berdasarkan nomor tiket untuk mempercepat proses verifikasi data.
<img width="1920" height="2160" alt="_8043_Screenshot 10__1364_Screenshot 11" src="https://github.com/user-attachments/assets/1ff495f1-fa61-4a46-93b6-9b38b7c035ed" />

  baris 1 : Mendefinisikan fungsi tukar yang menerima tiga parameter. list antrean, serta indeks i dan j yang akan ditukar.  
  baris 2 : Membuat variabel sementara (temp) untuk menyimpan data penonton pada posisi.  
  baris 3 : Mengambil data penonton dari posisi j dan memasukkannya ke posisi i.  
  baris 4 : Mengambil data yang disimpan di temp tadi (data asli posisi i) dan menaruhnya ke posisi j. Sekarang posisi bertukar.  
  baris 5 :  
  baris 6 : Mendefinisikan fungsi untuk proses pengurutan.  
  baris 7 : Menghitung jumlah total penonton dalam list dan menyimpannya dalam variabel n.  
  baris 8 : Mengontrol berapa kali pengecekan seluruh barisan dilakukan. Proses ini dilakukan sebanyak n dikurangi satu.  
  baris 9 : Membandingkan elemen yang bersebelahan. Batas - i adalah optimasi.  
  baris 10 : Kondisi pengecekan. Program masuk ke dalam dictionary penonton dan membandingkan Nomor Tiket pada indeks j dengan indeks di sebelahnya (j + 1).  
  baris 11 : Jika nomor tiket di kiri lebih besar dari yang di kanan, fungsi tukar dipanggil untuk memindahkan posisi mereka.  
  baris 12 :  
  baris 13 : Mendefinisikan fungsi utama program.  
  baris 14 : Blok exception handling untuk menangkap kesalahan input.  
  baris 15 : Meminta input jumlah penonton dan mengubahnya menjadi tipe data integer.  
  baris 16 : Jika user memasukkan selain angka, program akan menampilkan print  
  baris 17 : Menampilkan pesan kesalahan. (input tidak valid)  
  baris 18 : Menghentikan program karena input jumlah tidak valid.  
  baris 19 :  
  baris 20 : Inisialisasi list kosong untuk menampung data penonton.  
  baris 21 : Menampilkan instruksi untuk input.  
  baris 22 : Melakukan perulangan sebanyak jumlah penonton yang sudah diinput tadi.  
  baris 23: Input nama penonton. Label {i+1} digunakan agar di layar muncul Orang ke-1 (bukan ke-0).  
  baris 24 : Membuat perulangan tanpa henti untuk memvalidasi input nomor tiket.  
  baris 25 : Mencoba memproses input nomor tiket.  
  baris 26 : Mengambil input nomor tiket dan mengubahnya menjadi angka.  
  baris 27 : Menyimpan data nama dan nomor ke dalam dictionary, lalu memasukkannya ke dalam list antrean.  
  baris 28 : Keluar dari while True jika input sudah benar (berupa angka).  
  baris 29 : Menangkap kesalahan jika nomor tiket diisi huruf.  
  baris 30 : Meminta user mengulang input nomor.  
  baris 31 :  
  baris 32 : Menampilkan urutan data asli sesuai waktu input. (belum terurut)  
  baris 33 : Memanggil fungsi algoritma untuk merapikan list berdasarkan nomor tiket.  
  baris 34 :  
  baris 35 : menampilkan urutan data yang sudah terurut. 
  baris 36 : Melakukan perulangan pada list yang sudah rapi untuk mencetaknya satu per satu.  
  baris 37 : Mencetak nama dan nomor tiket dengan format yang sudah rapi.  
  baris 38 :  
  baris 39 : Memastikan fungsi main() hanya dijalankan jika file ini dieksekusi secara langsung.  
  baris 40 : Memanggil fungsi utama untuk memulai seluruh proses.  
