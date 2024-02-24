#!/bin/bash

# Start compile.sh in the background since it runs indefinitely
./startScripts/compile.sh &

# Proceed with installing dependencies sequentially
sudo apt-get update
sudo apt-get install -y xterm

#Install Python dependencies sequentially 
pip install python-dotenv

pip install supabase

pip install pygame


# Set the directory where the Python file is located
directory="frontend"

# Set the Python file name
filename="main.py"

# Navigate to the specified directory
cd "$directory" || exit

# Run the Python file
python3 "$filename"

