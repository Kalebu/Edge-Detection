import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_edge(image):
    ''' Detecting Edges '''
    image_with_edges = cv2.Canny(image , 100, 200)
    images = [image , image_with_edges]
    location = [121, 122]
    for loc, img in zip(location, images):
        plt.subplot(loc)
        plt.imshow(img, cmap='gray')
    plt.savefig('edge.png')
    plt.show()

image = cv2.imread('road.jpg', 0)
detect_edge(image)
