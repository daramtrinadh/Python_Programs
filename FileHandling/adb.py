import subprocess
import time
import os


def run_adb_command(command):
    """Runs an ADB command and returns the output."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=15)
        if result.returncode != 0:
            print(f"Error running command: {' '.join(command)}\n{result.stderr}")
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        print(f"Error: Command {' '.join(command)} timed out.")
        return None


def list_adb_devices():
    """Lists connected ADB devices."""
    output = run_adb_command(["adb", "devices"])
    if output:
        lines = output.split("\n")[1:]
        devices = [line.split("\t")[0] for line in lines if line.strip()]
        return devices
    return []


def get_logcat():
    """Fetches and saves ADB logcat logs."""
    logs = run_adb_command(["adb", "logcat", "-d", "-v", "threadtime"])
    if logs:
        with open("today_logs.txt", "w") as f:
            f.write(logs)
        print("Logs saved to 'adb_logs.txt'")
    else:
        print("No logs captured.")


def install_apk(device, apk_path):
    """Installs an APK on the specified device."""
    print(f"Installing {apk_path} on {device}...")
    run_adb_command(["adb", "-s", device, "install", apk_path])


def uninstall_package(device,package_name):
    """Uninstalls an app by package name from the specified device."""
    print(f"Uninstalling {package_name} from {device}...")
    run_adb_command(["adb", "-s", device, "uninstall", package_name])


def take_screenshot():
    """Takes a screenshot and pulls it to the local machine."""
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    remote_path = f"/sdcard/screenshot_{timestamp}.png"
    local_path = f"screenshot_{timestamp}.png"

    print(f"Taking screenshot on {device}...")
    run_adb_command(["adb", "-s", device, "shell", "screencap", "-p", remote_path])
    run_adb_command(["adb", "-s", device, "pull", remote_path, local_path])

    if os.path.exists(local_path):
        print(f"Screenshot saved as {local_path}")
    else:
        print("Failed to retrieve screenshot.")


def restart_adb_server():
    """Restarts the ADB server."""
    print("Restarting ADB server...")
    run_adb_command(["adb", "kill-server"])
    time.sleep(2)
    run_adb_command(["adb", "start-server"])


if __name__ == "__main__":
    restart_adb_server()
    devices = list_adb_devices()

    if devices:
        print("Connected ADB Devices:")
        for device in devices:
            print(f"- {device}")
            take_screenshot()
            get_logcat()
            # install_apk(device, "path/to/your.apk")  # Uncomment to install APK
            # uninstall_package(device, "com.example.app")  # Uncomment to uninstall
    else:
        print("No devices found.")
