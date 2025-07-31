# ADB Command Tool

A simple Python script for interacting with Android devices using ADB (Android Debug Bridge) commands. This tool allows users to collect logs, perform reboots, pull bug reports, and more, from Android devices connected via USB or network.

## Features

- Pull Bug Reports from connected devices
- Reboot Devices
- Collect various logs (Android, QXDM, Audio Dump, etc.)
- Flash ROMs (System, Bootloader, Radio)
- Control ADB server (kill or refresh)
- Change working directory for ADB operations

## Requirements

- Python 3.x
- ADB installed on your system (`adb` command must be available in terminal)
- Connected Android device(s) with USB debugging enabled

## Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/OmerShareif/my_adb_tool.git
   cd your-project-directory

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt

3. **Ensure ADB is Installed:**
    ```bash
    adb version
 
