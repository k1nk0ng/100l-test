#!/usr/bin/python3

import sys
import pytesseract as tsr
import cv2
import numpy as np
import imutils

def test1(img):
    # Load an image
    #img = cv2.imread('circle1.jpg')
    img1 = img.copy()

    # Resize an image
    if img1.shape[1] > 600:
        img1 = imutils.resize(img1, width=600)
    clone = img1.copy()

    # Convert to grayscale
    gray = cv2.cvtColor(clone, cv2.COLOR_BGR2GRAY)
     
    # Threshold grayscaled image to get binary image
    ret,gray_threshed = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
     
    # Smooth an image
    bilateral_filtered_image = cv2.bilateralFilter(gray_threshed, 5, 175, 175)
     
    # Find edges
    edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)
     
    # Find contours
    contours, _= cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     
    contour_list = []
    for contour in contours:
        approx = cv2.approxPolyDP(contour,0.3*cv2.arcLength(contour,True),True)
        area = cv2.contourArea(contour)
        if ((len(approx) > 8) & (50000 > area > 10000) ):
            contour_list.append(contour)
    print(contour_list)
     
    # Draw contours
    cv2.drawContours(clone, contour_list, -1, (255,0,0), 2)
     
    # Displaying the results
    #cv2.imshow("Original", img)
    cv2.imshow('Smooth', bilateral_filtered_image)
    #cv2.imshow('Edge', edge_detected_image)
    cv2.imshow('Objects Detected',clone)
    cv2.waitKey(0)

def get_name():
    if len(sys.argv[1:]) == 1:
        return sys.argv[1]
    else:
        print('wrong arguments')
        exit(1)

def test2(img):
    clone = img.copy()

    # Преобразовать в оттенки серого.
    gray = cv2.cvtColor(clone, cv2.COLOR_BGR2GRAY)

    # Blur используя ядро 3 * 3.
    gray_blurred = cv2.blur(gray, (3, 3))

    # Применить преобразование Хафа на размытое изображение.
    detected_circles = cv2.HoughCircles(gray_blurred, 
                       cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
                       param2 = 30, minRadius = 5, maxRadius = 40)

    # Нарисуйте круги, которые обнаружены.
    if detected_circles is not None:
        # Преобразовать параметры круга a, b и r в целые числа.
        detected_circles = np.uint16(np.around(detected_circles))
    return detected_circles

def test3(img):
    clone = img.copy()
    gray = cv2.cvtColor(clone, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 20, 250, apertureSize = 3)
    lines = cv2.HoughLines(canny, 1, np.pi/180, 10, 10, 120)
    _lines = lines.tolist()
    if len(_lines) > 1:
        return 'x'
    else:
        return None

def to_chk(file_name=None):
    if file_name is None:
        file_name = get_name()
    img = cv2.imread(file_name, cv2.IMREAD_COLOR)
    res = test2(img)
    if res is not None and len(res[0]) == 1:
        return 'o'
    else:
        res = test3(img)
        if res is not None:
            return res
    return 'Check error'

if __name__ == '__main__':
        to_chk()
        exit(1)
