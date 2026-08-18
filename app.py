import os
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello, Secure CI/CD Pipeline!"

if __name__ == '__main__':
    # Binds to localhost/env variable rather than 0.0.0.0 directly
    host = os.getenv('HOST', '127.0.0.1')
    port = int(os.getenv('PORT', 5000))
    app.run(host=host, port=port)
