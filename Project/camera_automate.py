import pytest
import subprocess
import time
from unittest.mock import patch, MagicMock
from contextlib import contextmanager

# Import the AndroidDevice class - assuming it's in a file called android_device.py
# If it's in a different file, adjust the import accordingly
from android_device import AndroidDevice


###############################
# Unit Tests                  #
###############################

@pytest.fixture
def mock_subprocess_run():
    """Fixture to mock subprocess.run."""
    with patch('subprocess.run') as mock_run:
        mock_process = MagicMock()
        mock_process.stdout = "List of devices attached\ntest_device_123\tdevice\n"
        mock_process.returncode = 0
        mock_run.return_value = mock_process
        yield mock_run


@pytest.fixture
def test_device_id():
    """Fixture for test device ID."""
    return "test_device_123"


@pytest.fixture
def android_device(mock_subprocess_run, test_device_id):
    """Fixture that returns an AndroidDevice instance."""
    return AndroidDevice(device_id=test_device_id)


class TestAndroidDeviceInit:
    """Tests for AndroidDevice initialization."""

    def test_init_with_device_id(self, mock_subprocess_run, test_device_id):
        """Test initialization with a specific device ID."""
        device = AndroidDevice(device_id=test_device_id)
        assert device.device_id == test_device_id
        assert device.adb_command == ["adb", "-s", test_device_id]

    def test_init_without_device_id(self, mock_subprocess_run):
        """Test initialization without a device ID."""
        device = AndroidDevice()
        assert device.device_id is None
        assert device.adb_command == ["adb"]

    def test_check_adb_device_success(self, mock_subprocess_run, android_device):
        """Test successful ADB device check."""
        # Should not raise an exception
        android_device.check_adb_device()

    def test_check_adb_device_no_devices(self, mock_subprocess_run):
        """Test ADB device check when no devices are connected."""
        mock_subprocess_run.return_value.stdout = "List of devices attached\n"

        with pytest.raises(SystemExit):
            AndroidDevice(device_id="test_device_123")

    def test_check_adb_device_error(self, mock_subprocess_run):
        """Test ADB device check when an error occurs."""
        mock_subprocess_run.side_effect = subprocess.CalledProcessError(1, "adb devices", "Error")

        with pytest.raises(SystemExit):
            AndroidDevice(device_id="test_device_123")


class TestAndroidDeviceCommands:
    """Tests for AndroidDevice ADB commands."""

    def test_run_adb_command_success(self, mock_subprocess_run, android_device, test_device_id):
        """Test successful execution of an ADB command."""
        mock_subprocess_run.return_value.stdout = "Command output"
        result = android_device.run_adb_command(["test", "command"])

        # Verify correct command was constructed
        mock_subprocess_run.assert_called_with(
            ["adb", "-s", test_device_id, "test", "command"],
            capture_output=True, text=True, check=True, timeout=20
        )

        assert result == "Command output"

    def test_run_adb_command_failure(self, mock_subprocess_run, android_device):
        """Test handling of ADB command failure."""
        mock_subprocess_run.side_effect = subprocess.CalledProcessError(1, "command", "Error")

        result = android_device.run_adb_command(["test", "command"])
        assert result is None

    def test_run_adb_command_timeout(self, mock_subprocess_run, android_device):
        """Test handling of ADB command timeout."""
        mock_subprocess_run.side_effect = subprocess.TimeoutExpired("command", 20)

        result = android_device.run_adb_command(["test", "command"])
        assert result is None


class TestAndroidDeviceCameraOperations:
    """Tests for AndroidDevice camera operations."""

    def test_launch_camera_image_mode(self, mock_subprocess_run, android_device, test_device_id):
        """Test launching camera in image capture mode."""
        android_device.launch_camera_image_mode()

        # Verify the correct ADB command was executed
        mock_subprocess_run.assert_called_with(
            ["adb", "-s", test_device_id, "shell", "am", "start", "-a", "android.media.action.IMAGE_CAPTURE"],
            capture_output=True, text=True, check=True, timeout=20
        )

    def test_launch_camera_video_mode(self, mock_subprocess_run, android_device, test_device_id):
        """Test launching camera in video recording mode."""
        android_device.launch_camera_video_mode()

        # Verify the correct ADB command was executed
        mock_subprocess_run.assert_called_with(
            ["adb", "-s", test_device_id, "shell", "am", "start", "-a", "android.media.action.VIDEO_CAPTURE"],
            capture_output=True, text=True, check=True, timeout=20
        )

    def test_simulate_camera_focus(self, mock_subprocess_run, android_device, test_device_id):
        """Test simulating camera focus action."""
        android_device.simulate_camera_focus()

        # Verify the correct ADB command was executed
        mock_subprocess_run.assert_called_with(
            ["adb", "-s", test_device_id, "shell", "input", "keyevent", "KEYCODE_FOCUS"],
            capture_output=True, text=True, check=True, timeout=20
        )

    def test_simulate_camera_shutter(self, mock_subprocess_run, android_device, test_device_id):
        """Test simulating camera shutter action."""
        android_device.simulate_camera_shutter()

        # Verify the correct ADB command was executed
        mock_subprocess_run.assert_called_with(
            ["adb", "-s", test_device_id, "shell", "input", "keyevent", "KEYCODE_CAMERA"],
            capture_output=True, text=True, check=True, timeout=20
        )


class TestAndroidDeviceHighLevelOperations:
    """Tests for AndroidDevice high-level operations."""

    def test_capture_photo(self, android_device):
        """Test the full photo capture process."""
        with patch.object(android_device, 'launch_camera_image_mode') as mock_launch:
            with patch.object(android_device, 'simulate_camera_focus') as mock_focus:
                with patch.object(android_device, 'simulate_camera_shutter') as mock_shutter:
                    with patch('time.sleep') as mock_sleep:
                        android_device.capture_photo()

                        # Verify all methods were called in the correct order
                        mock_launch.assert_called_once()
                        mock_focus.assert_called_once()
                        mock_shutter.assert_called_once()

                        # Verify sleep was called with the correct durations
                        assert mock_sleep.call_count == 3
                        mock_sleep.assert_any_call(2)
                        mock_sleep.assert_any_call(1)

    def test_start_video_recording(self, android_device):
        """Test the full video recording process."""
        with patch.object(android_device, 'launch_camera_video_mode') as mock_launch:
            with patch.object(android_device, 'simulate_camera_shutter') as mock_shutter:
                with patch('time.sleep') as mock_sleep:
                    android_device.start_video_recording(duration=5)

                    # Verify all methods were called in the correct order
                    mock_launch.assert_called_once()
                    assert mock_shutter.call_count == 2  # Once to start, once to stop

                    # Verify sleep was called with the correct durations
                    assert mock_sleep.call_count == 3
                    mock_sleep.assert_any_call(2)  # Wait for camera to open
                    mock_sleep.assert_any_call(5)  # Recording duration
                    mock_sleep.assert_any_call(1)  # Wait for video to be saved

    def test_custom_duration_video_recording(self, android_device):
        """Test video recording with a custom duration."""
        with patch.object(android_device, 'launch_camera_video_mode'):
            with patch.object(android_device, 'simulate_camera_shutter'):
                with patch('time.sleep') as mock_sleep:
                    android_device.start_video_recording(duration=10)

                    # Verify sleep was called with the custom duration
                    mock_sleep.assert_any_call(10)


###############################
# Integration Tests           #
###############################

@pytest.fixture(scope="session")
def real_device_info():
    """Check for real devices and return device info if available."""
    try:
        result = subprocess.run(
            ["adb", "devices"],
            capture_output=True,
            text=True,
            check=True,
            timeout=5
        )
        lines = result.stdout.strip().split('\n')[1:]
        devices = [line.split()[0] for line in lines if 'device' in line]

        if devices:
            return {"available": True, "device_id": devices[0]}
        return {"available": False}
    except Exception:
        return {"available": False}


@pytest.fixture
def real_android_device(real_device_info):
    """Create an AndroidDevice instance with a real device if available."""
    if not real_device_info["available"]:
        pytest.skip("No real Android devices connected")
    return AndroidDevice(device_id=real_device_info["device_id"])


@pytest.mark.integration
class TestAndroidDeviceIntegration:
    """Integration tests for AndroidDevice class with real devices."""

    def test_real_device_detection(self, real_android_device):
        """Test detection of real Android device."""
        real_android_device.check_adb_device()  # Should not raise an exception

    def test_real_camera_image_launch(self, real_android_device):
        """Test launching camera app on real device."""
        result = real_android_device.launch_camera_image_mode()
        assert result is not None

    def test_real_camera_video_launch(self, real_android_device):
        """Test launching video camera app on real device."""
        result = real_android_device.launch_camera_video_mode()
        assert result is not None

    def test_real_camera_focus(self, real_android_device):
        """Test camera focus on real device."""
        result = real_android_device.simulate_camera_focus()
        assert result is not None

    def test_real_camera_shutter(self, real_android_device):
        """Test camera shutter on real device."""
        result = real_android_device.simulate_camera_shutter()
        assert result is not None


###############################
# Performance Tests           #
###############################

@pytest.mark.performance
class TestAndroidDevicePerformance:
    """Performance tests for AndroidDevice class."""

    @pytest.fixture(autouse=True)
    def setup_performance(self, android_device):
        """Setup for performance tests."""
        self.device = android_device
        # Patch all methods that would make actual ADB calls
        patch_targets = [
            'launch_camera_image_mode',
            'launch_camera_video_mode',
            'simulate_camera_focus',
            'simulate_camera_shutter',
            'run_adb_command'
        ]

        self.patches = []
        for target in patch_targets:
            p = patch.object(android_device, target, return_value="Success")
            mock = p.start()
            self.patches.append((p, mock))

        # Also patch time.sleep to avoid actual waiting
        self.sleep_patch = patch('time.sleep')
        self.sleep_mock = self.sleep_patch.start()

        yield

        # Stop all patches
        for p, _ in self.patches:
            p.stop()
        self.sleep_patch.stop()

    def test_capture_photo_performance(self):
        """Test the performance of capturing a photo."""
        import timeit

        # Measure execution time over multiple runs
        iterations = 1000
        execution_time = timeit.timeit(lambda: self.device.capture_photo(), number=iterations)
        avg_time_ms = (execution_time / iterations) * 1000

        # Performance assertion - should execute quickly (under 1ms per call)
        assert avg_time_ms < 1, f"Photo capture too slow: {avg_time_ms:.3f}ms per operation (target: <1ms)"
        print(f"Photo capture performance: {avg_time_ms:.3f}ms per operation")

    def test_start_video_recording_performance(self):
        """Test the performance of starting a video recording."""
        import timeit

        # Measure execution time over multiple runs
        iterations = 1000
        execution_time = timeit.timeit(lambda: self.device.start_video_recording(duration=1), number=iterations)
        avg_time_ms = (execution_time / iterations) * 1000

        # Performance assertion - should execute quickly (under 1ms per call)
        assert avg_time_ms < 1, f"Video recording too slow: {avg_time_ms:.3f}ms per operation (target: <1ms)"
        print(f"Video recording performance: {avg_time_ms:.3f}ms per operation")


###############################
# Parameterized Tests         #
###############################

@pytest.mark.parametrize("duration", [1, 5, 10, 30, 60])
def test_video_recording_durations(android_device, duration):
    """Test video recording with various durations."""
    with patch.object(android_device, 'launch_camera_video_mode'):
        with patch.object(android_device, 'simulate_camera_shutter'):
            with patch('time.sleep') as mock_sleep:
                android_device.start_video_recording(duration=duration)
                mock_sleep.assert_any_call(duration)


if __name__ == "__main__":
    # For manual execution
    pytest.main(["-v", "--color=yes"])