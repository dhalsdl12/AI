import pytesseract
import cv2
import matplotlib.pyplot as plt


path = './young.jpg'
image = cv2.imread(path)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
