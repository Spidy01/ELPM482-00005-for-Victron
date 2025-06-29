#!/bin/sh
set -e
TARGET=/opt/victronenergy/dbus-modbus-client
THIS_DIR="$(dirname "$0")"

mkdir -p "$TARGET"
install -m 0644 "$THIS_DIR/samsung_battery.py" "$TARGET/"

# ensure import line is present
if ! grep -q '^import samsung_battery' "$TARGET/dbus-modbus-client.py"; then
    sed -i '/import victron_em/a import samsung_battery' "$TARGET/dbus-modbus-client.py"
fi

echo "Samsung battery support installed to $TARGET"
