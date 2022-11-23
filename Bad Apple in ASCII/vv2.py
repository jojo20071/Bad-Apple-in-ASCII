import PIL
from PIL import Image
import os
import numpy as np
import cv2
import time

size = 55
tollerance = 0





cap = cv2.VideoCapture("ba3.mov")

def get_image(path):
    cap.set(1,r5)
    ret, frame = cap.read()
    cv2.imwrite("frame.jpg", frame)
    img = Image.open(path)
    img = img.resize((size,size))
    img = img.convert('L')
    pix = img.load()
    for r in range(size):
        #print(r)
        print(" ")
        for r2 in range(size):
            #print(pix[r,r2])
            if pix[r2,r] > (20):
                #pix[r,r2] = (255)
                print("  ", end = '')
                #print(pix[r2,r],"white")
            else:
                #pix[r2,r1] = (0)
                print("%""%", end = '')
                #print(pix[r,r2],"black")
    #img.save("ma.jpg")

    return img

for r5 in range(1,20000):
    get_image("frame.jpg")
    time.sleep(0.0333)

#get_image("frame.jpg",150)



