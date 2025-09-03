# WebCam=Flask-Stream 🎥

WebCam-Flask-Stream is a lightweight webcam streaming application built with **Flask**. This app streams real-time video from your webcam in **MJPEG format**, ideal for low-latency live streaming. It is **fully optimized for use on Android devices** with **Pydroid 3**, but can also run on other platforms such as **Windows**, **Linux**, and **macOS**. The app automatically monitors IP changes and restarts the Flask server if the IP changes, ensuring uninterrupted streaming. 🚀

## Features 🌟

- **Live Webcam Stream**: Streams real-time video from your webcam in MJPEG format. Perfect for web-based video applications with low latency. 🌐
- **Automatic IP Monitoring**: The app continuously monitors your local IP address. If the IP changes, the server is automatically restarted. 🔄
- **Optimized Performance**: The video stream is resized to **640x480** to ensure smooth performance, especially when running on mobile devices via **Pydroid 3**. 📱
- **Cross-Platform Support**: Works on Android (Pydroid 3), Windows, Linux, and macOS. 🖥️

![License](https://img.shields.io/github/license/Behdad-kanaani/WebCam=Flask-Stream?style=flat-square)
![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat-square)
![OpenCV](https://img.shields.io/badge/OpenCV-%2B%20MJPEG-brightgreen?style=flat-square)

## Installation 🛠️

### **Setting up on Android with Pydroid 3**

1. **Clone or Download the Repository**:
   Clone the repo using Git, or download the ZIP file and extract it:

   ```bash
   git clone https://github.com/Behdad-kanaani/WebCam-Flask-Stream.git
   cd WebCam-Flask-Stream
````

2. **Install Required Dependencies**:
   In the terminal of **Pydroid 3**, install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask Application**:
   After the dependencies are installed, you can start the Flask server with:

   ```bash
   python app.py
   ```

4. **Access the Webcam Stream**:
   Open your browser (on the same device or any device connected to the same network) and go to:

   ```
   http://<your-ip-address>:5000/video
   ```

   Replace `<your-ip-address>` with the IP address of your Android device. To find your IP address in Pydroid 3's terminal, use:

   ```bash
   ip addr show
   ```

### **Setting up on Windows, Linux, or macOS**

1. **Clone or Download the Repository**:
   Clone or download the ZIP file and extract it:

   ```bash
   git clone https://github.com/Behdad-kanaani/WebCam=Flask-Stream.git
   cd WebCam=Flask-Stream
   ```

2. **Install Dependencies**:
   Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask Application**:
   Start the Flask server:

   ```bash
   python app.py
   ```

4. **Access the Webcam Stream**:
   Open any browser and go to:

   ```
   http://<your-ip-address>:5000/video
   ```

   Replace `<your-ip-address>` with the IP address of the server (on Windows, `localhost` can also be used).

## Usage 🖥️

* **Viewing the Webcam Stream**: Once the Flask server is running, you can view the live webcam stream at `http://<your-ip-address>:5000/video`.
* **Automatic IP Monitoring**: The app continuously checks for changes in your local IP address. If a change is detected (e.g., when you reconnect to Wi-Fi), the server will restart and the stream will continue without interruptions.

### Example Usage:

1. After running the server, open your browser on any device connected to the same network and navigate to:

   ```
   http://<your-ip-address>:5000/video
   ```
   for exaple :
   ```
   http://1.1.1.1:5000/video
   ```

3. If the device's IP address changes (for example, when switching networks), the server will restart automatically, keeping the stream live.

حتماً! در اینجا فقط بخش **Screenshot** که می‌خواهید به `README.md` اضافه کنید آمده است:

---

## License 📜

This project is licensed under the **AGPL 3.0 License**. See the [LICENSE](LICENSE) file for more details.

## Troubleshooting ⚠️

* **No Video Stream**: Make sure your webcam is properly connected and accessible. If running on Pydroid 3, ensure the app has permission to access your camera.

* **IP Change Detection Not Working**: Ensure your device is connected to a stable network. The app checks for IP changes every 10 seconds. If you experience issues, try restarting the app or reconnecting to the network.
