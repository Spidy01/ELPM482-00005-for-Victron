#!/bin/sh
# Run this script on boot to ensure samsung battery support persists after upgrades
set -e
DIR="$(dirname "$0")"
TARGET=/opt/victronenergy/dbus-modbus-client

if ! grep -q '^import samsung_battery' "$TARGET/dbus-modbus-client.py"; then
    echo "Reinstalling samsung battery support" >&2
    "$DIR/install.sh"
fi
