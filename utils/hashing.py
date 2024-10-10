# utils/hashing.py
import hashlib
import bcrypt

def hash_password(password, algorithm='sha256'):
    if algorithm == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()
    elif algorithm == 'bcrypt':
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt)
