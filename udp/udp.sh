#!/bin/bash


#Compiles the server and starts in a seperate window
set -e
g++ -Wall server.cpp -o server
g++ -Wall client.cpp -o client



# Start the server in a new xterm window and get its PID.

xterm -e ./server &
server_pid=$!

# Start the client in a new xterm window and get its PID.
xterm -e ./client &
client_pid=$!