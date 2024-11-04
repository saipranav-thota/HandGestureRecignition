import cv2
import mediapipe as mp
from orientation import orientation, position, trial
from checkFinger import finger
from gestures import gestures

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mphands = mp.solutions.hands
hands = mphands.Hands(max_num_hands = 1)
frame = 0

cap = cv2.VideoCapture(0)

while True:
    success, image = cap.read()
    if not success:
        break
    frame+=1
    image = cv2.cvtColor(cv2.flip(image,1), cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
            mp_drawing.draw_landmarks(
                image, 
                hand_landmarks, mphands.HAND_CONNECTIONS
            )
            labels = results.multi_handedness[idx].classification[0].label 
            # print(frame)
            print(gestures(orientation(hand_landmarks), labels))
            # print(finger(orientation(hand_landmarks), labels))
            # print(position(orientation(hand_landmarks)))
           
            # to access each individaul landmark of a single frame use 
            # hand_landmarks.landmark[location number]
            
                        


    cv2.imshow('Handtracker', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release 

