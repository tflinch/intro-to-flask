# app.py

from flask import Flask, jsonify, abort, request

personnel = {
    "rachel": "Executive Vice President of Managerial Functions",
    "wallace": "Senior Vice President of Managerial Functions",
    "rosie": "Staff Vice President of Managerial Functions",
    "james": "Vice Vice President of Managerial Functions",
    "henri": "Junior Vice President of Managerial Functions"
}

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/information')
def info():
    return 'Flask is the micro-framework of choice for building Machine Learning API endpoints'

@app.route('/profile/<name>')
def profile(name):
    return f"this profile information for {name.upper()}"

@app.route('/personnel/<name>')
def employee(name):
    if name in personnel:
        return jsonify({name: personnel[name]})
    else:
        # abort(404)
        return jsonify({'error':"Employee not found"}), 404
    
@app.route('/employee-search')
def employee_search():
    name = request.args.get('name')
    age = request.args.get('age')
    return f"I searched for employees named {name} who are {age} years"

if __name__ == '__main__':
    app.run()