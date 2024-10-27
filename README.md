
# FCFS Scheduling Algorithm

## Deskripsi Proyek
Proyek ini adalah implementasi dari algoritma penjadwalan First-Come, First-Served (FCFS) untuk sistem manajemen antrian pada server web. FCFS adalah algoritma sederhana yang memproses permintaan berdasarkan urutan kedatangannya, menjadikannya mudah dipahami dan diterapkan.

## Latar Belakang
Dalam konteks perusahaan e-commerce, sering terjadi lonjakan trafik pada saat promo besar-besaran. Permintaan yang masuk dari berbagai sumber perlu dikelola dengan efisien untuk meminimalkan waktu tunggu bagi pengguna. Algoritma FCFS digunakan untuk menjamin keadilan dalam pemrosesan permintaan.

## Fitur
- Menghitung waktu penyelesaian, waktu turnaround, dan waktu tunggu untuk setiap permintaan.
- Menampilkan hasil dalam bentuk tabel yang mudah dibaca.
- Implementasi kode yang jelas dan terstruktur.

## Struktur Kode
### Kelas `Request`
Kelas ini digunakan untuk mendefinisikan objek permintaan yang memiliki atribut:
- `name`: Nama permintaan (A, B, C, D, E).
- `arrival_time`: Waktu kedatangan permintaan.
- `processing_time`: Waktu yang diperlukan untuk memproses permintaan.
- `completion_time`: Waktu penyelesaian permintaan.
- `turnaround_time`: Waktu turnaround permintaan.
- `waiting_time`: Waktu tunggu permintaan.

### Fungsi `calculate_fcfs`
Fungsi ini menghitung waktu penyelesaian, waktu turnaround, dan waktu tunggu untuk setiap permintaan berdasarkan algoritma FCFS.

### Fungsi `display_results`
Fungsi ini menampilkan hasil perhitungan dalam format tabel yang rapi, memudahkan pengguna untuk memahami hasil dari proses penjadwalan.

## Cara Menjalankan
1. Pastikan Anda memiliki Python terinstal di sistem Anda.
2. Unduh atau clone repositori ini ke komputer Anda.
3. Buka terminal dan arahkan ke direktori proyek.
4. Jalankan program dengan perintah:
   ```bash
   python fcfs_scheduling.py
   ```

## Output
Program akan menghasilkan tabel dengan hasil perhitungan, yang menunjukkan waktu penyelesaian, waktu turnaround, dan waktu tunggu untuk setiap permintaan.

## Analisis
Hasil perhitungan manual menunjukkan bahwa nilai yang diperoleh sesuai dengan output program, yang memastikan bahwa algoritma FCFS diimplementasikan dengan benar. Meskipun FCFS adil dalam pemrosesan, perhatian harus diberikan terhadap efisiensi, terutama ketika waktu respons menjadi kritis.

## Kesimpulan
Proyek ini memberikan pemahaman yang jelas tentang penerapan algoritma FCFS dalam manajemen antrian pada server web. Implementasi yang sederhana namun efektif memungkinkan pengembangan lebih lanjut dengan algoritma yang lebih kompleks untuk situasi yang lebih menantang.

## Kontribusi
Jika Anda ingin berkontribusi pada proyek ini, silakan buat fork dari repositori ini, buat perubahan yang diinginkan, dan kirim pull request.
