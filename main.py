from dotenv import load_dotenv
from lib.cryptography import Cryptography
from flask import Flask, request
from flask_cors import CORS
from waitress import serve
from lib.database import Database

load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(force=True)
    user = data["user"]
    encode_password = Cryptography.encode(data["password"])
    is_valid_user = Database(data["database"]).verify_user(
        user, encode_password)
    return {"status": 200, "content": is_valid_user}


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json(force=True)
    user = data["user"]
    encode_password = Cryptography.encode(data["password"])

    database = Database(data["database"])
    result = database.register_user(user, encode_password)
    is_registered = len(result) > 0
    if result == database.ALREADY_EXIST:
        return {"status": 200, "content": database.ALREADY_EXIST}
    elif is_registered:
        return {"status": 201, "content": database.REGISTERED}
    else:
        return {"status": 500, "content": "Internal Server Error"}


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5001)
