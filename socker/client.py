import socket
from pickle import loads
import cv2

client = socket.socket()
client.connect(('127.0.0.1',5000))

while True:
	frame = client.recv(921764)
	frame = loads(frame)
	cv2.imshow('Frame',frame)
	if cv2.waitKey(1) == ord('q'):
		break
cv2.destroyAllWindows()
