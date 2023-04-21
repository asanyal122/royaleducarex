from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('applink.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/policy')
def policy():
    return render_template('policy.html')

@app.route('/refund')
def refund():
    return render_template('refund.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/shipping')
def shipping():
    return render_template('shipping.html')