
import sys
from device_utils import check_adb, get_connected_device, get_bugreport

def main():
    if not check_adb():
        return

    device = get_connected_device()
    if not device:
        print("No connected devices found.")
        return

    print(f"Connected device: {device}")
    print("Options:")
    print("1. Get Bugreport")
    print("2. Reboot")
    choice = input("Choose an option: ")

    if choice == '1':
        get_bugreport(device)
    elif choice == '2':
        import subprocess
        subprocess.run(['adb', '-s', device, 'reboot'])
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
