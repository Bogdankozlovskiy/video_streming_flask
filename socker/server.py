import cv2
import socket
from pickle import dumps

server = socket.socket()
server.bind(('127.0.0.1', 5000))
server.listen()
client, addr = server.accept()
print(f'accept connect by addr {addr}')


cap = cv2.VideoCapture(0)
while True:
    # Capture frame-by-frame
    _, frame = cap.read()
    data = dumps(frame)
    client.send(data)

cap.release()
