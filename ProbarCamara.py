import cv2
import mediapipe as mp
import serial
import time

# Configura la conexión serial con Arduino
arduino = serial.Serial('COM3', 9600)  # Cambia 'COM3' por el puerto de tu Arduino
time.sleep(2)  # Espera a que se inicie la conexión

# Inicializa MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=1)
cap = cv2.VideoCapture(0)

# Configura los IDs de los puntos clave de la mano
finger_tips_ids = [4, 8, 12, 16, 20]
prev_fingers_up = -1  # Para detectar cambios

def count_fingers(hand_landmarks):
    fingers = []

    # Pulgar
    if hand_landmarks.landmark[finger_tips_ids[0]].x < hand_landmarks.landmark[finger_tips_ids[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # 4 dedos restantes
    for tip_id in finger_tips_ids[1:]:
        if hand_landmarks.landmark[tip_id].y < hand_landmarks.landmark[tip_id - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return sum(fingers)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            fingers_up = count_fingers(hand_landmarks)

            # Solo enviar si hay cambio en los dedos levantados
            if fingers_up != prev_fingers_up:
                print(f'Dedos: {fingers_up}')
                arduino.write(str(fingers_up).encode())
                prev_fingers_up = fingers_up

    cv2.imshow("Contador de Dedos", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cierre
cap.release()
cv2.destroyAllWindows()
arduino.close()
