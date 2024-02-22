import socket

server_ip = '170.176.232.159'
port = 7500
message = ''

def send_udp_packet(server_ip, port, message):
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

# Replace 'localhost' with your server's IP address if it's not running locally
server_ip = '170.176.232.159'
port = 7500
message = '100'

send_udp_packet(server_ip, port, message)
