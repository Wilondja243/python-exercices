import cv2 as cv
import os

# Capture a video camera
cap = cv.VideoCapture(0)

# If capture is not open, we exit code and show error message
if not cap.isOpened():
    print("Impossible d'ouvrir la vidéo")
    exit()

# Create folder to stock image capture
output_dir = "captured_images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Take time to the image capture with camera 
fps = cap.get(cv.CAP_PROP_FPS)
if fps == 0.0:
    # Default time
    fps = 30  
    
print(f"FPS de la vidéo: {fps}")

# Image count and Frame count
frame_count = 0
image_count = 1

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Show video camera
    cv.imshow("Video", frame)

    # We register image after all 30 fps per second
    if frame_count % int(fps) == 0:

        image_name = f"{output_dir}/image_{image_count}.jpg"

        # Image register
        cv.imwrite(image_name, frame)
        print(f"Image {image_count} enregistrée: {image_name}")

        image_count += 1

    frame_count += 1

    # Quit with key 'q'
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
