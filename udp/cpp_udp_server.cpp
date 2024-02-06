#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>

const int PORT = 12345;
const int BUFFER_SIZE = 1024;

int main() {
    // Create socket
    int serverSocket = socket(AF_INET, SOCK_DGRAM, 0);
    if (serverSocket == -1) {
        std::cerr << "Error creating socket" << std::endl;
        return 1;
    }

    // Set up server address
    struct sockaddr_in serverAddress;
    memset(&serverAddress, 0, sizeof(serverAddress));
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_addr.s_addr = INADDR_ANY;
    serverAddress.sin_port = htons(PORT);

    // Bind the socket to the specified port
    if (bind(serverSocket, (struct sockaddr*)&serverAddress, sizeof(serverAddress)) == -1) {
        std::cerr << "Error binding socket" << std::endl;
        close(serverSocket);
        return 1;
    }

    std::cout << "UDP Server is listening on port " << PORT << std::endl;

    char buffer[BUFFER_SIZE];

    while (true) {
        // Receive data
        struct sockaddr_in clientAddress;
        socklen_t clientAddrLen = sizeof(clientAddress);
        ssize_t receivedBytes = recvfrom(serverSocket, buffer, sizeof(buffer), 0,
                                        (struct sockaddr*)&clientAddress, &clientAddrLen);

        if (receivedBytes == -1) {
            std::cerr << "Error receiving data" << std::endl;
            continue;
        }

        // Print received data
        buffer[receivedBytes] = '\0'; // Null-terminate the received data
        std::cout << "Received from " << inet_ntoa(clientAddress.sin_addr) << ":" << ntohs(clientAddress.sin_port)
                  << " - " << buffer << std::endl;

        // Send a response (optional)
        const char* responseMessage = "Hello, client! I received your message.";
        sendto(serverSocket, responseMessage, strlen(responseMessage), 0,
               (struct sockaddr*)&clientAddress, sizeof(clientAddress));
    }

    // Close the socket
    close(serverSocket);

    return 0;
}

