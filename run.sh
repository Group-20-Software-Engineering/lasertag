#!/bin/bash

#./startScripts/compile.sh &

git pull


#Compiles the server and starts in a seperate window
set -e
g++ -Wall udp/server.cpp -o udp/server
g++ -Wall udp/client.cpp -o udp/client



# Start the server in a new xterm window and get its PID.

xterm -e ./udp/server &
server_pid=$!

# Start the client in a new xterm window and get its PID.
# xterm -e ./udp/client &
# client_pid=$!

# Set the directory where the Python file is located
directory="frontend"

# Set the Python file name
filename="main.py"

# Set the Player Entry file name
entry="playentry.py"

# Set the play action file name
playAction="playaction.py"

# Navigate to the specified directory
cd "$directory" || exit

# Run the Python file
python3 "$filename"
while true; do
    python3 "$entry"

    python3 "$playAction"

    play_action_exit_code=$?

    if [ $play_action_exit_code -eq 42 ]; then
         kill $server_pid
        # kill $client_pid
        break
    fi
done





