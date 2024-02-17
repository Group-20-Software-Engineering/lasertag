#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>

const int SERVER_PORT = 7501; // Server's listening port
const int BUFFER_SIZE = 1024;

int main() {
    const char* SERVER_IP = "170.176.232.159"; // Server IP address
    // Create socket
    int socketFD = socket(AF_INET, SOCK_DGRAM, 0);
    if (socketFD == -1) {
        std::cerr << "Error creating socket" << std::endl;
        return 1;
    }

    // Set up server address
    struct sockaddr_in serverAddress;
    memset(&serverAddress, 0, sizeof(serverAddress));
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_addr.s_addr = inet_addr(SERVER_IP);
    serverAddress.sin_port = htons(SERVER_PORT);

    char buffer[BUFFER_SIZE];
    struct sockaddr_in fromAddress;
    socklen_t fromAddressLen = sizeof(fromAddress);

    while (true) {
        std::cout << "Enter a message (or type 'exit' to quit): ";
        std::cin.getline(buffer, BUFFER_SIZE);

        // Check for exit command
        if (strcmp(buffer, "exit") == 0) {
            break;
        }

        // Send the message to the server
        ssize_t sentBytes = sendto(socketFD, buffer, strlen(buffer), 0,
                                   (struct sockaddr*)&serverAddress, sizeof(serverAddress));
        if (sentBytes == -1) {
            std::cerr << "Error sending data" << std::endl;
            continue;
        }

        std::cout << "Message sent, waiting for server response..." << std::endl;

        // Receive the response from the server
        ssize_t receivedBytes = recvfrom(socketFD, buffer, BUFFER_SIZE, 0,
                                         (struct sockaddr*)&fromAddress, &fromAddressLen);

        if (receivedBytes == -1) {
            std::cerr << "Error receiving data" << std::endl;
            continue;
        }

        // Print the server's response
        buffer[receivedBytes] = '\0'; // Null-terminate the received data
        std::cout << "Server response: " << buffer << std::endl;
    }

    // Close the socket
    close(socketFD);

    return 0;
}
