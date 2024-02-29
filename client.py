import base64
import socket
import cv2
import numpy

RHOST = '127.0.0.1'
RPORT = 4444
ADDRESS = (RHOST, RPORT)

BUF_SIZE = 65535

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUF_SIZE)
sock.sendto(b"Hello", ADDRESS)

while True:
    data, addr = sock.recvfrom(BUF_SIZE)
    data = base64.b64decode(data)
    npdata = numpy.frombuffer(data, dtype=numpy.uint8)
    frame = cv2.imdecode(npdata, cv2.IMREAD_COLOR)
    cv2.imshow("RECEIVE", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break