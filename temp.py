import pywinusb.hid as hid

def create_devices_list():
    devices_list = {}

    # Find all HID devices
    all_devices = hid.HidDeviceFilter().get_devices()

    idx = 0
    for device in all_devices:
        if device.vendor_name and device.product_name:
            identifier = f"{device.vendor_name} {device.product_name}"
        else:
            identifier = "Unknown Device"

        if "gamepad" in identifier.lower():
            device_type = "Gamepad"
        elif "keyboard" in identifier.lower():
            device_type = "Keyboard"
        else:
            device_type = "Other"

        devices_list[idx] = {"type": device_type,
                             "device": device,
                             "id": identifier}
        idx += 1

    return devices_list

# Example usage
devices_list = create_devices_list()
print(devices_list)