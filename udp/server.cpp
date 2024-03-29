#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <unordered_map>
#include <fstream>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <cerrno>
#include <cstring>
#include <string>
//Bind server receive port 7501 do not bind 7500 broadcast but still create it
//127.0.0.1

const int PORT = 7501;
const int BROADCAST_PORT = 7500;
const int BUFFER_SIZE = 1024;
int shooterID, killedID;


void printMapContents(const std::unordered_map<int, std::string>& map) {
    for (const auto& pair : map) {
        std::cout << "Machine ID: " << pair.first << ", Player ID: " << pair.second << std::endl;
    }
}

int pipeInsert(const std::string& shooterCodename, const std::string& killedCodename) {
    const char* pipePath = "pipe";
    int fd = open(pipePath, O_WRONLY | O_NONBLOCK);
    if (fd == -1) {
        std::cerr << "Error opening pipe: " << std::strerror(errno) << std::endl;
        return 1; // Failure
    }

    // Format the message with codenames instead of IDs
    std::string message = shooterCodename + "/" + killedCodename + "\n";
    ssize_t bytesWritten = write(fd, message.c_str(), message.length());
    if (bytesWritten == -1) {
        std::cerr << "Error writing to pipe: " << std::strerror(errno) << std::endl;
        close(fd);
        return 1;
    }

    close(fd);
    return 0;
}





int main() {
    int socketFD = socket(AF_INET, SOCK_DGRAM, 0);
    if (socketFD == -1) {
        std::cerr << "Error creating socket" << std::endl;
        return 1;
    }

    //Enables Broadcasting
    int broadcastEnable=1;
    if(setsockopt(socketFD, SOL_SOCKET, SO_BROADCAST, &broadcastEnable, sizeof(broadcastEnable)) == -1){
        std::cerr << "Error setting socket to broadcast" << std::endl;
        close(socketFD);
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

    std::unordered_map<int, std::string> machineToPlayerMap;


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
           
             int machineID;
            char playerCodenameBuffer[128]; // Make sure the buffer is large enough for the codename
            sscanf(buffer, "Hardware/%d/%s", &machineID, playerCodenameBuffer);
            std::string playerCodename(playerCodenameBuffer);
            machineToPlayerMap[machineID] = playerCodename;
            printMapContents(machineToPlayerMap);
            



            // std::string playerCodename;
            // sscanf(buffer, "Hardware/%d/%s", &machineID, &playerCodename);
            // machineToPlayerMap[machineID] = playerCodename; 
            // printMapContents(machineToPlayerMap); 
            
         

            // Broadcast the ID to all clients right now it only echos back to the client
            struct sockaddr_in broadcastAddress;
            memset(&broadcastAddress, 0, sizeof(broadcastAddress));
            broadcastAddress.sin_family = AF_INET;
            broadcastAddress.sin_port = htons(BROADCAST_PORT);
            broadcastAddress.sin_addr.s_addr = inet_addr("127.0.0.1");

            //Converts machineID to a char so it can be broadcasted
            char idBuffer[32];
            snprintf(idBuffer, sizeof(idBuffer),"%d",machineID);


            sendto(socketFD, idBuffer, strlen(idBuffer), 0, (struct sockaddr*)&broadcastAddress, sizeof(broadcastAddress));
        } 

        // Else-if block to handle "id/id" format
    // Else-if block to handle "id/id" format
        else if (sscanf(buffer, "%d/%d", &shooterID, &killedID) == 2) {
    auto shooterEntry = machineToPlayerMap.find(shooterID);
    auto killedEntry = machineToPlayerMap.find(killedID);
    if (shooterEntry != machineToPlayerMap.end() && killedEntry != machineToPlayerMap.end()) {
        // Found both shooter's and killed's player codenames in the map
        const std::string& playerShooterCodename = shooterEntry->second;
        const std::string& playerKilledCodename = killedEntry->second;
        std::cout << "Shooter Player Codename: " << playerShooterCodename << ", Killed Player Codename: " << playerKilledCodename << std::endl;
        
        // Assuming pipeInsert function needs to be updated to handle std::string instead of int
        // You will need to adjust the pipeInsert function accordingly if it is supposed to accept player codenames as strings.
        pipeInsert(playerShooterCodename, playerKilledCodename);
    } else {
        if (shooterEntry == machineToPlayerMap.end()) {
            std::cerr << "Shooter machine ID " << shooterID << " not found in player map." << std::endl;
        }
        if (killedEntry == machineToPlayerMap.end()) {
            std::cerr << "Killed machine ID " << killedID << " not found in player map." << std::endl;
        }
    }
}


        

        sendto(socketFD, responseMessage, strlen(responseMessage), 0, (struct sockaddr*)&clientAddress, clientAddrLen);

    }

    close(socketFD);
    return 0;
}
