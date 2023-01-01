#!/usr/bin/env bash

python3.11 -m venv venv
source ./venv/bin/activate
packages=("xcffib" "cairocffi" "dbus-next" "qtile")
for package in ${packages[@]}
do
    pip install $package
done
