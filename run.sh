#!/bin/bash

./startScripts/compile.sh &

# Set the directory where the Python file is located
directory="frontend"

# Set the Python file name
filename="main.py"

# Navigate to the specified directory
cd "$directory" || exit

# Run the Python file
python3 "$filename"
