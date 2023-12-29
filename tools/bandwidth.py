import socket

# Server details
server_ip = "127.0.0.1"  # Replace with your server's IP
server_port = 2911

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Example message to send
message = "{\"bandwidth\":1000000}"

# Send the message to the server
client_socket.sendto(message.encode(), (server_ip, server_port))
print(f"Message sent to server: {message}")

# Close the socket
client_socket.close()
