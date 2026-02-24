import os
import flask
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    return render_template('submit.html', data=request.form)

if __name__ == '__main__':
    app.run(debug=True)