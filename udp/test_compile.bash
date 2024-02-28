#!/bin/bash

#Used to compile the code and run the server locally, not in a seperate window
g++ client.cpp -Wall -o client
g++ server.cpp -Wall -o server

./server