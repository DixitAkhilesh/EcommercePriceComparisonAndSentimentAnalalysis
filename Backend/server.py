from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from amazonElectronics import amazon_function
from flipkartElectronics import flipkart_function
from amazonFashion import amazon_fashion_function
from flipkartFashion import flipkart_fashion_function
from amazon_details import amazon_details_function
from flipkart_details import flipkart_details_function
from amazon_details import get_amazon_details
from FlipkartExtraction import extract_f_data
from AmazonExtraction import extract_a_data
import json
# from try2 import mai

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}})
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

@app.route('/receive-string/fashion', methods=['POST'])
def fashion_list():
    input_string = request.json['inputString']
    print(f'String received from frontend: {input_string}')
    amazon_fashion_function(input_string)
    flipkart_fashion_function(input_string)
    response = make_response(input_string)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/amazon', methods=['POST'])
def set_amazon_url():
    url = request.json['url']
    extract_a_data(url)
    amazon_details_function(url)
    print(url)
    response = make_response(url)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/flipkart', methods=['POST'])
def set_flipkart_url():
    url = request.json['url']
    extract_f_data(url)
    flipkart_details_function(url)
    print(url)
    response = make_response(url)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/details/amazon',methods=['GET'])
def amazon_details():
    filePath = './reviews/amazon_reviews.csv'
    data = get_amazon_details(filePath)
    response = make_response(jsonify(data))
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/details/flipkart',methods=['GET'])
def flipkart_details():
    filePath = './reviews/flipkart_reviews.csv'
    data = get_amazon_details(filePath)
    response = make_response(jsonify(data))
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/')
def home():
    return "Welcome To Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
