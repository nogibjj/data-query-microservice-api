from flask import Flask, jsonify, request

# creating a Flask app
app = Flask(__name__)

@app.route("/")
def home():

    # country = request.args.get('country')
    data = "hello world"
    return jsonify({"data": data})

if __name__ == "__main__":
    app.run(debug=True)