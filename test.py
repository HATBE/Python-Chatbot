import socket

def start_echo_server(host='127.0.0.1', port=65432):
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        try:
            # Bind the socket to the address and port
            server_socket.bind((host, port))
            # Listen for incoming connections
            server_socket.listen()
            print(f'Server started and listening on {host}:{port}')
            
            while True:
                # Accept a connection
                client_socket, client_address = server_socket.accept()
                print(f'Accepted connection from {client_address}')
                with client_socket:
                    buffer = ""
                    while True:
                        # Receive data from the client
                        data = client_socket.recv(1024).decode('utf-8')
                        if not data:
                            print('No data received. Closing connection.')
                            break
                        
                        buffer += data
                        # Check if a newline is in the buffer
                        if '\n' in buffer:
                            message, buffer = buffer.split('\n', 1)
                            print(f'Received message: {message}')
                            # Send the same data back to the client (echo)
                            client_socket.sendall((message + '\n').encode('utf-8'))
                            print(f'Sent message: {message}')
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    start_echo_server()