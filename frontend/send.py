import socket

def send_udp_packet(message, server_ip='127.0.0.1', port=7501):
   
    # Create a socket object for UDP communication
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Send the message to the server
        sock.sendto(message.encode(), (server_ip, port))
        
        # Optionally, receive a response from the server
        # Increase the buffer size if you expect longer responses
        response, _ = sock.recvfrom(4096)
        print("Server response:", response.decode())
    finally:
        # Close the socket to clean up resources
        sock.close()


