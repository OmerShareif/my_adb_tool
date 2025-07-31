
import subprocess

def check_adb():
    try:
        subprocess.run(['adb', 'version'], check=True)
        return True
    except subprocess.CalledProcessError:
        print("ADB not found or not installed.")
        return False

def get_connected_device():
    result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')[1:]  # skip first line
    devices = [line.split('\t')[0] for line in lines if 'device' in line]
    return devices[0] if devices else None


def get_bugreport(device_serial):
    print(f"Pulling bugreport from device: {device_serial}")
    subprocess.run(['adb', '-s', device_serial, 'bugreport', f'bugreport_{device_serial}.zip'])

def reboot_device(device_serial):
    print(f"Rebooting device: {device_serial}")
    subprocess.run(['adb', '-s', device_serial, 'reboot'])