cd /home/main/school/junior_second_semester/Software_Eng/lasertag/udp

echo cwd


tmux send-keys -t lasertag-session "g++ server.cpp -Wall -o server"

sleep 3s

tmux send-keys -t  lasertag-session  "./server"
