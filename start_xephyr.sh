#!/usr/bin/env bash

# source ~/projects/qtile-config/venv/bin/activate
Xephyr -br -ac -noreset -screen 1200x900 :2 &
DISPLAY=:2 qtile start -c ./config.py
