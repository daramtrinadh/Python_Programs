import subprocess
import time
import os
from datetime import datetime


class CameraAutomation:
    def __init__(self, device_id=None):
        """Initialize camera automation with optional specific device ID."""
        self.device_id = device_id
        self.adb_prefix = ["adb"]
        if device_id:
            self.adb_prefix = ["adb", "-s", device_id]

        # Verify ADB connection
        if not self._is_device_connected():
            raise Exception("No device connected or ADB not installed")

    def _is_device_connected(self):
        """Check if a device is connected via ADB."""
        try:
            result = subprocess.run(
                ["adb", "devices"],
                capture_output=True,
                text=True,
                check=False
            )
            return len(result.stdout.strip().split('\n')) > 1
        except Exception:
            return False

    def _run_adb_command(self, command):
        """Run an ADB command and return the result."""
        try:
            result = subprocess.run(
                self.adb_prefix + command,
                capture_output=True,
                text=True,
                check=False
            )
            if result.returncode != 0:
                print(f"Warning: Command returned non-zero exit status {result.returncode}")
                print(f"Error output: {result.stderr}")
            return result.stdout.strip()
        except Exception as e:
            print(f"Error executing command: {e}")
            return ""

    def launch_camera(self):
        """Launch the default camera app."""
        print("Launching camera app...")
        result = self._run_adb_command([
            "shell", "am", "start", "-a", "android.media.action.STILL_IMAGE_CAMERA"
        ])
        # Wait for camera to initialize
        time.sleep(3)
        return result

    def take_picture(self):
        """Simulate pressing the camera button to take a picture."""
        print("Taking picture...")
        result = self._run_adb_command([
            "shell", "input", "keyevent", "KEYCODE_CAMERA"
        ])
        # Wait for photo to be saved
        time.sleep(2)
        return result

    def take_picture_volume_key(self):
        """Alternative method: use volume key to take picture on some devices."""
        print("Taking picture using volume key...")
        result = self._run_adb_command([
            "shell", "input", "keyevent", "KEYCODE_VOLUME_DOWN"
        ])
        time.sleep(2)
        return result

    def take_picture_tap_screen(self, x=540, y=960):
        """Take picture by tapping on the screen (coordinates may vary by device)."""
        print(f"Taking picture by tapping at ({x}, {y})...")
        result = self._run_adb_command([
            "shell", "input", "tap", str(x), str(y)
        ])
        time.sleep(2)
        return result

    def switch_camera(self):
        """Switch between front and back camera."""
        print("Switching camera...")
        # Try standard method first
        result = self._run_adb_command([
            "shell", "input", "keyevent", "KEYCODE_CAMERA_SWITCH"
        ])

        # If that doesn't work, try UI Automator if available
        if not result:
            print("Trying alternative switch method...")
            self._run_adb_command([
                "shell", "input", "swipe", "540", "960", "540", "100", "300"
            ])

        # Give time for camera to switch
        time.sleep(2)
        return result

    def close_camera(self):
        """Close the camera app safely."""
        print("Closing camera app...")
        # First try to go back to home screen
        self._run_adb_command([
            "shell", "input", "keyevent", "KEYCODE_HOME"
        ])

        # Then force stop camera apps (try multiple common package names)
        camera_packages = [
            "com.android.camera",
            "com.android.camera2",
            "com.google.android.GoogleCamera",
            "com.sec.android.app.camera"
        ]

        for package in camera_packages:
            self._run_adb_command([
                "shell", "am", "force-stop", package
            ])

        return True

    def find_latest_photo(self):
        """Find the most recent photo on the device."""
        # Try multiple common photo locations
        photo_locations = [
            "/sdcard/DCIM/Camera",
            "/storage/emulated/0/DCIM/Camera",
            "/sdcard/Pictures/Camera"
        ]

        for location in photo_locations:
            # First check if directory exists
            dir_exists = self._run_adb_command([
                "shell", "ls", location
            ])

            if dir_exists and "No such file" not in dir_exists:
                # Try to find the latest file
                latest_photo = self._run_adb_command([
                    "shell", "ls", "-t", location, "|", "head", "-1"
                ])

                if latest_photo and "No such file" not in latest_photo:
                    print(f"Found latest photo: {latest_photo} in {location}")
                    return f"{location}/{latest_photo}"

        print("Could not find any recent photos")
        return None

    def pull_latest_photo(self, destination_folder="."):
        """Pull the most recent photo from the device."""
        # Create destination folder if it doesn't exist
        os.makedirs(destination_folder, exist_ok=True)

        # Find the latest photo
        source_path = self.find_latest_photo()
        if not source_path:
            print("No photos found to pull")
            return None

        # Create a proper destination path with normalized slashes
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        destination_path = os.path.join(destination_folder, f"photo_{timestamp}.jpg")
        destination_path = destination_path.replace('\\', '/')

        print(f"Pulling photo from {source_path} to {destination_path}")

        # Pull the file
        pull_result = self._run_adb_command([
            "pull", source_path, destination_path
        ])

        if os.path.exists(destination_path):
            print(f"Successfully saved photo to {destination_path}")
            return destination_path
        else:
            print(f"Failed to pull photo. ADB output: {pull_result}")
            return None

    def record_video(self, duration_seconds=10):
        """Start video recording, wait for specified duration, then stop."""
        # Launch camera in video mode
        print(f"Starting video recording for {duration_seconds} seconds...")
        self._run_adb_command([
            "shell", "am", "start", "-a", "android.media.action.VIDEO_CAPTURE"
        ])

        # Wait for camera to initialize
        time.sleep(3)

        # Start recording (press shutter button)
        self._run_adb_command([
            "shell", "input", "keyevent", "KEYCODE_CAMERA"
        ])

        # Wait for specified duration
        for i in range(duration_seconds):
            print(f"Recording: {i + 1}/{duration_seconds} seconds")
            time.sleep(1)

        # Stop recording (press shutter button again)
        self._run_adb_command([
            "shell", "input", "keyevent", "KEYCODE_CAMERA"
        ])

        print("Video recording completed")
        time.sleep(2)  # Wait for video to be saved
        return True

    def set_flash_mode(self, mode="auto"):
        """Set flash mode (on/off/auto) by tapping typical flash button location."""
        print(f"Setting flash mode to {mode}...")
        # Common x,y coordinates for flash button (will vary by device)
        flash_locations = {
            "top_right": (900, 100),
            "top_left": (100, 100)
        }

        # Try tapping both common locations
        for location_name, (x, y) in flash_locations.items():
            print(f"Trying flash button at {location_name}")
            self._run_adb_command([
                "shell", "input", "tap", str(x), str(y)
            ])
            time.sleep(1)

            # For multiple taps to cycle through modes (off->auto->on)
            if mode == "auto":
                # Tap once more to get to auto typically
                self._run_adb_command([
                    "shell", "input", "tap", str(x), str(y)
                ])
            elif mode == "on":
                # Tap twice more to get to on typically
                for _ in range(2):
                    self._run_adb_command([
                        "shell", "input", "tap", str(x), str(y)
                    ])
                    time.sleep(0.5)

        return True


# Example usage
def test_camera_functions():
    try:
        camera = CameraAutomation()

        # Create a folder for downloaded photos
        download_folder = "./downloaded_photos"
        os.makedirs(download_folder, exist_ok=True)

        # Basic photo test
        camera.launch_camera()
        camera.take_picture()

        # Try pulling the photo
        photo_path = camera.pull_latest_photo(download_folder)

        # Try alternative picture-taking methods if first method failed
        if not photo_path:
            print("Trying alternative picture-taking methods...")
            camera.take_picture_volume_key()
            time.sleep(1)
            photo_path = camera.pull_latest_photo(download_folder)

            if not photo_path:
                camera.take_picture_tap_screen()
                time.sleep(1)
                photo_path = camera.pull_latest_photo(download_folder)

        # Close and relaunch for video test
        camera.close_camera()
        time.sleep(2)

        # Try a short video recording
        print("\nTesting video recording...")
        camera.record_video(5)

        # Close camera when done
        camera.close_camera()

        print("\nTests completed. Check the downloaded_photos folder for results.")

    except Exception as e:
        print(f"Error during test: {e}")


if __name__ == "__main__":
    test_camera_functions()