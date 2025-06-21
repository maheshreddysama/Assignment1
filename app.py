from flask import Flask
app = Flask(__name__)
@app.route('/')
#mahesh reddy Sama
#100953232
def hello():
    return 'Hello from Dockerized Flask App!'
if __name__ == '__main__':
             app.run(host='0.0.0.0', port=5000)