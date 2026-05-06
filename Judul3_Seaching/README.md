 # Sistem Pengecekan Absensi Siswa
 Deskripsi : Sistem ini dirancang untuk melakukan pendataan dan evaluasi tingkat kehadiran mahasiswa menggunakan algoritma Sequential Search. Sistem bekerja dengan cara menghitung frekuensi kemunculan ID mahasiswa tertentu di dalam catatan kehadiran, kemudian mengkategorikan tingkat kehadirannya berdasarkan jumlah kemunculan tersebut. dimana jika ID mahasiswa muncul sebanyak lebih dari 4 kali maka akan di nyatakan "selalu hadir", jika ID mahasiswa muncul kurang dari 4 kali maka akan di nyatakan "jarang hadir"
<img width="1920" height="2160" alt="_3479_Screenshot 16__7525_Screenshot 17" src="https://github.com/user-attachments/assets/04262cb9-00a6-43cf-b348-8b2ec93bd7f8" />
  Baris 1 : Mendefinisikan Fungsi  
  Baris 2 : Mendefinisikan Indeks dimulai dari 0  
  Baris 3 : menghitung seberapa banyak target ditemukan  
  Baris 4 : Melakukan perulangan selama indeks kurang dari n  
  Baris 5 : mengecek apakah indeks sama dengan target  
  Baris 6 : data di temukan, counter bertambah 1  
  Baris 7 : indeks akan ikut bertambah 1  
  Baris 8 : mengembalikan nilai akhir dari counter  
  Baris 9 :  
  Baris 10 : mendefinisikan fungsi utama sebagai awal dari program berjalan  
  Baris 11 : mendefinisikan data berisi ID mahasiswa  
  Baris 12 : Menyimpan list kedalam variable n  
  Baris 13 : menampilkan data mahasiswa  
  Baris 14 :  
  Baris 15 : melakukan perulangan untuk meminta inputan  
  Baris 16 : Blok exception handling untuk menangkap kesalahan input  
  Baris 17 : Meminta Input ID mahasiswa yang akan diubah jadi angka  
  Baris 18 : menghentikan perulangan jika valid  
  Baris 19 : Menangkap kesalahan jika user menginput lain  
  Baris 20 : menampilkan inputan tidak valid  
  Baris 21 :  
  Baris 22 : memanggil fungsi untuk mencari target dan menyimpan di counter  
  Baris 23 :  
  Baris 24 : Mengecek apakah ID ada di dalam data  
  Baris 25 : Menampilkan kemunculan ID mahasiswa tersebut  
  Baris 26-27 : jika ID muncul lebih dari 4 kali, tampilkan status "selalu hadir"  
  Baris 28-29 : jika  ID muncul kurang dari 4, tampilkan status "jarang hadir"  
  Baris 30-31 : jika ID tidak ada dalam data, tampilkan pesan "ID tidak ditemukan"  
  Baris 33 : memastikan fungsi main() berjalan jika file di eksekusi langsung  
  Baris 34 : memanggil fungsi utama untuk memulai seluruh proses  
  <img width="1920" height="1080" alt="Screenshot (18)" src="https://github.com/user-attachments/assets/45479a48-a743-4f26-acdf-f829b3f3887f" />
Penjelasan Output : Pada percobaan pertama dengan memasukkan ID 6101, program melakukan pencarian secara berurutan dari awal hingga akhir data dan menemukan ID tersebut sebanyak 1 kali. Karena nilai counter kurang dari 4, program memenuhi kondisi counter < 4 dan mencetak status "Jarang hadir". Pada percobaan kedua, pengguna memasukkan ID 6123. Setelah melakukan pencarian ulang, program menemukan ID tersebut sebanyak 5 kali. Karena jumlah kemunculannya lebih dari 4 kali, kondisi counter > 4 terpenuhi sehingga program mencetak status "Selalu hadir".  Secara keseluruhan, logika program ini berjalan dengan tepat sesuai kriteria yang telah ditentukan. kemunculan < 4 kali dikategorikan sebagai jarang hadir, sedangkan kemunculan > 4 kali dikategorikan sebagai selalu hadir.
Link Youtube : 
