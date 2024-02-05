import socket
import threading

HEADER = 64
PORT =  5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handleClient(conn, addr): 
   print("[NEW CONNECTION] " + addr + " connected." )
   connected = True
   while connected:
    msgLength = conn.recv(HEADER).decode(FORMAT)
    if msgLength:
      
      msgLength = int(msgLength)
      msg = conn.recv(msgLength).decode(FORMAT)
      if msg == DISCONNECT_MESSAGE:
         connected = False
      print(f"[{addr}] {msg}")
      conn.sendMessages("Msg received ".encode(FORMAT))
   conn.close()



def start():
  server.listen()
  print(f"[LISTENING] server is listening {server}.")
  while (True):
    conn, addr = server.accept()
    thread = threading.Thread(target = handleClient, args = (conn, addr))
    thread.start(
      print("[ACTIVE CONNECTIONS] " + threading.activeCount() - 1)
    )

print("[STARTING] server is starting...")
start()