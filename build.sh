#!/bin/bash

# Proceed with installing dependencies sequentially
sudo apt install pip
sudo apt-get update
sudo apt-get install -y xterm
sudo apt install wmctrl

#Install Python dependencies sequentially 
pip install python-dotenv

pip install supabase

pip install pygame







