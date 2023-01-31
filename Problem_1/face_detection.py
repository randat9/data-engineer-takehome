import cv2
import numpy as np
from PIL import Image
import os

def detect_faces(image_path, output_dir):
    # Load the cascade classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Load the input image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Save the detected faces
    i = 1
    for (x, y, w, h) in faces:
        roi_color = image[y:y + h, x:x + w]
        face = Image.fromarray(roi_color)
        face.save(os.path.join(output_dir, f"face_{i}.jpg"))
        i += 1

    return len(faces)

# Example usage:
image_path = "path/to/image.jpg"
output_dir = "path/to/output_dir"
face_count = detect_faces(image_path, output_dir)
print(f"{face_count} faces detected in the image.")
