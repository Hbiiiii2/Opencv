# 🚀 Hand Gesture Control

## 🔥 Deskripsi
Program ini menggunakan **MediaPipe** dan **OpenCV** untuk mendeteksi gerakan tangan dan mengontrol input keyboard berdasarkan posisi tangan. Dengan teknologi ini, Anda dapat mengendalikan perangkat hanya dengan gerakan tangan!

## 🎯 Fitur Unggulan
- 📷 **Deteksi tangan real-time** menggunakan kamera.
- ✋ **Pelacakan tangan presisi** dengan MediaPipe.
- 🎨 **Tampilan interaktif** menggunakan OpenCV.
- ⌨️ **Kontrol keyboard otomatis** berdasarkan gestur tangan.
- 🔍 **Dua mode utama**:
  - **🛑 Rem (Tangan Terbuka)** → Tombol `left` ditekan.
  - **🏎️ Gas (Tangan Mengepal)** → Tombol `right` ditekan.

## 📌 Prasyarat
Pastikan Anda telah menginstal pustaka yang diperlukan:
```bash
pip install opencv-python mediapipe numpy keyboard
```

## 🚀 Cara Menjalankan
1. 🔌 Sambungkan kamera ke komputer.
2. 🏁 Jalankan skrip dengan perintah berikut:
   ```bash
   python main.py
   ```
3. 🎥 Jendela kamera akan muncul dengan status:
   - **✅ "Rem (Tangan Terbuka)"** → Tombol `left` ditekan.
   - **✅ "Gas (Tangan Mengepal)"** → Tombol `right` ditekan.
4. 🔚 Tekan `q` untuk keluar dari program.

## 🏗️ Struktur Kode
- **🛠️ Inisialisasi MediaPipe**: Mendeteksi dan melacak tangan.
- **📏 Fungsi `is_hand_open(landmarks)`**: Menghitung jarak antar jari untuk deteksi tangan terbuka atau mengepal.
- **🔄 Loop utama**:
  - 📸 Membaca frame dari kamera.
  - 🖐️ Mendeteksi tangan menggunakan MediaPipe.
  - 🔀 Menentukan status tangan.
  - ⌨️ Mengirim input keyboard sesuai gestur.
  - 🎬 Menampilkan hasil deteksi.

## 💡 Catatan Tambahan
- 🎯 Pastikan kamera berfungsi dengan baik.
- 🎛️ Anda bisa menyesuaikan nilai threshold di fungsi `is_hand_open`.
- 🚀 Skrip ini bisa dikembangkan lebih lanjut untuk mendukung lebih banyak gestur.

## 📜 Lisensi
Proyek ini **bebas digunakan** dan **dapat dimodifikasi** sesuai kebutuhan.

