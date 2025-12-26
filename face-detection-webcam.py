# Face detection
import cv2
# Load the Haar Cascade
faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)
# Always check if webcam opened
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Convert to grayscale
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = faceCascade.detectMultiScale(
        imgGray,
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(30, 30)
    )

    # Draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show webcam feed
    cv2.imshow("Webcam Face Detection", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
