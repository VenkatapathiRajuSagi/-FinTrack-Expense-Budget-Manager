from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = 'data/expenses.json'

def read_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def write_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    expenses = read_data()
    total = sum(item['amount'] for item in expenses)
    return render_template('index.html', expenses=expenses, total=total)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    expenses = read_data()
    expenses.append(data)
    write_data(expenses)
    return jsonify({'status': 'success'})

@app.route('/clear', methods=['POST'])
def clear():
    write_data([])
    return jsonify({'status': 'cleared'})

if __name__ == '__main__':
    app.run(debug=True)
