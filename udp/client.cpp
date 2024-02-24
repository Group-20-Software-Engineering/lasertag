#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <thread>

const int SERVER_PORT = 7501; // Server's listening port
const int LISTEN_PORT = 7500; // Port to listen for broadcasts
const int BUFFER_SIZE = 1024;

// Function to listen for broadcasts
void listenForBroadcasts() {
    int listenFD = socket(AF_INET, SOCK_DGRAM, 0);
    if (listenFD == -1) {
        std::cerr << "Error creating listen socket" << std::endl;
        return;
    }

    int broadcastEnable = 1;
    setsockopt(listenFD, SOL_SOCKET, SO_BROADCAST, &broadcastEnable, sizeof(broadcastEnable));

    struct sockaddr_in listenAddr;
    memset(&listenAddr, 0, sizeof(listenAddr));
    listenAddr.sin_family = AF_INET;
    listenAddr.sin_addr.s_addr = htonl(INADDR_ANY);
    listenAddr.sin_port = htons(LISTEN_PORT);

    if (bind(listenFD, (struct sockaddr*)&listenAddr, sizeof(listenAddr)) == -1) {
        std::cerr << "Error binding listen socket" << std::endl;
        close(listenFD);
        return;
    }

    char buffer[BUFFER_SIZE];
    while (true) {
        struct sockaddr_in fromAddr;
        socklen_t fromAddrLen = sizeof(fromAddr);
        ssize_t receivedBytes = recvfrom(listenFD, buffer, BUFFER_SIZE, 0,
                                         (struct sockaddr*)&fromAddr, &fromAddrLen);

        if (receivedBytes == -1) {
            std::cerr << "Error receiving data" << std::endl;
            continue;
        }

        buffer[receivedBytes] = '\0'; // Null-terminate the received data
        std::cout << "Broadcast received: " << buffer << std::endl;
    }

    close(listenFD);
}

int main() {
    std::thread listener(listenForBroadcasts);

    const char* SERVER_IP = "127.0.0.1"; // Server IP address
    // Create socket for sending to the server
    int socketFD = socket(AF_INET, SOCK_DGRAM, 0);
    if (socketFD == -1) {
        std::cerr << "Error creating socket" << std::endl;
        return 1;
    }

    // Set up server address for sending messages
    struct sockaddr_in serverAddress;
    memset(&serverAddress, 0, sizeof(serverAddress));
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_addr.s_addr = inet_addr(SERVER_IP);
    serverAddress.sin_port = htons(SERVER_PORT);

    char buffer[BUFFER_SIZE];

    while (true) {
        std::cout << "Enter a message (or type 'exit' to quit): ";
        std::cin.getline(buffer, BUFFER_SIZE);

        if (strcmp(buffer, "exit") == 0) {
            break;
        }

        ssize_t sentBytes = sendto(socketFD, buffer, strlen(buffer), 0,
                                   (struct sockaddr*)&serverAddress, sizeof(serverAddress));
        if (sentBytes == -1) {
            std::cerr << "Error sending data" << std::endl;
            continue;
        }
    }

    listener.join(); // Wait for the listener thread to finish
    close(socketFD);
}
