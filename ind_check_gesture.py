import cv2
import mediapipe as mp
from orientation import orientation, position
from checkFinger import finger
from gestures import gestures

import os

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mphands = mp.solutions.hands
hands = mphands.Hands(static_image_mode=True, max_num_hands=1)
frame = 0

cap = cv2.VideoCapture(0)

# Load the image
img_path = r"Dataset\01_palm\frame_05_01_0010.png"
image = cv2.imread(img_path)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = hands.process(rgb_image)

if results.multi_hand_landmarks:
    for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
        # Draw hand landmarks
        mp_drawing.draw_landmarks(image, hand_landmarks, mphands.HAND_CONNECTIONS)

        # Get the label for the current hand
        labels = results.multi_handedness[idx].classification[0].label
        print(frame)
        print(finger(orientation(hand_landmarks), labels))
        print(position(orientation(hand_landmarks)))
        print(labels)

        # Loop through each landmark and draw the index number
        for landmark_idx, landmark in enumerate(hand_landmarks.landmark):
            # Get the coordinates of the landmark
            h, w, _ = image.shape
            cx, cy = int(landmark.x * w), int(landmark.y * h)

            # Draw the index number near the landmark
            cv2.putText(image, str(landmark_idx), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

# Display the image with landmarks
cv2.imshow('Hand Landmarks', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
