
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')


# POST requests 

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
    print("Post request have been invoked in app.js for flipping an image.")

    data = request.json['type']
    
    # Here flip the image according to the type.

    
    print(data)  
    # Code to run the specific function goes here
    return "Image succesfully flipped"


@app.route('/scaleImage', methods=['POST'])
def scaleImage():
    print("Post request have been invoked in app.js for scaling an image.")
    # Code to run the specific function goes here
    return "Function executed successfully"


@app.route('/rotateImage', methods=['POST'])
def rotateImage():
    print("Post request have been invoked in app.js for rotating an image. ")
    # Code to run the specific function goes here
    return "Function executed successfully"


@app.route('/linearMapImage', methods=['POST'])
def linearMapImage():
    print("Post request have been invoked in app.js for applying linear gray level mapping to image")
    # Code to run the specific function goes here
    return "Function executed successfully"


@app.route('/powerLawMapImage', methods=['POST'])
def powerLawMapImage():
    print("Post request have been invoked in app.js for power law mapping an image. ")
    # Code to run the specific function goes here
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
    print("Post request have been invoked in app.js for applying convolution to an image. ")
    # Code to run the specific function goes here
    return "Function executed successfully"



@app.route('/filterImage', methods=['POST'])
def filterImage():
    print("Post request have been invoked in app.js for applying non-linear filterin to an image. ")
    # Code to run the specific function goes here
    return "Function executed successfully"


if __name__ == "__main__":
    app.run(debug=True)



