from flask import Flask
from flask import render_template 
from flask import request

app = Flask(__name__)



@app.route('/')
def form():
    return render_template('form.html')



@app.route('/submit', methods=['POST'])
def form_submit():
   
    submitted_username = request.form['username']
    return render_template('submit.html', username=submitted_username)



if __name__ == '__main__':
    app.run()
