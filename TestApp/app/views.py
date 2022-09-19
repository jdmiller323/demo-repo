"""Missing function docstring (missing-docstring)"""
from app import app

@app.route('/')
def home():
    """Missing function docstring (missing-docstring)"""
    return "hello world!"
