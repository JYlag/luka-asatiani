from flask import request, redirect, render_template, session, flash
from app import app, db

import datetime

app.secret_key = "a1hf892fHre2dsa92J"

@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()
