#!/bin/bash
set -e
hostname -I | awk '{print $1}' > hostname.txt
./client