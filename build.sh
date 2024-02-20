#!/bin/bash
set -e
g++ -Wall udp/server.cpp -o udp/server
g++ -Wall udp/client.cpp -o udp/client
./udp/client
xterm -e ./udp/server