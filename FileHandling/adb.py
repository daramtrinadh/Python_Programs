import subprocess


def list_adb_devices():
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)

    if result.returncode != 0:  # Check if ADB command failed
        print("Error: ADB command failed. Ensure ADB is installed and running.")
        return []

    lines = result.stdout.strip().split("\n")[1:]
    devices = [line.split("\t")[0] for line in lines if line.strip()]

    return devices


def log_file():
    try:
        results = subprocess.run(["adb", "logcat", "-d", "-v", "threadtime"], capture_output=True, text=True,
                                 timeout=10)
        lines = results.stdout.strip().split("\n")  # Don't skip first line
        logs = [line for line in lines if line.strip()]  # Store log lines
        return logs
    except subprocess.TimeoutExpired:
        print("Error: ADB logcat timed out.")
        return []


# Get and print ADB devices
devices = list_adb_devices()
if devices:
    print("Connected ADB Devices:")
    for device in devices:
        print(f"- {device}")
else:
    print("No devices found.")

# Get and save logcat output
logs = log_file()
if logs:
    print("Saving logs to 'adb_logs.txt'...")
    with open("adb_logs.txt", "w") as f:
        f.write("\n".join(logs))
    print("Logs saved successfully.")
else:
    print("No logs captured.")
