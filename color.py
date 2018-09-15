import cv2
import urllib
import numpy as np
stream = urllib.urlopen('http://192.168.137.64:8080/shot.jpg')
bytes = ''
while(1):
    bytes += stream.read(1024)
    a = bytes.find(b'\xff\xd8')
    b = bytes.find(b'\xff\xd9')
    if a != -1 and b != -1:
        jpg = bytes[a:b+2]
        bytes = bytes[b+2:]
        frame = cv2.imdecode((np.fromstring(jpg, dtype=np.uint8)), cv2.IMREAD_COLOR)
    #imgu = urllib.urlopen(url)
    #imgr = np.array(bytearray(imgu.read()),dtype=np.uint8)
    #frame = cv2.imdecode(imgr, -1)
    #frame = cv2.VideoCapture('http://192.168.137.64:8080/shot.jpg')
    #cv2.imshow('test', frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
    