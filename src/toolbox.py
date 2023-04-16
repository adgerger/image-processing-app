
import math
import numpy as np

def filtering_rgb(image, window_size, filter_type):

    # Get image dimensions
    image_height, image_width, _ = image.shape

    # Calculate padding size
    pad_height = window_size[0] // 2
    pad_width = window_size[1] // 2

    # Initialize the output filtered image
    output_image = np.zeros(image.shape, dtype=float)

    # Perform max filtering for each color channel
    for channel in range(3):
        # Apply zero padding to the color channel
        padded_image = np.pad(image[:, :, channel], ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=0)

        # Perform max filtering on the color channel
        for i in range(image_height):
            for j in range(image_width):
                if filter_type == "min":
                    output_image[i, j, channel] = np.min(padded_image[i:i+window_size[0], j:j+window_size[1]])
                elif filter_type == "max":
                    output_image[i, j, channel] = np.max(padded_image[i:i+window_size[0], j:j+window_size[1]])
                elif filter_type ==  "median":
                    output_image[i, j, channel] = np.median(padded_image[i:i+window_size[0], j:j+window_size[1]])
                    
    return output_image



def filtering_grayscale(image, window_size, filter_type):
    image = rgb_to_grayscale(image)

    # Get image dimensions
    image_height, image_width = image.shape

    # Calculate padding size
    pad_height = window_size[0] // 2
    pad_width = window_size[1] // 2

    # Apply zero padding to the image
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=0)

    # Initialize the output filtered image
    output_image = np.zeros((image_height, image_width), dtype=float)

    # Perform max filtering
    for i in range(image_height):
        for j in range(image_width):
            if filter_type == "min":
                output_image[i, j] = np.min(padded_image[i:i+window_size[0], j:j+window_size[1]])
            elif filter_type == "max":
                output_image[i, j] = np.max(padded_image[i:i+window_size[0], j:j+window_size[1]])        
            elif filter_type == "median":
                output_image[i, j] = np.median(padded_image[i:i+window_size[0], j:j+window_size[1]])        
                

    return output_image    



def convolution_coloured(image, kernel):
    
    # Get image and kernel dimensions
    image_height, image_width, _ = image.shape
    kernel_height, kernel_width = kernel.shape

    # Calculate padding size
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2

    # Initialize the output convolved image
    output_image = np.zeros(image.shape, dtype=float)

    # Perform convolution for each color channel
    for channel in range(3):
        # Apply zero padding to the color channel
        padded_image = np.pad(image[:, :, channel], ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=0)

        # Perform convolution on the color channel
        for i in range(image_height):
            for j in range(image_width):
                output_image[i, j, channel] = np.sum(padded_image[i:i+kernel_height, j:j+kernel_width] * kernel)

    return output_image 


def convolution(image, kernel):
    image = rgb_to_grayscale(image)

    # Get image and kernel dimensions
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape

    # Calculate padding size
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2

    # Apply zero padding to the image
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=0)

    # Initialize the output convolved image
    output_image = np.zeros((image_height, image_width), dtype=float)

    # Perform convolution
    for i in range(image_height):
        for j in range(image_width):
            output_image[i, j] = np.sum(padded_image[i:i+kernel_height, j:j+kernel_width] * kernel)

    return output_image


# maybe change it to support coloured images as well
def normalize_histogram(image):
    histogram = calculate_histogram_grayscale(image)
    
    # Calculate the cumulative distribution function (CDF)
    cdf = np.cumsum(histogram)
    cdf_min = np.min(cdf[cdf > 0])

    # Calculate the equalization mapping
    equalization_mapping = (cdf - cdf_min) * 255 / (image.size - cdf_min)
    equalization_mapping = equalization_mapping.astype(np.uint8)

    # Apply the equalization mapping to the image
    equalized_image = equalization_mapping[image]

    return equalized_image



def calculate_histogram_rgb(image):
    # Initialize the histograms for each color channel with zeros
    histograms = np.zeros((3, 256), dtype=np.int64)

    # Calculate the histograms for each color channel
    for row in image:
        for pixel in row:
            for channel in range(3):
                histograms[channel, pixel[channel]] += 1
    
    return histograms


def calculate_histogram_grayscale(image):

    image = rgb_to_grayscale(image)

    # Initialize the histogram with zeros
    histogram = np.zeros(256, dtype=np.int64)

    # Calculate the histogram
    for row in image:
        for pixel_value in row:
            histogram[pixel_value] += 1

    return histogram



def power_law_grey_level_mapping(image, c, gamma):
    image = rgb_to_grayscale(image)
    
    # Normalize the image to [0, 1]
    normalized_image = image / 255.0

    # Apply the power-law gray-level mapping
    mapped_image = c * np.power(normalized_image, gamma)

    # Scale the image back to [0, 255] and convert to uint8
    mapped_image = np.clip(mapped_image * 255, 0, 255).astype(np.uint8)

    return mapped_image


# ex a=1.5, b=-50
def linear_gray_level_mapping(image, a, b):
    # Read the image using imageio
    image = rgb_to_grayscale(image)

    # Apply the linear gray-level mapping
    mapped_image = np.clip(a * image + b, 0, 255).astype(np.uint8)

    return mapped_image



def rotate_image2(image, angle_degrees):

    input_height, input_width, channels = image.shape
    angle_radians = np.radians(angle_degrees)

    # Calculate the dimensions of the rotated image
    output_width = int(input_width * abs(np.cos(angle_radians)) + input_height * abs(np.sin(angle_radians)))
    output_height = int(input_width * abs(np.sin(angle_radians)) + input_height * abs(np.cos(angle_radians)))

    output_image = np.zeros((output_height, output_width, channels), dtype=np.uint8)

    # Calculate the center of the input and output images
    center_input_x, center_input_y = input_width / 2.0, input_height / 2.0
    center_output_x, center_output_y = output_width / 2.0, output_height / 2.0

    for output_y in range(output_height):
        for output_x in range(output_width):
            # Translate the output image coordinates to the input image coordinates
            input_x = (output_x - center_output_x) * np.cos(angle_radians) + (output_y - center_output_y) * np.sin(angle_radians) + center_input_x
            input_y = -(output_x - center_output_x) * np.sin(angle_radians) + (output_y - center_output_y) * np.cos(angle_radians) + center_input_y

            # Check if the input coordinates are within the bounds of the input image
            if 0 <= input_x < input_width - 1 and 0 <= input_y < input_height - 1:
                output_image[output_y, output_x] = bilinear_interpolation(input_x, input_y, image)

    return output_image



def scale_image(image, output_width, output_height):

    input_height, input_width, channels = image.shape
    output_image = np.zeros((output_height, output_width, channels), dtype=np.uint8)

    x_ratio = float(input_width - 1) / (output_width - 1) if output_width > 1 else 0
    y_ratio = float(input_height - 1) / (output_height - 1) if output_height > 1 else 0

    for output_y in range(output_height):
        for output_x in range(output_width):
            input_x = x_ratio * output_x
            input_y = y_ratio * output_y
            output_image[output_y, output_x] = bilinear_interpolation(input_x, input_y, image)

    return output_image



def flip_image(image, flip_dir):
    
    if flip_dir == 'horizontal':
        flipped_image = np.fliplr(image)
    elif flip_dir == 'vertical':
        flipped_image = np.flipud(image)

    return flipped_image



def rotate_image(image, angle):
    # Convert angle to radians
    angle_rad = np.radians(angle)

    # Compute sine and cosine of angle
    sin_a = np.sin(angle_rad)
    cos_a = np.cos(angle_rad)

    # Compute center point of image
    center_x = image.shape[1] / 2
    center_y = image.shape[0] / 2

    # Define output image
    output_image = np.zeros_like(image)

    # Apply rotation to each pixel in image
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            # Compute new pixel location after rotation
            new_x = int((x - center_x) * cos_a - (y - center_y) * sin_a + center_x)
            new_y = int((x - center_x) * sin_a + (y - center_y) * cos_a + center_y)

            # Copy pixel value to new location in output image
            if 0 <= new_x < image.shape[1] and 0 <= new_y < image.shape[0]:
                output_image[new_y, new_x, 0] = image[y, x, 0]  # red channel
                output_image[new_y, new_x, 1] = image[y, x, 1]  # green channel
                output_image[new_y, new_x, 2] = image[y, x, 2]  # blue channel

    return output_image


def bilinear_interpolation(x, y, img):
    x1, y1 = int(x), int(y)
    x2, y2 = min(x1 + 1, img.shape[1] - 1), min(y1 + 1, img.shape[0] - 1)

    r1 = (x2 - x) * img[y1, x1] + (x - x1) * img[y1, x2]
    r2 = (x2 - x) * img[y2, x1] + (x - x1) * img[y2, x2]

    return (y2 - y) * r1 + (y - y1) * r2



def rgb_to_grayscale(image):
    if len(image.shape) != 3:
        raise ValueError("Input image should be in RGB format.")

    grayscale_image = (0.2989 * image[:, :, 0] + 0.5870 * image[:, :, 1] + 0.1140 * image[:, :, 2]).astype(np.uint8)
    return grayscale_image


def string_to_2d_array(s):
    # Remove square brackets
    s = s.strip("[]")
    
    # Split the string into rows
    rows = s.split(";")
    
    # Split each row into elements and convert to desired data type (e.g., float)
    data = [list(map(float, row.split(","))) for row in rows]
    
    # Convert the list of lists into a NumPy array
    array = np.array(data)
    
    return array


def string_to_tuple(s):
    # Remove parentheses
    s = s.strip("()")
    
    # Split the string into elements and convert to the desired data type (e.g., int)
    elements = list(map(int, s.split(",")))
    
    # Create a tuple from the elements
    result = tuple(elements)
    
    return result




