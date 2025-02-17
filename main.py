import cv2
import mediapipe as mp
import numpy as np
import keyboard  # Menggunakan library keyboard untuk input

# Inisialisasi MediaPipe untuk deteksi tangan
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.75, min_tracking_confidence=0.75, max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils

# Fungsi untuk menghitung jarak antar jari tangan untuk mendeteksi kepalan tangan
def is_hand_open(landmarks):
    index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    pinky_finger_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]
    distance = np.linalg.norm(
        np.array([index_finger_tip.x, index_finger_tip.y]) - np.array([pinky_finger_tip.x, pinky_finger_tip.y])
    )
    return distance > 0.15  # Threshold lebih stabil

# Inisialisasi kamera dengan pengaturan optimal
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

# Status tombol keyboard
is_left_pressed = False
is_right_pressed = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)  # Membalik agar lebih natural
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            landmarks = hand_landmarks.landmark
            if is_hand_open(landmarks):
                cv2.putText(frame, "Rem (Tangan Terbuka)", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                if not is_left_pressed:
                    keyboard.press('left')
                    is_left_pressed = True
                if is_right_pressed:
                    keyboard.release('right')
                    is_right_pressed = False
            else:
                cv2.putText(frame, "Gas (Tangan Mengepal)", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                if not is_right_pressed:
                    keyboard.press('right')
                    is_right_pressed = True
                if is_left_pressed:
                    keyboard.release('left')
                    is_left_pressed = False
            
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    cv2.imshow("Hand Gesture Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()