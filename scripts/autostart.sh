#!/usr/bin/env bash

picom -b
blueman-applet &
nm-applet &
flatpak run com.github.wwmm.easyeffects &
discord &
fusermount -uz ~/APC || true
rclone --vfs-cache-mode writes mount "APC":  ~/APC &
