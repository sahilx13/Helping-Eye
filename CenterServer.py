# This script contains server code which is ready to communicate securely with a drone
# @author Sahil Sharma
# @group - JanhiTech

import socket
import pickle
import struct

class Server:
    def __init__(self, host="127.0.0.1", port=65001):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen()
        print('listening on', (host, port))

    def start(self):
        # accept drone connection request
        conn, addr = self.sock.accept()
        data = ""
        payload_size = struct.calcsize("H")
        while len(data) < payload_size:
            data += conn.recv(4096)
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("H", packed_msg_size)[0]
        while len(data) < msg_size:
            data += conn.recv(4096)
        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data)
        print("Video received from Drone, closing the connection")
        self.stop()
        return frame

    def stop(self):
        self.sock.close()
