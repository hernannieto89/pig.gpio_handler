from flask import Flask, jsonify

from handler import switch_pin
from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('pin', type=int, help='Target GPIO pin', required=True)


app = Flask(__name__)


@app.route("/switch", methods=['POST'])
def index():
    args = parser.parse_args()
    pin = args['pin']
    error = switch_pin(pin)
    if error:
        return jsonify({"message": f"Error: {error}"}, 500)
    return jsonify({"message": "Success"}, 200)


if __name__ == "__main__":
    app.run()
