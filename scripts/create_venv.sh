#!/usr/bin/env bash

python3.11 -m venv ~/.config/qtile/venv
source ~/.config/qtile/venv/bin/activate
packages=("xcffib" "cairocffi" "dbus-next" "qtile")
for package in ${packages[@]}
do
    pip install $package
done
# git clone https://github.com/qtile/qtile.git
# cd qtile
# pip install .
# cd ..
