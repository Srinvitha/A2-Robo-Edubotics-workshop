import time
import cv2
import numpy as np
from bonicbot_bridge import BonicBot

# NOTE: Replace with your actual BonicBot / Raspberry Pi IP address
ROBOT_IP = "192.168.1.100"  # <-- Change this to your robot's IP address


def draw_detections(frame, detections):
    h_px, w_px = frame.shape[:2]
    for det in detections:
        bbox = det.get("bbox")
        if not bbox or len(bbox) < 4:
            continue

        # Pipeline publishes normalised [cx, cy, w, h] (0-1)
        cx_n, cy_n, bw_n, bh_n = bbox
        x1 = max(0, int((cx_n - bw_n / 2) * w_px))
        y1 = max(0, int((cy_n - bh_n / 2) * h_px))
        x2 = min(w_px - 1, int((cx_n + bw_n / 2) * w_px))
        y2 = min(h_px - 1, int((cy_n + bh_n / 2) * h_px))

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f"{det.get('class', '?')} {det.get('confidence', 0.0):.0%}"
        cv2.putText(
            frame,
            label,
            (x1 + 2, max(15, y1 - 4)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2,
        )
    return frame


def main():
    print(f"Connecting to BonicBot at {ROBOT_IP}...")
    with BonicBot(host=ROBOT_IP) as bot:
        print("📷 Starting camera and streaming...")
        bot.system.start_camera()
        bot.start_camera()
        bot.camera.wait_for_image(timeout=5.0)

        print("🚀 Starting YOLO detection mode...")
        bot.enable_detection("yolo")

        # Wait for RPi to load the model and confirm YOLO is active
        while not bot.vision.yolo_enabled:
            time.sleep(0.1)

        print("✅ Live Stream Active. Press 'q' to quit.")
        while True:
            frame = bot.get_image()
            if frame is not None:
                detections = bot.vision.get_detections()
                display = draw_detections(frame.copy(), detections)
                cv2.imshow("BonicBot Vision", display)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cv2.destroyAllWindows()
        bot.disable_detection()
        bot.stop_camera()
        bot.system.stop_camera()


if __name__ == "__main__":
    main()
