from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/home')
def home():
    return 'This is the home page'

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.debug = True  # setting the debugging option for the application instance
    app.run(host='0.0.0.0', port=5001)
