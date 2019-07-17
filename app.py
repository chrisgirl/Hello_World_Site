from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'
    


number = 0

@app.route('/ping')
def ping():
    global number 
    number += 1
    return 'you are ping' + str(number)

@app.route('/api')
def api():
    return jsonify({"hello": "there"})

@app.route('/foo/<name>')
def foo(name):
    return render_template('index.html', to=name)


if (os.getenv('LIVE', 'false') == 'true'):
    if __name__ == '__main__':
       app.run(debug=False, host='0.0.0.0')
else:
    if __name__== '__main__':
        app.run(debug=True, host='0.0.0.0')

   
