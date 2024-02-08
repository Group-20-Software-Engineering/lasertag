#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <fstream>




const int SERVER_PORT = 12345;
const int BUFFER_SIZE = 1024;

int main() {
    std::ifstream din;
    din.open("hostname.txt"); //open the hostname file
    std::string hostname; 
    getline(din, hostname); //Getline doesn't like the type
    const int length = hostname.length();
    char* hostname_char = new char[length + 1]; //length +1 for null terminator
    strcpy(hostname_char, hostname.c_str()); //copy

    std::cout << "Hostname: ";
    for (int i = 0; i < length; i++) // print the char array
    { 
        std::cout << hostname_char[i]; 
    } 

    const char* SERVER_IP = hostname_char;
    // Create socket
    int clientSocket = socket(AF_INET, SOCK_DGRAM, 0);
    if (clientSocket == -1) {
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

    while (true) {
        // Get user input
        std::cout << "Enter a message (or type 'exit' to quit): ";
        std::cin.getline(buffer, sizeof(buffer));

        // Check for exit command
        if (strcmp(buffer, "exit") == 0) {
            break;
        }

        // Send the message to the server
        ssize_t sentBytes = sendto(clientSocket, buffer, strlen(buffer), 0,
                                   (struct sockaddr*)&serverAddress, sizeof(serverAddress));
        if (sentBytes == -1) {
            std::cerr << "Error sending data" << std::endl;
            continue;
        }

        // Receive the response from the server (optional)
        struct sockaddr_in serverResponseAddress;
        socklen_t serverResponseAddrLen = sizeof(serverResponseAddress);
        ssize_t receivedBytes = recvfrom(clientSocket, buffer, sizeof(buffer), 0,
                                         (struct sockaddr*)&serverResponseAddress, &serverResponseAddrLen);

        if (receivedBytes == -1) {
            std::cerr << "Error receiving data" << std::endl;
            continue;
        }

        // Print the server's response
        buffer[receivedBytes] = '\0'; // Null-terminate the received data
        std::cout << "Server response: " << buffer << std::endl;
    }

    // Close the socket
    close(clientSocket);

    return 0;
}

