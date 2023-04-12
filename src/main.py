import cv2
import numpy as np

from toolbox import *


def main():

    print("Select what you need to do : ")
    print("1. Rotate")
    print("2. Exit")

    image = cv2.imread('input_image.jpeg')

    usr_input = input()
    if usr_input == "1":
        output_image = rotate_image(image, 45)
    
    elif usr_input == "2":
        output_image = flip_image(image, 'horizontal')
    
    elif usr_input == "3":
        output_image = rotate_image2(image, 45)
    
    elif usr_input == "4":
        output_image = scale_image(image, 1200, 1400)
    
    elif usr_input == "5":
        output_image = linear_gray_level_mapping(image, 1.5, -50)
    
    elif usr_input == "6":
        output_image = power_law_grey_level_mapping(image, 1.0, 2.2)
    
    elif usr_input == "7":
        output_image = calculate_histogram_grayscale(image)
        print(output_image)
    
    elif usr_input == "8":
        output_image = normalize_histogram(image)
    
    elif usr_input == "9":
        kernel = np.array([[1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9]])
        output_image = convolution(image, kernel)
    
    elif usr_input == "10":
        kernel = np.array([[1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9]])
        output_image = convolution_coloured(image, kernel)

    elif usr_input == "11":
        window = (3,3)
        output_image = filtering_grayscale(image, window, "min")
    
    elif usr_input == "12":
        window = (3,3)
        output_image = filtering_rgb(image, window, "min")

    elif usr_input == "99":
        exit()

    cv2.imwrite('output_image.jpeg', output_image)

    print("End of program")





if __name__ == "__main__":
    main()

