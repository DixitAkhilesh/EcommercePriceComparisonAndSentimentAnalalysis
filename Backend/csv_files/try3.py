from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_string', methods=['POST'])
def process_string():
    string = request.json.get('string')
    print(string)
    # Do some processing on the input string
    processed_string = string.upper()

    # Return the processed string as a JSON response
    return jsonify({'result': processed_string})

if __name__ == '__main__':
    app.run()
