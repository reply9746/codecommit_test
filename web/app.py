"""
You're a clever      Betech.
"""

from flask import Flask, request, abort
app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello_world():
<<<<<<< HEAD
    abort(404)
=======
    return 'This is version 1.'
>>>>>>> origin

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
