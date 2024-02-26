#!/bin/bash

# Start compile.sh in the background since it runs indefinitely


# Proceed with installing dependencies sequentially
sudo apt-get update
sudo apt-get install -y xterm

#Install Python dependencies sequentially 
pip install python-dotenv

pip install supabase

pip install pygame





