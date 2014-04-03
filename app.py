from flask import Flask, render_template, request
import re
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    #meal_cost = request.form.submit
    print request.form
    keywords = request.form['keywords']
    text_to_parse = request.form['text_to_parse']
    


    result_dict = dict(
        meal_cost = meal_cost,
        tip_percentage = tip_percentage,
        tip_amount = tip_amount        
        )
    return render_template('results.html', data=result_dict)

if __name__ == '__main__':
    app.run(debug=True)
