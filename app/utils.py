from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(input_pass: str):
    return password_context.hash(input_pass)

def verify_password(input_pass: str, hashed_pass: str):
    return password_context.verify(input_pass, hashed_pass)
