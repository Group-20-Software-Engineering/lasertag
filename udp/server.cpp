#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>

//Bind server receive port 7501 do not bind 7500 but still create it
//127.0.0.1

const int PORT = 7501;
const int BUFFER_SIZE = 1024;

int main() {
    int socketFD = socket(AF_INET, SOCK_DGRAM, 0);
    if (socketFD == -1) {
        std::cerr << "Error creating socket" << std::endl;
        return 1;
    }

    struct sockaddr_in serverAddress;
    memset(&serverAddress, 0, sizeof(serverAddress));
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_addr.s_addr = INADDR_ANY;
    serverAddress.sin_port = htons(PORT);

    if (bind(socketFD, (struct sockaddr*)&serverAddress, sizeof(serverAddress)) == -1) {
        std::cerr << "Error binding socket" << std::endl;
        close(socketFD);
        return 1;
    }

    std::cout << "UDP Server is listening on port " << PORT << std::endl;

    char buffer[BUFFER_SIZE];
    while (true) {
        struct sockaddr_in clientAddress;
        socklen_t clientAddrLen = sizeof(clientAddress);
        ssize_t receivedBytes = recvfrom(socketFD, buffer, BUFFER_SIZE, 0, (struct sockaddr*)&clientAddress, &clientAddrLen);
        if (receivedBytes == -1) {
            std::cerr << "Error receiving data" << std::endl;
            continue;
        }

        buffer[receivedBytes] = '\0'; // Null-terminate the received data
        std::cout << "Received: " << buffer << std::endl;

        // Respond based on the received message
        const char* responseMessage = "Default response";
        if (strcmp(buffer, "202") == 0) {
            responseMessage = "Hello, client! Welcome to laser hair removal inc.";
        } else if (strcmp(buffer, "221") == 0) {
            responseMessage = "Hello, client! Looks like the game is over.";
        }
        else if (strncmp(buffer, "Hardware/", 9) == 0) {
            char* id = buffer + 9; // Get the ID part of the message
            std::cout << "Received Hardware ID: " << id << std::endl;

            // Broadcast the ID to all clients right now it only echos back to the client
            sendto(socketFD, id, strlen(id), 0, (struct sockaddr*)&clientAddress, clientAddrLen);
        } 

        sendto(socketFD, responseMessage, strlen(responseMessage), 0, (struct sockaddr*)&clientAddress, clientAddrLen);
    }

    close(socketFD);
    return 0;
}
