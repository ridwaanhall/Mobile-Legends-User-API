from authlib.jose import jwt
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("TOKEN")

# Decode the token
decoded_token = jwt.decode(token, options={"verify_signature": False})

# Access the payload
print(decoded_token)
