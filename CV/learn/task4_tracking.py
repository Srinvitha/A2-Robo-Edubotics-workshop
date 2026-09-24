from ultralytics import YOLO
import cv2

model = YOLO("yolo11n.pt")

cap = cv2.VideoCapture(0)

# Get camera dimensions
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 20

# Video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

out = cv2.VideoWriter(
    "tracked_output.mp4",
    fourcc,
    fps,
    (width, height)
)

# Keep track of people already seen
seen_ids = set()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Track ONLY persons
    results = model.track(
        frame,
        persist=True,
        classes=[0],
        verbose=False
    )

    result = results[0]

    # Number of detected people
    person_count = len(result.boxes)

    # Process tracking IDs
    if result.boxes.id is not None:

        track_ids = result.boxes.id.int().cpu().tolist()

        for track_id in track_ids:
            seen_ids.add(track_id)

    # Draw results
    annotated_frame = result.plot()

    # Display current people count
    cv2.putText(
        annotated_frame,
        f"People detected: {person_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    # Display total unique people seen
    cv2.putText(
        annotated_frame,
        f"People seen: {len(seen_ids)}",
        (20, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    # Display
    cv2.imshow(
        "Person Tracking",
        annotated_frame
    )

    # Save processed video
    out.write(annotated_frame)

    # Q = quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
