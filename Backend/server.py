from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from amazon import amazon_function
from flipkart import flipkart_function
import json
# from try2 import main

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])
inputString = ""

@app.route('/receive-string', methods=['POST'])
def generate_lists():
    input_string = request.json['inputString']
    print(f'String received from frontend: {input_string}')
    amazon_function(input_string)
    flipkart_function(input_string)
    response = make_response(input_string)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

# @app.route('/amazon_list', methods=['GET'])
# def get_amazon_data():
#     with open('')
    
# @app.route('/flipkart_list', methods=['GET'])
# def get_flipkart_data():

@app.route('/')
def home():
    return "Welcome To Flask!"

if __name__ == '__main__':
    app.run(debug=True)

