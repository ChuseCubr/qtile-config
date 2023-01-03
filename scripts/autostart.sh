#!/usr/bin/env bash

picom -b
blueman-applet &
nm-applet &
flatpak run com.github.wwmm.easyeffects &
discord &
rclone --vfs-cache-mode writes mount "APC":  ~/APC &
