# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(("", port))
    # Fill in start
    serverSocket.listen(5)  # The server listens for connection requests from potential clients with a parameter that sets the maximum number of queued connections to 5 Fill in end

    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()  # The accept() method creates a new socket in the server that is dedicated to the connecting clients
        try:

            try:
                message = connectionSocket.recv(4000)  # Size of request message received,in bytes, from the client
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read()  # Read the contents of the file referenced and store it in a variable

                # Send one HTTP header line into socket.
                # Fill in start
                connectionSocket.send(str.encode("HTTP/1.1 200 OK\r\n\r\n"))  # Send a response header to the client. Without the str.encode, it will pass as a binary
                # Fill in end

                # Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())

                connectionSocket.send("\r\n".encode())
                connectionSocket.close()
            except IOError:
                # Send response message for file not found (404)
                # Fill in start
                connectionSocket.send(str.encode("HTTP/1.1 404 Not Found\r\n\r\n")) # Send a response header to the client
                connectionSocket.send(str.encode("<html><head></head><body><h1>Sorry, this page was lost to the void!</h1></body></html>\r\n\r\n"))  # Send a custom responses page to the client
                # Fill in end

                # Close client socket
                # Fill in start
                connectionSocket.close()  # Close the connection socket for the connected clients
                # Fill in end

        except (ConnectionResetError, BrokenPipeError):
            pass

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)
