import subprocess
import time
import os
import pytest


class ADBHelper:
    """Helper class for automating mobile testing with ADB commands."""

    def __init__(self):
        """Initialize and check for connected devices."""
        self.devices = self.list_devices()
        if not self.devices:
            print("❌ No ADB devices found. Please connect a device and enable USB debugging.")
            exit(1)
        else:
            print(f"✅ Found devices: {', '.join(self.devices)}")

    def test_run_adb_command(self, command, device=None, timeout=15):
        """Runs an ADB command and returns the output."""
        try:
            adb_command = ["adb"]
            if device:
                adb_command.extend(["-s", device])
            adb_command.extend(command)

            result = subprocess.run(adb_command, capture_output=True, text=True, timeout=timeout)

            if result.returncode != 0:
                print(f"❌ Error running command: {' '.join(adb_command)}\n{result.stderr}")
                return None
            return result.stdout.strip()
        except subprocess.TimeoutExpired:
            print(f"⚠️ Command timed out: {' '.join(command)}")
            return None

    def list_devices(self):
        """Returns a list of connected ADB devices."""
        output = self.run_adb_command(["devices"])
        if output:
            lines = output.split("\n")[1:]
            return [line.split("\t")[0] for line in lines if line.strip()]
        return []

    def get_logcat(self, device):
        """Fetches and saves ADB logcat logs."""
        print(f"📜 Fetching logs from {device}...")
        logs = self.run_adb_command(["logcat", "-d", "-v", "threadtime"], device)
        if logs:
            filename = f"adb_logs_{device}.txt"
            with open(filename, "w") as f:
                f.write(logs)
            print(f"✅ Logs saved to '{filename}'")
        else:
            print("⚠️ No logs captured.")

    def install_apk(self, device, apk_path):
        """Installs an APK on the specified device."""
        if os.path.exists(apk_path):
            print(f"📦 Installing {apk_path} on {device}...")
            self.run_adb_command(["install", apk_path], device)
        else:
            print(f"❌ APK file not found: {apk_path}")

    def uninstall_package(self, device, package_name):
        """Uninstalls an app by package name."""
        print(f"🗑️ Uninstalling {package_name} from {device}...")
        self.run_adb_command(["uninstall", package_name], device)

    def take_screenshot(self, device):
        """Takes a screenshot and saves it locally."""
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        remote_path = f"/sdcard/screenshot_{timestamp}.png"
        local_path = f"screenshot_sample_{device}_{timestamp}.png"

        print(f"📸 Taking screenshot on {device}...")
        self.run_adb_command(["shell", "screencap", "-p", remote_path], device)
        self.run_adb_command(["pull", remote_path, local_path], device)

        if os.path.exists(local_path):
            print(f"✅ Screenshot saved as '{local_path}'")
        else:
            print("❌ Failed to retrieve screenshot.")

    def check_battery(self, device):
        """Fetches battery status of the connected device."""
        print(f"🔋 Checking battery status for {device}...")
        output = self.run_adb_command(["shell", "dumpsys", "battery"], device)
        if output:
            print(f"🔋 Battery Status:\n{output}")

    def get_cpu_memory_usage(self, device, package_name):
        """Fetches CPU and memory usage of a specific app."""
        print(f"📊 Checking CPU & Memory usage for {package_name} on {device}...")
        output = self.run_adb_command(["shell", "dumpsys", "meminfo", package_name], device)
        if output:
            print(f"📊 Memory Info:\n{output}")

    def restart_adb_server(self):
        """Restarts the ADB server."""
        print("🔄 Restarting ADB server...")
        self.run_adb_command(["kill-server"])
        time.sleep(2)
        self.run_adb_command(["start-server"])
        print("✅ ADB server restarted.")

    def perform_ui_test(self, device):
        """Runs a basic UI automation test (Example: Opening Settings)."""
        print(f"🛠️ Running UI automation test on {device}...")
        self.run_adb_command(["shell", "input", "keyevent", "KEYCODE_HOME"], device)
        time.sleep(1)
        self.run_adb_command(["shell", "am", "start", "-a", "android.settings.SETTINGS"], device)
        print("✅ Opened Settings app!")


if __name__ == "__main__":
    adb = ADBHelper()

    for device in adb.devices:
        adb.take_screenshot(device)
        adb.get_logcat(device)
        adb.check_battery(device)
        adb.perform_ui_test(device)

        # Uncomment these to install/uninstall apps
        # adb.install_apk(device, "path/to/your.apk")
        # adb.uninstall_package(device, "com.example.app")

        # Uncomment this to check CPU and memory usage of an app
        adb.get_cpu_memory_usage(device, "com.android.whatsapp.app")

    print("✅ Mobile testing automation completed!")
