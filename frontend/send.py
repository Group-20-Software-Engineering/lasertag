import os
import socket

def send_udp_packet(message, server_ip='127.0.0.1', port=7501):
    # Create a socket object for UDP communication
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Send the message to the server
        sock.sendto(message.encode(), (server_ip, port))
        
        # Optionally, receive a response from the server
        response, _ = sock.recvfrom(4096)
        print("Server response:", response.decode())
    finally:
        # Close the socket to clean up resources
        sock.close()


def pipeRemove():
    # Get the current file's directory
    current_dir = os.path.dirname(__file__)
    # Construct the pipe_path dynamically relative to the current file's location
    pipe_path = os.path.join(current_dir, '..', 'udp', 'pipe')
    
    # Ensure the named pipe exists before attempting to open it
    if not os.path.exists(pipe_path):
        os.mkfifo(pipe_path)
        print(f"Named pipe created at: {pipe_path}")

    try:
        # Open the named pipe in read mode
        with open(pipe_path, 'r') as pipeIn:
            while True:
                playerID = pipeIn.readline().strip()
                if playerID:
                    print(f"Received player ID: {playerID}")
                    return playerID
                    
                else:
                    break
    except FileNotFoundError:
        print(f"Error: {pipe_path} not found")
    except Exception as e:
        print(f"Error: {e}")


# def main():
#     send_udp_packet("Hardware/22/YEET")
#     send_udp_packet("Hardware/11/YAGA")
#     while True:  
#         pipeRemove()

# if __name__ == "__main__":
#     main()
