import cv2
import time


def open_camera():
    # Try DirectShow (cv2.CAP_DSHOW) first on Windows, then MSMF
    backends = [
        ("DirectShow", cv2.CAP_DSHOW),
        ("MSMF", cv2.CAP_MSMF),
        ("Default", cv2.CAP_ANY),
    ]

    for backend_name, backend in backends:
        for idx in range(3):
            print(f"Testing Camera Index {idx} with backend {backend_name}...")
            cap = cv2.VideoCapture(idx, backend)
            if cap.isOpened():
                ret, frame = cap.read()
                if ret and frame is not None:
                    print(
                        f"✅ Successfully opened camera index {idx} with {backend_name}!"
                    )
                    return cap
                cap.release()
    return None


def main():
    use_yolo = False
    try:
        from ultralytics import YOLO

        print("📦 Loading YOLOv8 nano model...")
        model = YOLO("yolov8n.pt")
        use_yolo = True
        print("✅ YOLO model loaded.")
    except Exception as e:
        print(f"⚠️ Could not load YOLO: {e}")

    cap = open_camera()
    if cap is None:
        print("\n❌ Could not access any webcam.")
        print(
            "👉 Please check Windows Settings > Privacy & security > Camera to ensure app access is ON."
        )
        return

    print("✅ Live stream starting. Press 'q' on the video window to quit.")
    prev_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Failed to grab frame.")
            break

        if use_yolo:
            results = model(frame, verbose=False)
            frame = results[0].plot()

        curr_time = time.time()
        fps = 1.0 / (curr_time - prev_time) if (curr_time - prev_time) > 0 else 0
        prev_time = curr_time
        cv2.putText(
            frame,
            f"FPS: {fps:.1f}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2,
        )

        cv2.imshow("Webcam YOLO Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
