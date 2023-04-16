
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from mimetypes import guess_extension

from src.toolbox import *
import cv2

import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

UPLOAD_FOLDER = "static/img"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# POST requests 

new_filename = ""

@app.route('/upload', methods=['POST'])
def upload_image():
    global new_filename

    # Check if there's an image in the request
    if 'image' not in request.files:
        return "No image in the request", 400

    image = request.files['image']

    print("Upload request has been made")


    # Check if the image is empty
    if image.filename == '':
        return "No image selected", 400


    file_ext = os.path.splitext(image.filename)[1]
    new_filename = f"image{file_ext}"
   

    # Save the uploaded image
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(new_filename)))

    # Get the RGB checkbox value
    rgb = bool(request.form.get('rgb'))

    # Render the home.html template
    return redirect(url_for('home'))



@app.route('/home')
def home():
    global new_filename
    return render_template('home.html', img_name=new_filename)


@app.route('/displayImageInfo', methods=['POST'])
def displayImageInfo():
    print("Post request have been invoked in app.js for displaying image information. ")

    # Code to run the specific function goes here
    return "Test image data"


@app.route('/cropImage', methods=['POST'])
def cropImage():
    print("Post request have been invoked in app.js for cropping an image. ")
    # Code to run the specific function goes here
    return "Function executed successfully"


@app.route('/flipImage', methods=['POST'])
def flipImage():
    global new_filename

    print("Post request have been invoked in app.js for flipping an image.")
    print("Flipping the image " + new_filename)

    data = request.json['type']
    
    img = cv2.imread("static/img/" + new_filename)
    
    output_image = flip_image(img, data)
    
    cv2.imwrite("static/img/" + new_filename, output_image)

    # Here flip the image according to the type.
    
    print(data)

    # Code to run the specific function goes here
    return "Image succesfully flipped"


@app.route('/scaleImage', methods=['POST'])
def scaleImage():
    global new_filename

    print("Post request have been invoked in app.js for scaling an image.")
    
    height = request.json['height']
    width = request.json['width']
    
    img = cv2.imread("static/img/" + new_filename)

    output_image = scale_image(img, int(width), int(height))
    
    cv2.imwrite("static/img/" + new_filename, output_image)

    # Code to run the specific function goes here
    return "Function executed successfully"


@app.route('/rotateImage', methods=['POST'])
def rotateImage():
    global new_filename

    print("Post request have been invoked in app.js for rotating an image. ")
    # Code to run the specific function goes here

    angle = request.json['angle']
    
    img = cv2.imread("static/img/" + new_filename)
    output_image = rotate_image2(img, int(angle))
    
    cv2.imwrite("static/img/" + new_filename, output_image)



    return "Function executed successfully"


@app.route('/linearMapImage', methods=['POST'])
def linearMapImage():
    global new_filename
    
    print("Post request have been invoked in app.js for applying linear gray level mapping to image")

    a = request.json['a']
    b = request.json['b']
    
    img = cv2.imread("static/img/" + new_filename)

    output_image = linear_gray_level_mapping(img, float(a), int(b))
    
    cv2.imwrite("static/img/" + new_filename, output_image)

    return "Function executed successfully"


@app.route('/powerLawMapImage', methods=['POST'])
def powerLawMapImage():
    
    global new_filename
    
    print("Post request have been invoked in app.js for power law mapping an image. ")
    # Code to run the specific function goes here

    c = request.json['c']
    gamma = request.json['gamma']
    
    img = cv2.imread("static/img/" + new_filename)

    output_image = power_law_grey_level_mapping(img, float(c), float(gamma))
    
    cv2.imwrite("static/img/" + new_filename, output_image)


    return "Function executed successfully"


@app.route('/calculateHistogram', methods=['POST'])
def calculateHistogram():
    print("Post request have been invoked in app.js for calculating the histogram of an image. ")
    # Code to run the specific function goes here
    return "Function executed successfully"


@app.route('/histogramEqualizeImage', methods=['POST'])
def equalizeHistogram():
    print("Post request have been invoked in app.js for histogram equalizing an image. ")
    # Code to run the specific function goes here
    return "Function executed successfully"


@app.route('/convoluteImage', methods=['POST'])
def convoluteImage():
    global new_filename
    
    print("Post request have been invoked in app.js for applying convolution to an image. ")
    
    kernel = request.json['kernel']
    color_type = request.json['color']
    
    img = cv2.imread("static/img/" + new_filename)

    kernel_array = string_to_2d_array(kernel)
    
    if color_type == "true":
        output_image = convolution_coloured(img, kernel_array)
    else:
        output_image = convolution(img, kernel_array)
    
    cv2.imwrite("static/img/" + new_filename, output_image)

    return "Function executed successfully"



@app.route('/filterImage', methods=['POST'])
def filterImage():
    global new_filename
    
    print("Post request have been invoked in app.js for applying non-linear filterin to an image. ")
    # Code to run the specific function goes here

    window = request.json['window']
    filter_type = request.json['type']
    color_type = request.json['color']
    
    img = cv2.imread("static/img/" + new_filename)
    
    window_size = string_to_tuple(window)
    
    if color_type == "true":
        output_image = filtering_rgb(img, window_size, filter_type)
    else:
        output_image = filtering_grayscale(img, window_size, filter_type)

    cv2.imwrite("static/img/" + new_filename, output_image)

    return "Function executed successfully"


if __name__ == "__main__":
    app.run(debug=True)



