import socket

HEADER = 64
PORT =  5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def sendMessages(aMessage):
    message = aMessage.encode(FORMAT)
    messageLength = len(aMessage)
    sendLength = str(messageLength).encode(FORMAT)
    sendLength += b' ' * (HEADER - len(sendLength))
    client.sendMessages(sendLength)
    client.sendMessages(message)

print("Hello World")
input()
print("How is it going?")
input()
print("Very Good TNX")
sendMessages(DISCONNECT_MESSAGE)