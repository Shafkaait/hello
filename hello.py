from flask import Flask

myapp = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

app.run(debug = True)
