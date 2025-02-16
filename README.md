# Hand Gesture Control

## Deskripsi
Program ini menggunakan MediaPipe dan OpenCV untuk mendeteksi gerakan tangan dan mengontrol input keyboard berdasarkan posisi tangan. Program ini dirancang untuk mendeteksi apakah tangan terbuka (rem) atau mengepal (gas), dan kemudian mengirimkan input keyboard yang sesuai.

## Fitur
- Menggunakan kamera untuk mendeteksi tangan secara real-time.
- Menggunakan MediaPipe untuk pelacakan tangan.
- Menggunakan OpenCV untuk menampilkan hasil deteksi.
- Mengontrol keyboard menggunakan pustaka `keyboard`.
- Mendeteksi dua kondisi:
  - **Tangan Terbuka** → Menekan tombol `left` (Rem)
  - **Tangan Mengepal** → Menekan tombol `right` (Gas)

## Prasyarat
Sebelum menjalankan program ini, pastikan Anda telah menginstal pustaka yang diperlukan:
```bash
pip install opencv-python mediapipe numpy keyboard
```

## Cara Menjalankan
1. Sambungkan kamera ke komputer.
2. Jalankan skrip menggunakan Python:
   ```bash
   python main.py
   ```
3. Jendela dengan tampilan kamera akan muncul, menampilkan status tangan:
   - "Rem (Tangan Terbuka)" → Tombol `left` ditekan.
   - "Gas (Tangan Mengepal)" → Tombol `right` ditekan.
4. Tekan `q` untuk keluar dari program.

## Struktur Kode
- **Inisialisasi MediaPipe**: Untuk mendeteksi dan melacak tangan.
- **Fungsi `is_hand_open(landmarks)`**: Menghitung jarak antara ujung jari telunjuk dan kelingking untuk menentukan apakah tangan terbuka atau mengepal.
- **Loop utama**:
  - Membaca frame dari kamera.
  - Mendeteksi tangan menggunakan MediaPipe.
  - Menentukan apakah tangan terbuka atau mengepal.
  - Mengirim input keyboard berdasarkan status tangan.
  - Menampilkan hasil deteksi.

## Catatan Tambahan
- Pastikan kamera berfungsi dengan baik.
- Nilai threshold untuk mendeteksi tangan terbuka atau mengepal dapat disesuaikan sesuai kebutuhan di fungsi `is_hand_open`.
- Skrip ini dapat dikembangkan lebih lanjut untuk mendukung lebih banyak gestur atau fungsi lainnya.

## Lisensi
Proyek ini bebas digunakan dan dimodifikasi sesuai kebutuhan.

