# This contains the code running on Drones
import socket
import pickle
import struct
import cv2

class Client:
    def __init__(self, videoCaptured):
        self.cap = cv2.VideoCapture(videoCaptured)
        self.clientsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.clientsock.connect(('localhost', 65001))

    def connect(self):
        while True:
            net, frame = self.cap.read()
            data = pickle.dumps(frame)
            self.clientsock.sendall(struct.pack("H", len(data))+data)