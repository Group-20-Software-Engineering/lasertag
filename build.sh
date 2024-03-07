#!/bin/bash

# Proceed with installing dependencies sequentially
sudo apt-get update
sudo apt-get install -y xterm


#Install Python dependencies sequentially 
pip install python-dotenv

pip install supabase

pip install pygame

#Initalize the Pipes

# Check if the named pipe exists, and if not, create it


PIPE_PATH="udp/pipe"
if [[ ! -p $PIPE_PATH ]]; then
    mkfifo $PIPE_PATH
    echo "Named pipe $PIPE_PATH created."
else
    echo "Named pipe $PIPE_PATH already exists."
fi








