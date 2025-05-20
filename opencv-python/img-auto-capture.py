import cv2 as cv
import os

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Impossible d'ouvrir la vidéo")
    exit()

output_dir = "captured_images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

fps = cap.get(cv.CAP_PROP_FPS)
if fps == 0.0:
    fps = 30  
    
print(f"FPS de la vidéo: {fps}")

frame_count = 0
image_count = 1

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv.imshow("Image Register", frame)

    if frame_count % int(fps) == 0:
        image_name = f"{output_dir}/image_{image_count}.jpg"
        cv.imwrite(image_name, frame)
        print(f"Image {image_count} enregistrée: {image_name}")
        image_count += 1

    frame_count += 1

    # Quitter avec la touche 'q'
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
