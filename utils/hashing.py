import hashlib
import bcrypt
import os

def hash_password(password, algorithm):
    """
    Hash a password using the specified algorithm without salt.
    Supported algorithms: sha256, md5, bcrypt
    """
    if algorithm == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()
    elif algorithm == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == 'bcrypt':
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode('utf-8')
    else:
        raise ValueError(f"Unsupported hashing algorithm: {algorithm}")

def hash_password_with_salt(password, algorithm, salt=None):
    """
    Hash a password with a salt using the specified algorithm.
    Supported algorithms: sha256, md5, bcrypt
    A new salt will be generated if none is provided.
    """
    if salt is None:
        salt = os.urandom(16)

    if algorithm == 'sha256':
        hash_value = hashlib.sha256(salt + password.encode()).hexdigest()
    elif algorithm == 'md5':
        hash_value = hashlib.md5(salt + password.encode()).hexdigest()
    elif algorithm == 'bcrypt':
        hash_value = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode('utf-8')
        salt = None
    else:
        raise ValueError(f"Unsupported hashing algorithm: {algorithm}")

    return hash_value, salt 
