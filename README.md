# Image-histogram-Equalization
## Overview
This project is a simple Python script that performs histogram equalization on a grayscale image. Histogram equalization is a technique in image processing that enhances the contrast of an image by redistributing pixel intensities. The script uses the OpenCV library for image processing, NumPy for numerical operations, and Matplotlib for visualization.
## Project Structure
The project consists of a single Python script named histogram_equalization.py. The script contains the following main components:
### 1. Loading and Displaying an Image:
The script uses the OpenCV library (cv2) to load a grayscale image from the image. The image is then displayed using Matplotlib (plt.imshow()), ensuring that the colormap is set to 'gray' for proper grayscale representation.
### 2. Utility Functions:
The script defines several utility functions:
display_image(title, image): Displays a grayscale image with a specified title, hiding the axis labels.
calculate_histogram(image): Calculates the histogram of a given grayscale image.
plot_histogram(title, hist, bins, color): Plots a histogram with specified attributes.
### 3. Histogram Equalization Function:
The equalization function takes a grayscale image as input and performs histogram equalization. It displays the input image along with its histogram, calculates the PDF (Probability Density Function) and CDF (Cumulative Distribution Function), applies histogram equalization, and finally displays the equalized image with its histogram.
## Usage
To use this project, follow these steps:
### 1.Ensure you have Python installed on your system.
### 2.Install the required libraries
### 3.Download the script
### 4.Run the script
Feel free to experiment with different images and modify the script to suit your needs!


