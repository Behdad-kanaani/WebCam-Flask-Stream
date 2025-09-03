# ------------------------------------------------------------------------------
# Author: Behdad Kanaani
# GitHub: https://github.com/Behdad-kanaani
# Description: This Flask app streams video from a webcam in MJPEG format.
# It also monitors the local IP address and restarts the Flask server if the IP changes.
# ------------------------------------------------------------------------------
from flask import Flask, Response
import cv2
import threading
import socket
import subprocess
import time

app = Flask(__name__)

# Connect to the default webcam (usually the internal webcam on a laptop)
cap = cv2.VideoCapture(0)  # 0 represents the default camera

# Resize the image to 640x480 for better performance and reduced load
frame_width = 640
frame_height = 480

# Set the frame width and height
cap.set(3, frame_width)  # Set the frame width
cap.set(4, frame_height)  # Set the frame height

# Variable to store the current frame
frame = None
lock = threading.Lock()  # Lock to handle concurrency when accessing the frame

# Function to get the current local IP address of the machine
def get_current_ip():
    hostname = socket.gethostname()  
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Function to monitor IP address changes and restart the Flask server when it changes
def monitor_ip_change():
    current_ip = get_current_ip()  # Get the current IP address
    while True:
        new_ip = get_current_ip()  # Get the new IP address
        if new_ip != current_ip:  # If the IP has changed
            print(f"IP address has changed: {current_ip} -> {new_ip}")
            current_ip = new_ip
            # Restart the Flask server upon IP change
            subprocess.Popen(["python", "app.py"])  # Assuming your file is named app.py
            break
        time.sleep(10)  # Check the IP every 10 seconds

# Function to generate frames for streaming in MJPEG format
def generate_frames():
    global frame
    while True:
        ret, new_frame = cap.read()  # Read a frame from the webcam
        if not ret:
            print("Failed to capture frame from camera")
            break
        
        # Use a lock to ensure thread-safe access to the frame
        with lock:
            frame = new_frame.copy()

        # Compress the frame into JPEG format with 50% quality
        ret, buffer = cv2.imencode('.jpg', new_frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
        if ret:
            # Yield the frame in MJPEG format for streaming
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n\r\n')

# Route to stream video on '/video' endpoint
@app.route('/video')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Run the Flask application on port 5000
if __name__ == '__main__':
    # Start a separate thread to monitor IP address changes
    threading.Thread(target=monitor_ip_change, daemon=True).start()
    app.run(host='0.0.0.0', port=5000, threaded=True)

# Close any OpenCV windows if open
cv2.destroyAllWindows()
