#!/usr/local/bin/python3
import os
import cv2
import numpy as np

#doesn't match up well with gimp?
def getWhiteRGB(image):
    white_lo=np.array([229,229,229]) #about 90%
    white_hi=np.array([255,255,255])
    wCount=cv2.countNonZero(cv2.inRange(image,white_lo,white_hi))
    #print(f"White count: {wCount}")
    return wCount

def getBlackRGB(image):
    black_lo=np.array([0,0,0])
    black_hi=np.array([26,26,26]) #about 10%
    bCount=cv2.countNonZero(cv2.inRange(image,black_lo,black_hi))
    #print(f"Black count: {bCount}")
    return bCount

def getWhiteV(image):
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    white_lo=np.array([0,0,229]) #about 90%
    white_hi=np.array([255,255,255])
    wCount=cv2.countNonZero(cv2.inRange(hsv_img,white_lo,white_hi))
    #print(f"White by value count: {wCount}")
    return wCount

def getBlackV(image):
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    black_lo=np.array([0,0,0])
    black_hi=np.array([255,255,26]) #about 10%
    bCount=cv2.countNonZero(cv2.inRange(hsv_img,black_lo,black_hi))
    #print(f"Black by value  count: {bCount}")
    return bCount

def getColorCount(image,hr,hg,hb,lr,lg,lb):
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    color_lo = np.array([lr,lg,lb])
    color_hi = np.array([hr,hg,hb])
    cCount=cv2.countNonZero(cv2.inRange(rgb_image,color_lo,color_hi))
    return cCount

def getRedHigh(image): #90 percent
    rCount=getColorCount(image,255,255,255,229,0,0)
    #print(f"Red count over 90%: {rCount}")
    return rCount

def getBlueHigh(image): #90 percent
    bCount=getColorCount(image,255,255,255,0,0,229)
    #print(f"Blue count over 90%: {bCount}")
    return bCount

def getGreenHigh(image): #90 percent
    gCount=getColorCount(image,255,255,255,0,229,0)
    #print(f"Green count over 90%: {gCount}")
    return gCount

def getRedLow(image): #10 percent
    rCount=getColorCount(image,26,255,255,0,0,0)
    #print(f"Red count under 10%: {rCount}")
    return rCount

def getBlueLow(image): #10 percent
    bCount=getColorCount(image,255,255,26,0,0,0)
    #print(f"Blue count under 10%: {bCount}")
    return bCount

def getGreenLow(image): #10 percent
    gCount=getColorCount(image,255,26,255,0,0,0)
    #print(f"Green count under 10%: {gCount}")
    return gCount

def getSaturationHigh(image): #90 percent
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    sat_lo=np.array([0,229,0])
    sat_hi=np.array([255,255,255]) #about 10%
    sCount=cv2.countNonZero(cv2.inRange(hsv_img,sat_lo,sat_hi))
    #print(f"Sat high count: {sCount}")
    return sCount

def getSaturationLow(image): #10 percent
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    sat_lo=np.array([0,0,0])
    sat_hi=np.array([255,26,255]) #about 10%
    sCount=cv2.countNonZero(cv2.inRange(hsv_img,sat_lo,sat_hi))
    #print(f"Sat low count: {sCount}")
    return sCount

f= open("data_l.csv","w")
os.chdir('imgs/')
f.write("filename,white_rgb,black_rgb,white_value,black_value,red_high,red_low,green_high,green_low,blue_high,blue_low,saturation_high,saturation_low\n")
for file in os.listdir('.'):
    filename = os.fsdecode(file)
    if(filename.endswith('.jpg')):
        try:
            image = cv2.imread(filename)
            height, width = image.shape[:2]
            pixelCount = height*width
            #print(f"PixelCount: {pixelCount}")
            #print(f"Image: {filename}")
            wrgb=(getWhiteRGB(image)/pixelCount)
            brgb=(getBlackRGB(image)/pixelCount)
            wv=(getWhiteV(image)/pixelCount)
            bv=(getBlackV(image)/pixelCount)
            rh=(getRedHigh(image)/pixelCount)
            rl=(getRedLow(image)/pixelCount)
            gh=(getGreenHigh(image)/pixelCount)
            gl=(getGreenLow(image)/pixelCount)
            bh=(getBlueHigh(image)/pixelCount)
            bl=(getBlueLow(image)/pixelCount)
            sh=(getSaturationHigh(image)/pixelCount)
            sl=(getSaturationLow(image)/pixelCount)
            f.write(f"{filename},")
            f.write(f"{wrgb},")
            f.write(f"{brgb},")
            f.write(f"{wv},")
            f.write(f"{wv},")
            f.write(f"{bv},")
            f.write(f"{rh},")
            f.write(f"{rl},")
            f.write(f"{gh},")
            f.write(f"{gl},")
            f.write(f"{bh},")
            f.write(f"{bl},")
            f.write(f"{sh},")
            f.write(f"{sl}\n")
        except Exception as e:
            print(e)
f.close


