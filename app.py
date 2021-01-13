from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/<int:num1>/<int:num2>')
def sum(num1,num2):
    return jsonify({"sum": num1 + num2})

if __name__ == "__main__":
    app.run()