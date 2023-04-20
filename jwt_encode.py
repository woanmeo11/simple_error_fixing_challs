import jwt

data = {"inteface": "meo", "core": "dog"}
token = jwt.encode(data, "super_secret_key", algorithm="HS256")
print("Token:", token)

token_data = jwt.decode(
    token, options={"verify_signature": False}, algorithms=["HS256"]
)
print("Token data:", token_data)
