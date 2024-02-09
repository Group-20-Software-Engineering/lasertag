#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <fstream>




const int sendPort = 25565;
const int receivePort = 25565;
const int BUFFER_SIZE = 1024;

int main() {
    const char* SERVER_IP = "170.176.232.159";
    // Create socket
    int sendSocket = socket(AF_INET, SOCK_DGRAM, 0);
    if (sendSocket == -1) {
        std::cerr << "Error creating socket" << std::endl;
        return 1;
    }

    // Set up server address
    struct sockaddr_in sendAddress;
    memset(&sendAddress, 0, sizeof(sendAddress));
    sendAddress.sin_family = AF_INET;
    sendAddress.sin_addr.s_addr = inet_addr(SERVER_IP);
    sendAddress.sin_port = htons(sendPort);
    char sendBuffer[BUFFER_SIZE];

    //Create recive socket
    int receiveSocket = socket(AF_INET, SOCK_DGRAM, 0);
    if (receiveSocket == -1) {
        std::cerr << "Error creating socket" << std::endl;
        return 1;
    }

    char receiveBuffer[BUFFER_SIZE];
    

    while (true) {
        // Get user input
        std::cout << "Enter a message (or type 'exit' to quit): ";
        std::cin.getline(sendBuffer, sizeof(sendBuffer));

        // Check for exit command
        if (strcmp(sendBuffer, "exit") == 0) {
            break;
        }

        // Send the message to the server
        ssize_t sentBytes = sendto(sendSocket, sendBuffer, strlen(sendBuffer), 0,
                                   (struct sockaddr*)&sendAddress, sizeof(sendAddress));
        if (sentBytes == -1) {
            std::cerr << "Error sending data" << std::endl;
            continue;
        }

        // // Receive the response from the server (optional)
        // struct sockaddr_in receiveAddress;
        std::cout << "Waiting for server response..." << std::endl;

            // Set up server address
        struct sockaddr_in receiveAddress;
        memset(&receiveAddress, 0, sizeof(receiveAddress));
        receiveAddress.sin_family = AF_INET;
        receiveAddress.sin_addr.s_addr = inet_addr(SERVER_IP);
        receiveAddress.sin_port = htons(receivePort);
        
        socklen_t receiveAddressLen = sizeof(receiveAddress);
        ssize_t receivedBytes = recvfrom(receiveSocket, receiveBuffer, sizeof(receiveBuffer), 0,
                                         (struct sockaddr*)&receiveAddress, &receiveAddressLen);
                                         

        if (receivedBytes == -1) {
            std::cerr << "Error receiving data" << std::endl;
            continue;
        }

        // Print the server's response
        receiveBuffer[receivedBytes] = '\0'; // Null-terminate the received data
        std::cout << "Server response: " << receiveBuffer << std::endl;
    }

    // Close the socket
    close(sendSocket);
    close(receiveSocket);

    return 0;
}

