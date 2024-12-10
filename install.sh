#!/bin/sh

sudo apt update
sudo apt upgrade -y

# install ffmpeg
sudo apt install ffmpeg

# install pangocairo
sudo apt install libpango1.0-dev -y
sudo apt install libcairo2-dev libjpeg-dev libgif-dev

python -m pip install manim