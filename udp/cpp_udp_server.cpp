#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>

const int PORT = 25565; //make this 7501 later
const int sendPort = 8123; //make this 7500 later
const int BUFFER_SIZE = 1024;

int main() {
//--------------------------------------------------------------------------------------------------------
//Socket to LISTEN
    // Create socket
    int receiveSocket = socket(AF_INET, SOCK_DGRAM, 0);
    if (receiveSocket == -1) {
        std::cerr << "Error creating receive socket" << std::endl;
        return 1;
    }
    
    // Set up server address
    struct sockaddr_in receiveAddress;
    memset(&receiveAddress, 0, sizeof(receiveAddress));
    receiveAddress.sin_family = AF_INET;
    receiveAddress.sin_addr.s_addr = INADDR_ANY;
    receiveAddress.sin_port = htons(PORT);

    // Bind the socket to the specified port
    if (bind(receiveSocket, (struct sockaddr*)&receiveAddress, sizeof(receiveAddress)) == -1) {
        std::cerr << "Error binding socket" << std::endl;
        close(receiveSocket);
        return 1;
    }

    std::cout << "UDP Server is listening on port " << PORT << std::endl;

//--------------------------------------------------------------------------------------------------------
//Socket to SEND BACK
    // Create socket
    int sendSocket = socket(AF_INET, SOCK_DGRAM, 0);
    if (sendSocket == -1) {
        std::cerr << "Error creating send socket" << std::endl;
        return 1;
    }
    // Set up server address
        struct sockaddr_in sendAddress;
        memset(&sendAddress, 0, sizeof(sendAddress));
        sendAddress.sin_family = AF_INET;
        sendAddress.sin_addr.s_addr = INADDR_ANY;
        sendAddress.sin_port = htons(sendPort);

        // Bind the socket to the specified port
        if (bind(sendSocket, (struct sockaddr*)&sendAddress, sizeof(sendAddress)) == -1) {
            std::cerr << "Error binding socket" << std::endl;
            close(sendSocket);
            return 1;
        }

        std::cout << "UDP Server is sending on port " << sendPort << std::endl;
//--------------------------------------------------------------------------------------------------------
//Handle operation 
    char buffer[BUFFER_SIZE];

    while (true) {
        const char* responseMessage;
        // Receive data
        struct sockaddr_in clientAddress;
        socklen_t clientAddrLen = sizeof(clientAddress);
        ssize_t receivedBytes = recvfrom(receiveSocket, buffer, sizeof(buffer), 0,
                                        (struct sockaddr*)&clientAddress, &clientAddrLen);

        if (receivedBytes == -1) {
            std::cerr << "Error receiving data" << std::endl;
            continue;
        }

        // Print received data
        buffer[receivedBytes] = '\0'; // Null-terminate the received data
        std::cout << "Received from " << inet_ntoa(clientAddress.sin_addr) << ":" << ntohs(clientAddress.sin_port)
                  << " - " << buffer << std::endl;

        if(strcmp(buffer,"202")== 0)
        {
            responseMessage = "Hello, client! Welcome to laser hair removal inc.";
            sendto(sendSocket, responseMessage, strlen(responseMessage), 0,
               (struct sockaddr*)&clientAddress, sizeof(clientAddress));
            break;
        }
        else if(strcmp(buffer,"221")== 0)
        {
            responseMessage = "Hello, client! Looks like the game is over.";
            sendto(sendSocket, responseMessage, strlen(responseMessage), 0,
               (struct sockaddr*)&clientAddress, sizeof(clientAddress));
            break;
        }

        // Send a response (optional)
        responseMessage = buffer;
        sendto(sendSocket, responseMessage, strlen(responseMessage), 0,
               (struct sockaddr*)&clientAddress, sizeof(clientAddress));
    }

    // Close the sockets
    close(sendSocket);
    close(receiveSocket);


    return 0;
}

