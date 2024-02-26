#!/bin/bash
#Compiles the server and starts in a seperate window
set -e
g++ -Wall udp/server.cpp -o udp/server
g++ -Wall udp/client.cpp -o udp/client

xterm -e ./udp/server&
xterm -e ./udp/client&
