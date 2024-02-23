#!/bin/bash

# Start compile.sh in the background since it runs indefinitely
./startScripts/compile.sh &

# Proceed with installing dependencies sequentially
sudo apt-get update
sudo apt-get install -y xterm
# No need for sleep after installation commands; each command will finish before the next starts

pip install python-dotenv
# Each pip install will start after the previous install finishes

pip install supabase

pip install pygame

# No wait is necessary for compile.sh as it runs indefinitely

# Set the directory where the Python file is located
directory="frontend"

# Set the Python file name
filename="main.py"

# Navigate to the specified directory
cd "$directory" || exit

# Run the Python file
python3 "$filename"

