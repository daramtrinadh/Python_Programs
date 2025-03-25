import subprocess
import re
import json
import os
from datetime import datetime
import time

class AndroidDevice:
    """Class to handle Android device interaction via ADB."""
    def __init__(self, device_id=None):
        self.device_id = device_id
        self.adb_command = ["adb"] if not device_id else ["adb", "-s", device_id]
        self.check_adb_setup()

    def check_adb_setup(self):
        """Check if ADB is working and device is connected."""
        try:
            devices = subprocess.run(self.adb_command + ["devices"], capture_output=True, text=True, check=True, timeout=10).stdout
            if "device" not in devices:
                raise Exception("No device connected or ADB not working. Run 'adb devices' to verify.")
            print("ADB setup successful. Device detected.")
        except Exception as e:
            print(f"ADB setup error: {e}")
            exit(1)

    def run_adb_command(self, command):
        """Execute an ADB command and return the output."""
        full_command = self.adb_command + command
        try:
            result = subprocess.run(full_command, capture_output=True, text=True, check=True, timeout=10)
            return result.stdout.strip()
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            print(f"ADB command failed: {e}")
            return None

    def capture_logcat(self, duration=5):
        """Capture logcat output for a specified duration."""
        self.run_adb_command(["logcat", "-c"])  # Clear previous logs
        log_output = []
        process = subprocess.Popen(self.adb_command + ["logcat"], stdout=subprocess.PIPE, text=True)
        start_time = time.time()
        try:
            while time.time() - start_time < duration:
                line = process.stdout.readline()
                if line:
                    log_output.append(line.strip())
            process.terminate()
            return "\n".join(log_output)
        except Exception as e:
            print(f"Logcat capture error: {e}")
            process.terminate()
            return None

    def get_device_info(self):
        """Get device information (version, model, resolution)."""
        info = {}
        info["android_version"] = self.run_adb_command(["shell", "getprop", "ro.build.version.release"])
        info["model"] = self.run_adb_command(["shell", "getprop", "ro.product.model"])
        info["resolution"] = self.run_adb_command(["shell", "wm", "size"])
        return {k: v for k, v in info.items() if v}

    def check_camera_hardware(self):
        """Check if the device has a camera using dumpsys media.camera."""
        dumpsys_output = self.run_adb_command(["shell", "dumpsys", "media.camera"])
        if dumpsys_output:
            # Look for camera IDs or indications of camera hardware
            return bool(re.search(r"Camera\s*\d+", dumpsys_output, re.IGNORECASE))
        return False

    def take_picture(self):
        """Simulate taking a picture via ADB (requires camera app to be open)."""
        result = self.run_adb_command(["shell", "input", "keyevent", "27"])  # KEYCODE_CAMERA
        return "Picture taken" if result else "Failed to take picture"

    def set_brightness(self, level):
        """Set screen brightness to a specific level (0-255)."""
        if not 0 <= level <= 255:
            return "Invalid brightness level"
        result = self.run_adb_command(["shell", "settings", "put", "system", "screen_brightness", str(level)])
        return f"Brightness set to {level}" if result else "Failed to set brightness"

class CompatibilityChecker:
    """Class to check device compatibility for testing."""
    def __init__(self, device):
        self.device = device
        self.min_android_version = "5.0"  # Minimum required Android version
        self.required_features = ["camera", "display"]

    def check_compatibility(self):
        """Check if the device is compatible with the testing framework."""
        device_info = self.device.get_device_info()
        compatibility = {"compatible": True, "details": {}}

        # Check Android version
        android_version = device_info.get("android_version", "Unknown")
        try:
            if not android_version or float(android_version.split(".")[0]) < float(self.min_android_version.split(".")[0]):
                compatibility["compatible"] = False
                compatibility["details"]["android_version"] = f"Required: {self.min_android_version}, Found: {android_version}"
        except ValueError:
            compatibility["compatible"] = False
            compatibility["details"]["android_version"] = f"Invalid version format: {android_version}"

        # Check for camera using dumpsys
        has_camera = self.device.check_camera_hardware()
        if not has_camera:
            compatibility["compatible"] = False
            compatibility["details"]["camera"] = "Camera not detected via dumpsys media.camera"
        else:
            print("Camera hardware detected.")

        # Check resolution (basic check for any valid resolution)
        resolution = device_info.get("resolution", "")
        has_display = bool(re.search(r"\d+x\d+", resolution))
        if not has_display:
            compatibility["compatible"] = False
            compatibility["details"]["display"] = "Valid resolution not detected"

        return compatibility

class TestResultLogger:
    """Class to handle logging and saving test results using File Handling."""
    def __init__(self, output_file="test_results.json"):
        self.output_file = output_file
        self.results = []
        self.ensure_directory()

    def ensure_directory(self):
        """Ensure the directory exists for file writing."""
        os.makedirs(os.path.dirname(self.output_file) or ".", exist_ok=True)

    def log_result(self, test_name, status, details):
        """Log a test result with timestamp."""
        result = {
            "test_name": test_name,
            "status": status,
            "details": details,
            "timestamp": datetime.now().isoformat()
        }
        self.results.append(result)
        print(f"Logged: {test_name} - {status} - {details}")

    def save_results(self):
        """Save test results to a JSON file."""
        try:
            with open(self.output_file, "w") as f:
                json.dump(self.results, f, indent=4)
            print(f"Results saved to {self.output_file}")
        except Exception as e:
            print(f"Error saving results: {e}")

class CameraDisplayTester:
    """Class to manage camera and display tests using OOP principles."""
    def __init__(self, device_id=None):
        self.device = AndroidDevice(device_id)
        self.logger = TestResultLogger()
        self.compatibility_checker = CompatibilityChecker(self.device)
        self.log_patterns = {
            "focus": r"Focus\s*:\s*FAILED|Error.*focus",
            "brightness": r"Brightness\s*:\s*FAILED|Error.*brightness"
        }

    def parse_logs(self, log_buffer, test_type):
        """Parse logcat output using Regular Expressions to find issues."""
        if not log_buffer:
            return ["No logs captured"]
        pattern = self.log_patterns.get(test_type, r"Error.*")
        issues = []
        for line in log_buffer.splitlines():
            match = re.search(pattern, line, re.IGNORECASE)
            if match:
                issues.append(match.group(0))
        return issues if issues else ["No issues detected"]

    def test_camera_focus(self):
        """Test camera focus by taking a picture and analyzing logs."""
        print("Testing camera focus...")
        result = self.device.take_picture()
        log_output = self.device.capture_logcat(duration=3)
        if not log_output:
            self.logger.log_result("Camera Focus Test", "FAILED", "Log capture failed")
            return "FAILED", "Log capture failed"

        focus_issues = self.parse_logs(log_output, "focus")
        status = "FAILED" if focus_issues[0] != "No issues detected" else "PASSED"
        details = f"Focus issues: {focus_issues}" if status == "FAILED" else "No focus issues detected"
        self.logger.log_result("Camera Focus Test", status, details)
        return status, details

    def test_display_brightness(self):
        """Test display brightness by setting different levels and analyzing logs."""
        print("Testing display brightness...")
        brightness_levels = [50, 150, 255]
        log_output = ""
        for level in brightness_levels:
            result = self.device.set_brightness(level)
            print(result)
            time.sleep(1)
            log_output += self.device.capture_logcat(duration=2) + "\n"

        if not log_output:
            self.logger.log_result("Display Brightness Test", "FAILED", "Log capture failed")
            return "FAILED", "Log capture failed"

        brightness_issues = self.parse_logs(log_output, "brightness")
        status = "FAILED" if brightness_issues[0] != "No issues detected" else "PASSED"
        details = f"Brightness issues: {brightness_issues}" if status == "FAILED" else "No brightness issues detected"
        self.logger.log_result("Display Brightness Test", status, details)
        return status, details

    def run_all_tests(self):
        """Run compatibility check and all tests if compatible."""
        compatibility = self.compatibility_checker.check_compatibility()
        self.logger.log_result("Compatibility Check", "PASSED" if compatibility["compatible"] else "FAILED", str(compatibility["details"]))

        if not compatibility["compatible"]:
            print("Device is not compatible. Tests aborted.")
            self.logger.save_results()  # Save compatibility result before exiting
            return

        # Only run tests if compatible
        self.test_camera_focus()
        self.test_display_brightness()
        self.logger.save_results()

def main():
    """Main function to execute the testing framework."""
    tester = CameraDisplayTester()
    tester.run_all_tests()
    print("\nTest Summary for QA Team Review:")
    try:
        with open("test_results.json", "r") as f:
            results = json.load(f)
            for result in results:
                print(f"Test: {result['test_name']}, Status: {result['status']}, Details: {result['details']}")
    except FileNotFoundError:
        print("No results file found.")

if __name__ == "__main__":
    main()