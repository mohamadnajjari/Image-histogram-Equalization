import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('party.jpg',cv2.IMREAD_GRAYSCALE)

def display_image(title, image):
    plt.imshow(image, cmap='gray')  
    plt.title(title)  
    plt.axis('off')  
    plt.show()

def calculate_histogram(image):
    hist, bins = np.histogram(image.flatten(), 256, [0, 256])
    return hist, bins

def plot_histogram(title, hist, bins, color):
    plt.plot(hist, color=color)
    plt.title(title)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.show()

def equalization(image):
    image_hist, image_bins = calculate_histogram(image)

    image = image.astype(np.uint8)
    display_image('Input iamge', image)
    plot_histogram('Input Image Histogram', image_hist, image_bins, 'blue')

    pdf = image_hist / np.sum(image_hist)
    cdf = np.cumsum(pdf)

    equalized_image = np.interp(image.flatten(), image_bins[:-1], cdf * 255).reshape(image.shape).astype(np.uint8)
    equalized_image_hist, equalized_image_bins = calculate_histogram(equalized_image)

    display_image('Equalized iamge', equalized_image)
    plot_histogram('Equalized Image Histogram', equalized_image_hist, image_bins, 'blue')

equalization(image)
