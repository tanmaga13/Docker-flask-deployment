from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Fetching data from JSON file"


@app.route('/api')
def api():
    with open('data.json', 'r') as file:
        data = json.load(file)
    
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)