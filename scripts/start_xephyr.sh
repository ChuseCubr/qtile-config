#!/usr/bin/env bash

source ~/.config/qtile/venv/bin/activate
Xephyr -br -ac -noreset -screen 1200x900 :2 &
DISPLAY=:2 python ~/.config/qtile/venv/bin/qtile start
