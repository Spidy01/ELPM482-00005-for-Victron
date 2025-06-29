# ELPM482-00005-for-Victron

This package installs support for Samsung ELPM482-00005 batteries on Victron GX
devices. It adds a new `samsung_battery` module to Victron's
`dbus-modbus-client` service and patches `dbus-modbus-client.py` so the module
is imported automatically.

## Installation
1. Copy this repository to your GX device.
2. Run `./install.sh` to copy `samsung_battery.py` to
   `/opt/victronenergy/dbus-modbus-client` and patch `dbus-modbus-client.py`
   with `import samsung_battery`.
3. Optionally, arrange for `check_install.sh` to run at boot (for example from
   `/data/rc.local`). It will reinstall the files if the import line is removed
   during a system update.
