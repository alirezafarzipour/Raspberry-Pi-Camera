import cv2
from picamera2 import Picamera2
from datetime import datetime

class CameraApp:
    def __init__(self):
        self.piCam = Picamera2()
        self.piCam.preview_configuration.main.size = (1280, 720)
        self.piCam.preview_configuration.main.format = "RGB888"
        self.piCam.preview_configuration.align()
        self.piCam.configure("preview")
        self.piCam.start()

        self.recording = False

    def start_recording(self):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.video_filename = f"video_{timestamp}.mp4"
        self.video_writer = cv2.VideoWriter(self.video_filename, cv2.VideoWriter_fourcc(*'mp4v'), 30.0, (1280, 720))
        self.recording = True

    def end_recording(self):
        self.video_writer.release()
        self.recording = False

    def run(self):
        while True:
            frame = self.piCam.capture_array()

            # Show recording status on the frame
            status_text = "Recording" if self.recording else "Not Recording"
            status_color = (0, 255, 0) if self.recording else (0, 0, 255)
            cv2.putText(frame, status_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, status_color, 2)

        
            cv2.imshow("piCam", frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break
            elif key == ord('s') and not self.recording:
                self.start_recording()
            elif key == ord('e') and self.recording:
                self.end_recording()

            if self.recording:
                self.video_writer.write(frame)

        cv2.destroyAllWindows()

if __name__ == "__main__":
    app = CameraApp()
    app.run()
