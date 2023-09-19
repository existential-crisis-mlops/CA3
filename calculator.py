from flask import Flask, render_template, request, jsonify
#from calculator import Calculator  # Assuming your calculator logic is in a separate file

app = Flask(__name__)

# Initialize your calculator
#calculator = Calculator()

@app.route('/')
def index():
    return "Welcome to the Calculator App"

def sub(x,y):
    return x-y

# Define routes for your calculator functions
@app.route('/calc/sub/<int:num1>/<int:num2>', methods=['GET'])
def sub1(num1, num2):
    result = sub(num1, num2)
    return jsonify({"result": result})

if __name__ == '__main__':

    app.run(debug=True)