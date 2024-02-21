#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <cstdlib>

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
        if (strcmp(buffer, "100") == 0) {
            system("/home/main/school/junior_second_semester/Software_Eng/lasertag/startScripts/start.sh");
            
        } 
        else if(strcmp(buffer, "101") == 0){
            
        }
        sendto(socketFD, responseMessage, strlen(responseMessage), 0, (struct sockaddr*)&clientAddress, clientAddrLen);
    }

    close(socketFD);
    return 0;
}
