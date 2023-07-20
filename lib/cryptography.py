import jwt
import os


class Cryptography():
    def encode(password):
        return jwt.encode({"password": password}, os.getenv("SECRET"), os.getenv("ALGORITHM"))

    def decode(password):
        return jwt.decode(password, os.getenv("SECRET"), algorithms=os.getenv("ALGORITHM"))
