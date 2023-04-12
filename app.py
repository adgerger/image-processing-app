
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')



@app.route('/displayImageInfo', methods=['POST'])
def run_function():
    print("Post request have been invoked in app.js for displaying image information. ")
    # Code to run the specific function goes here
    return "Function executed successfully"


if __name__ == "__main__":
    app.run()



