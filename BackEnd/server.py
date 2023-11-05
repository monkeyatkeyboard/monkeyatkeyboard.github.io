from flask import Flask, render_template, request, jsonify
from test_main import *
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def show_about():
    return render_template('about.html')

@app.route('/output')
def get_output():
    text = request.args.get('text-input')
    text = Get_Text_Summary(text)
    return render_template(
        "output.html",
        output=text
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
    # serve(app, host="0.0.0.0", port=8000)