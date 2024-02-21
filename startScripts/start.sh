tmux new-session -d -s server-session

tmux send-keys -t server-session "cd ~/school/junior_second_semester/Software_Eng/lasertag/udp" C-m

tmux send-keys -t server-session "g++ start_server.cpp -Wall -o watch_server" C-m

tmux send-keys -t server-session " ~/school/junior_second_semester/Software_Eng/lasertag/udp/watch_server" C-m





