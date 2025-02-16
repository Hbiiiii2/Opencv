import cv2
import mediapipe as mp
import numpy as np
import keyboard  # Menggunakan library keyboard untuk input

# Inisialisasi MediaPipe untuk deteksi tangan
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Fungsi untuk menghitung jarak antar jari tangan untuk mendeteksi kepalan tangan
def is_hand_open(landmarks):
    # Mengukur jarak antar jari (misalnya, jarak antara ujung jari telunjuk dan jari kelingking)
    index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    pinky_finger_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]
    
    distance = np.linalg.norm(np.array([index_finger_tip.x, index_finger_tip.y]) - np.array([pinky_finger_tip.x, pinky_finger_tip.y]))
    # Threshold untuk mendeteksi apakah tangan terbuka atau mengepal
    return distance > 0.1  # Tuning nilai ini sesuai dengan kebutuhan

# Inisialisasi kamera
cap = cv2.VideoCapture(1)

# Variabel untuk status tombol yang sedang ditekan
is_left_pressed = False  # Untuk rem (tangan terbuka)
is_right_pressed = False  # Untuk gas (tangan mengepal)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Mengubah ukuran frame kamera (misalnya menjadi 640x480)
    frame = cv2.resize(frame, (640, 480))  # Ukuran baru: 640x480
    
    # Ubah gambar ke format RGB (MediaPipe memerlukan format ini)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Proses frame dengan MediaPipe Hands
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Gambar tangan yang terdeteksi
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

            # Periksa apakah tangan terbuka atau mengepal
            if is_hand_open(landmarks.landmark):
                cv2.putText(frame, "Rem (Tangan Terbuka)", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                
                # Kirimkan input keyboard untuk rem (misalnya, tombol 'left' untuk berhenti)
                if not is_left_pressed:
                    keyboard.press('left')  # Tekan tombol 'left' untuk rem
                    is_left_pressed = True
                # Pastikan tombol 'right' tidak ditekan
                if is_right_pressed:
                    keyboard.release('right')
                    is_right_pressed = False
            else:
                cv2.putText(frame, "Gas (Tangan Mengepal)", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
                # Kirimkan input keyboard untuk gas (misalnya, tombol 'right' untuk akselerasi)
                if not is_right_pressed:
                    keyboard.press('right')  # Tekan tombol 'right' untuk gas
                    is_right_pressed = True
                # Pastikan tombol 'left' tidak ditekan
                if is_left_pressed:
                    keyboard.release('left')
                    is_left_pressed = False

    # Tampilkan frame dengan hasil deteksi
    cv2.imshow("Hand Gesture Control", frame)

    # Keluar dengan menekan 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Bersihkan dan tutup
cap.release()
cv2.destroyAllWindows()
