from __future__ import division, print_function
import sys
import os
import glob
import re
from model import Recommendation

recommend = Recommendation()

# Flask utils
from flask import Flask, redirect, url_for, request, render_template


# Define a flask app
app = Flask(__name__)


# Main page
@app.route('/', methods=['GET'])
def index():
    results_page = False
    return render_template('index.html')


# Prediction page
@app.route('/search', methods=['POST'])
def search():
    '''
    For rendering results on HTML GUI
    '''
    results_page = True
    user_name = str(request.form.get('reviews_username'))
    prediction = recommend.top_5_recommendation(user_name)

    return render_template('index.html', username=user_name, results=prediction, results_page= results_page)         
        

if __name__ == '__main__':
    app.run(debug=True)
