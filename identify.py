import cv2
import mediapipe as mp

# Initialize MediaPipe Hands solution
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mphands = mp.solutions.hands
hands = mphands.Hands(static_image_mode=True, max_num_hands=1)

# Load an image from a file
image_path = 'thumbs-up.jpg'  # Replace with the path to your image
image = cv2.imread(image_path)
image = cv2.resize(image, (640, 480))


# Convert the image to RGB (MediaPipe expects RGB images)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Process the image and detect hand landmarks
results = hands.process(rgb_image)

# If hands are detected, draw landmarks and annotate with landmark index
if results.multi_hand_landmarks:
    for hand_landmarks in results.multi_hand_landmarks:
        # Draw the hand landmarks on the image
        mp_drawing.draw_landmarks(
            image, 
            hand_landmarks, mphands.HAND_CONNECTIONS
        )
        
        # Loop through each landmark, annotate its location with the index number
        for idx, landmark in enumerate(hand_landmarks.landmark):
            # Convert normalized landmark coordinates to pixel values
            h, w, _ = image.shape
            x, y = int(landmark.x * w), int(landmark.y * h)
            
            # Annotate the landmark index near the landmark
            cv2.putText(image, str(idx), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.5, (255, 0, 0), 2, cv2.LINE_AA)

# Display the image with landmarks and indices
cv2.imshow('Hand Landmarks with Indices', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
