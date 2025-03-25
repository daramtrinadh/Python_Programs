import subprocess

class AndroidDevice:
    def __init__(self, device_id=None):
        self.device_id = device_id
        self.adb_command = ["adb"] if not device_id else ["adb", "-s", device_id]
        self.check_adb_device()

    def check_adb_device(self):
        try:
            result = subprocess.run(
                self.adb_command + ["devices"],
                capture_output=True,
                text=True,
                check=True,
                timeout=20
            )
            lines = result.stdout.strip().split('\n')[1:]
            devices = [line.split()[0] for line in lines if 'device' in line]
            if not devices:
                raise Exception("No devices connected or ADB not working. Run 'adb devices' to verify.")
            print(f"ADB Setup Successful. Device(s) detected: {', '.join(devices)}")
        except Exception as e:
            print(f"Error: {e}")
            exit(1)

    def run_adb_command(self, command):
        full_command = self.adb_command + command
        try:
            result = subprocess.run(full_command, capture_output=True, text=True, check=True, timeout=20)
            return result.stdout.strip()
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            print(f"ADB command failed: {e}")
            return None

    def list_devices(self):
        return self.run_adb_command(["devices"])

    def install_app(self, apk_path):
        return self.run_adb_command(["install", apk_path])

    def uninstall_app(self, package_name):
        return self.run_adb_command(["uninstall", package_name])

    def push_file(self, local_path, remote_path):
        return self.run_adb_command(["push", local_path, remote_path])

    def pull_file(self, remote_path, local_path):
        return self.run_adb_command(["pull", remote_path, local_path])

    def reboot_device(self):
        return self.run_adb_command(["reboot"])

    def reboot_to_bootloader(self):
        return self.run_adb_command(["reboot", "bootloader"])

    def reboot_to_recovery(self):
        return self.run_adb_command(["reboot", "recovery"])

    def get_logcat(self):
        return self.run_adb_command(["logcat", "-d"])

    def record_screen(self, remote_path):
        return self.run_adb_command(["shell", "screenrecord", remote_path])

    def capture_screenshot(self, remote_path):
        return self.run_adb_command(["shell", "screencap", remote_path])

    def list_installed_packages(self):
        return self.run_adb_command(["shell", "pm", "list", "packages"])

    def get_device_properties(self):
        return self.run_adb_command(["shell", "getprop"])

    def set_device_property(self, property_name, value):
        return self.run_adb_command(["shell", "setprop", property_name, value])

    def simulate_tap(self, x, y):
        return self.run_adb_command(["shell", "input", "tap", str(x), str(y)])

    def simulate_swipe(self, x1, y1, x2, y2, duration=None):
        command = ["shell", "input", "swipe", str(x1), str(y1), str(x2), str(y2)]
        if duration:
            command.append(str(duration))
        return self.run_adb_command(command)

    def simulate_key_event(self, key_code):
        return self.run_adb_command(["shell", "input", "keyevent", str(key_code)])

    def dump_system_info(self):
        return self.run_adb_command(["shell", "dumpsys"])

    def get_device_state(self):
        return self.run_adb_command(["get-state"])

# Example usage:
if __name__ == "__main__":
    ad = AndroidDevice()
    print(ad.list_devices())
    print(ad.get_device_state())

