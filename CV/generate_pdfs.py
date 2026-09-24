import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


def build_pdf_scenario1(filename="Workshop_Scenario_1_Robot_Bridge.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        "DocTitle",
        parent=styles["Heading1"],
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#1A365D"),
        spaceAfter=6,
    )
    subtitle_style = ParagraphStyle(
        "DocSubtitle",
        parent=styles["Normal"],
        fontSize=11,
        textColor=colors.HexColor("#4A5568"),
        spaceAfter=12,
    )
    h2_style = ParagraphStyle(
        "SectionHeader",
        parent=styles["Heading2"],
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#2B6CB0"),
        spaceBefore=10,
        spaceAfter=6,
    )
    body_style = ParagraphStyle(
        "BodyDark",
        parent=styles["Normal"],
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor("#2D3748"),
    )
    code_style = ParagraphStyle(
        "CodeBlock",
        parent=styles["Code"],
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#2D3748"),
        backColor=colors.HexColor("#EDF2F7"),
        borderColor=colors.HexColor("#CBD5E0"),
        borderWidth=0.5,
        borderPadding=6,
        spaceBefore=4,
        spaceAfter=8,
    )

    story = []

    # Title & Header
    story.append(
        Paragraph(
            "Scenario 1: Physical Robot Deployment (BonicBot + ROS 2)",
            title_style,
        )
    )
    story.append(
        Paragraph(
            "Robotics & Edge AI Workshop — Architecture, Theory, and Step-by-Step Execution Guide",
            subtitle_style,
        )
    )
    story.append(
        HRFlowable(
            width="100%",
            thickness=1.5,
            color=colors.HexColor("#2B6CB0"),
            spaceAfter=12,
        )
    )

    # 1. Theory & Architecture
    story.append(Paragraph("1. System Architecture & Theory", h2_style))
    theory_text = (
        "<b>Core Concept:</b> In a networked robotics architecture, physical sensors (camera, LiDAR, IMU) "
        "and motor drivers run on a dedicated onboard computer (e.g., Raspberry Pi 4/5 or NVIDIA Jetson) running <b>Ubuntu Linux and ROS 2</b>. "
        "The robot acts as an edge node, and remote workstations interact with it via a lightweight bridge protocol.<br/><br/>"
        "<b>Key Subsystems:</b><br/>"
        "• <b>Edge Sensing & YOLO:</b> The camera feed is ingested into a ROS 2 camera node. YOLO runs directly on the robot hardware, "
        "predicting bounding boxes in normalized coordinates [cx, cy, w, h] to minimize data payload.<br/>"
        "• <b>ROSBridge WebSocket Server:</b> Exposes ROS 2 topics and services via JSON over WebSockets (default Port 9090).<br/>"
        "• <b>Client Bridge (Laptop):</b> Uses <code>bonicbot-bridge</code> (built on <code>roslibpy</code>) to subscribe to camera frames "
        "and YOLO detection telemetry, allowing remote telemetry display and control."
    )
    story.append(Paragraph(theory_text, body_style))
    story.append(Spacer(1, 10))

    # Architecture Flow Table
    flow_data = [
        ["Layer", "Component", "Role / Protocol"],
        [
            "Hardware",
            "Robot Camera & Sensors",
            "Captures raw video frames at source",
        ],
        [
            "Robot OS",
            "ROS 2 + YOLO Pipeline",
            "Runs local object detection; extracts [cx, cy, w, h]",
        ],
        [
            "Transport",
            "rosbridge_server (Port 9090)",
            "Serializes ROS topics to JSON WebSockets over Wi-Fi",
        ],
        [
            "Client / PC",
            "bonicbot-bridge + OpenCV",
            "Receives JSON telemetry, renders bounding boxes & UI",
        ],
    ]
    t = Table(flow_data, colWidths=[80, 160, 290])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2B6CB0")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 8.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#F7FAFC")),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
            ]
        )
    )
    story.append(t)
    story.append(Spacer(1, 12))

    # 2. Prerequisites & Environment
    story.append(Paragraph("2. Prerequisites & Setup", h2_style))
    prereq_text = (
        "• <b>Laptop & Robot must be on the same Wi-Fi network</b>.<br/>"
        "• Client Python packages installed on laptop: <code>pip install bonicbot-bridge opencv-python numpy</code>."
    )
    story.append(Paragraph(prereq_text, body_style))
    story.append(Spacer(1, 10))

    # 3. Step-by-Step Commands
    story.append(Paragraph("3. Step-by-Step Commands", h2_style))

    story.append(
        Paragraph("<b>Step A: On the Robot (SSH / Terminal)</b>", body_style)
    )
    robot_cmds = (
        "# 1. Find robot IP address\n"
        "hostname -I\n\n"
        "# 2. Launch the robot system with live camera\n"
        "ros2 launch my_bot robot_system.launch.py use_sim_time:=false use_real_camera:=True\n\n"
        "# 3. Ensure ROSBridge WebSocket server is active (Port 9090)\n"
        "ros2 launch rosbridge_server rosbridge_websocket_launch.xml"
    )
    story.append(Paragraph(robot_cmds.replace("\n", "<br/>"), code_style))

    story.append(
        Paragraph(
            "<b>Step B: On Laptop (Windows PowerShell Verification)</b>",
            body_style,
        )
    )
    client_cmds = (
        "# 1. Ping the robot to test IP connectivity\n"
        "ping <ROBOT_IP>\n\n"
        "# 2. Verify Port 9090 (WebSocket) is reachable\n"
        "Test-NetConnection -ComputerName <ROBOT_IP> -Port 9090"
    )
    story.append(Paragraph(client_cmds.replace("\n", "<br/>"), code_style))

    story.append(
        Paragraph("<b>Step C: Run Client Script on Laptop</b>", body_style)
    )
    script_run = (
        "# In bonicbot_vision.py, set ROBOT_IP = '<ROBOT_IP>'\n"
        "python bonicbot_vision.py"
    )
    story.append(Paragraph(script_run.replace("\n", "<br/>"), code_style))

    # 4. Troubleshooting
    story.append(Paragraph("4. Workshop Troubleshooting & FAQ", h2_style))
    troubleshoot = (
        "• <b>'RosTimeoutError: Failed to connect to ROS':</b> Robot IP is incorrect, robot is off, or Port 9090 is blocked by firewall.<br/>"
        "• <b>AP / Wi-Fi Isolation:</b> Some university/corporate Wi-Fi blocks device-to-device communication. Use a mobile hotspot if ping fails.<br/>"
        "• <b>Lag / High Latency:</b> Reduce camera resolution in ROS launch file to 320x240 or 640x480."
    )
    story.append(Paragraph(troubleshoot, body_style))

    doc.build(story)
    print(f"Generated {filename}")


def build_pdf_scenario2(filename="Workshop_Scenario_2_Local_Webcam_YOLO.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "DocTitle",
        parent=styles["Heading1"],
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#1A202C"),
        spaceAfter=6,
    )
    subtitle_style = ParagraphStyle(
        "DocSubtitle",
        parent=styles["Normal"],
        fontSize=11,
        textColor=colors.HexColor("#4A5568"),
        spaceAfter=12,
    )
    h2_style = ParagraphStyle(
        "SectionHeader",
        parent=styles["Heading2"],
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#C53030"),
        spaceBefore=10,
        spaceAfter=6,
    )
    body_style = ParagraphStyle(
        "BodyDark",
        parent=styles["Normal"],
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor("#2D3748"),
    )
    code_style = ParagraphStyle(
        "CodeBlock",
        parent=styles["Code"],
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#2D3748"),
        backColor=colors.HexColor("#EDF2F7"),
        borderColor=colors.HexColor("#CBD5E0"),
        borderWidth=0.5,
        borderPadding=6,
        spaceBefore=4,
        spaceAfter=8,
    )

    story = []

    # Title & Header
    story.append(
        Paragraph(
            "Scenario 2: Standalone Local Mode (Webcam + YOLOv8)", title_style
        )
    )
    story.append(
        Paragraph(
            "Robotics & Edge AI Workshop — Offline Simulation & Computer Vision Demonstration Guide",
            subtitle_style,
        )
    )
    story.append(
        HRFlowable(
            width="100%",
            thickness=1.5,
            color=colors.HexColor("#C53030"),
            spaceAfter=12,
        )
    )

    # 1. Theory & Architecture
    story.append(Paragraph("1. Computer Vision & YOLO Theory", h2_style))
    theory_text = (
        "<b>Core Concept:</b> When physical robot hardware is absent or unavailable, vision algorithms can be demonstrated directly "
        "on a laptop using the integrated or USB webcam and a local deep learning model.<br/><br/>"
        "<b>Key Concepts to Present:</b><br/>"
        "• <b>Single-Stage Object Detection (YOLO - You Only Look Once):</b> Unlike legacy two-stage detectors (e.g., R-CNN) that first generate region proposals "
        "and then classify them, YOLO reframes detection as a single regression problem. A single convolutional/transformer neural network divides the image into a grid "
        "and predicts bounding boxes, confidence scores, and class labels simultaneously in a single forward pass.<br/>"
        "• <b>Inference Pipeline:</b> Frame Capture (OpenCV) ➔ Tensor Resizing/Normalization ➔ Neural Network Forward Pass ➔ Non-Maximum Suppression (NMS) ➔ Bounding Box Rendering.<br/>"
        "• <b>YOLOv8 Nano (yolov8n):</b> Designed specifically for real-time edge processing and CPU inference (~3.2 million parameters), achieving 30+ FPS even without dedicated GPU."
    )
    story.append(Paragraph(theory_text, body_style))
    story.append(Spacer(1, 10))

    # Comparison Table
    flow_data = [
        ["Metric", "YOLOv8 Nano (yolov8n)", "Full YOLOv8 Extra (yolov8x)"],
        ["Parameters", "~3.2 Million", "~68.2 Million"],
        ["Inference Speed", "Real-time (CPU friendly)", "Requires High-end GPU"],
        [
            "Primary Use Case",
            "Robotics edge devices & laptops",
            "Offline server batch processing",
        ],
    ]
    t = Table(flow_data, colWidths=[130, 200, 200])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#C53030")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 8.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#FFF5F5")),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#FEB2B2")),
            ]
        )
    )
    story.append(t)
    story.append(Spacer(1, 12))

    # 2. Installation & Environment
    story.append(Paragraph("2. Installation & Setup", h2_style))
    setup_cmds = (
        "# Install Ultralytics YOLO and computer vision dependencies\n"
        "pip install ultralytics opencv-python numpy"
    )
    story.append(Paragraph(setup_cmds.replace("\n", "<br/>"), code_style))

    # 3. Execution Commands
    story.append(Paragraph("3. Execution Commands", h2_style))
    run_cmds = (
        "# Run the standalone webcam YOLO script\n"
        "python webcam_vision.py\n\n"
        "# Controls:\n"
        "# Press 'q' inside the video window to quit."
    )
    story.append(Paragraph(run_cmds.replace("\n", "<br/>"), code_style))

    # 4. Troubleshooting & Windows Camera Permissions
    story.append(Paragraph("4. Common Issues & Fixes in Workshop", h2_style))
    troubleshoot = (
        "• <b>'Camera index out of range' or OpenCV backend error:</b><br/>"
        "   - Windows uses DirectShow (<code>cv2.CAP_DSHOW</code>) or MSMF for webcams. The script tests both automatically.<br/>"
        "   - <b>Windows Privacy:</b> Open <b>Windows Settings ➔ Privacy & security ➔ Camera</b>. Ensure <i>'Let desktop apps access your camera'</i> is <b>ON</b>.<br/>"
        "   - Ensure no background apps (Zoom, Teams, Discord, Browser) are currently holding a lock on the webcam.<br/>"
        "• <b>First Run Delay:</b> On first execution, Ultralytics downloads <code>yolov8n.pt</code> (~6 MB) automatically from GitHub."
    )
    story.append(Paragraph(troubleshoot, body_style))

    doc.build(story)
    print(f"Generated {filename}")


if __name__ == "__main__":
    build_pdf_scenario1("Workshop_Scenario_1_Robot_Bridge.pdf")
    build_pdf_scenario2("Workshop_Scenario_2_Local_Webcam_YOLO.pdf")
