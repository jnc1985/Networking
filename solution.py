from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n Hello From NYU!"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, 1025))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '220':
        #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    #print('Sending E-mail...')
    mailpackage = "MAIL FROM: jnc5@nyu.edu\r\n"
    clientSocket.send(mailpackage.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(recv2)
    #if recv2[:3] != '250':
        #print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    #print('Sending RCPT TO...')
    envelope = "RCPT TO: jnc5@nyu.edu\r\n"
    clientSocket.send(envelope.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print(recv3)
    #if recv3[:3] != '250':
        #print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    #print('Sending Data...')
    sendData = "DATA\r\n"
    clientSocket.send(sendData.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print(recv4)
    #if recv4[:3] != '354':  # 354 Start mail input
        #print('354 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(bytes(msg, "UTF-8"))
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(bytes(endmsg, "UTF-8"))
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    #print('Quiting Connection...')
    endCommand = "QUIT\r\n"
    clientSocket.send(endCommand.encode())
    recv5 = clientSocket.recv(1024).decode()
    #print(recv5)
    #if recv5[:3] != '221':  # 221 Closing channel ack
        #print('221 reply not received from server.')
    # Fill in end

    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
