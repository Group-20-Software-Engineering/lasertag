#!/bin/bash

#./startScripts/compile.sh &


#Compiles the server and starts in a seperate window
set -e
g++ -Wall udp/server.cpp -o udp/server
g++ -Wall udp/client.cpp -o udp/client



# Start the server in a new xterm window and get its PID.

xterm -e ./udp/server &
server_pid=$!

# Start the client in a new xterm window and get its PID.
xterm -e ./udp/client &
client_pid=$!

# Set the directory where the Python file is located
directory="frontend"

# Set the Python file name
filename="main.py"

# Set the play action file name
playAction="playaction.py"

# Navigate to the specified directory
cd "$directory" || exit

# Run the Python file
python3 "$filename"

python3 "$playAction"

kill $server_pid
kill $client_pid




