from ultralytics import YOLO
import cv2

model = YOLO("yolo11n.pt")

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(
        frame,
        verbose=False
    )

    result = results[0]

    # Get detected boxes
    boxes = result.boxes

    for box in boxes:

        # Class ID
        class_id = int(box.cls[0])

        # Confidence
        confidence = float(box.conf[0])

        # Class name
        name = model.names[class_id]

        print(
            f"{name} {confidence:.2f}"
        )

    # Display detections
    annotated_frame = result.plot()

    cv2.imshow(
        "YOLO Detection",
        annotated_frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
