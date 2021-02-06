from flask import Flask
from flask import render_template 
from flask import request
# inisialisasi flask, bawaan framework sepertinya, harus seperti ini
app = Flask(__name__)


# Fungsi yang menampilkan form
@app.route('/')
def form():
    return render_template('form.html')


# Fungsi yang menangkap form submit
# karena action di form kita tulis '/submit', disini kita tulis juga '/submit'
# supaya nerima data yang dikirim dari form disini
@app.route('/submit', methods=['POST'])
def form_submit():
    # karena di form input kita namakan 'username', disini kita tulis 'username'
    # untuk dapetin value yang ditulis user
    submitted_username = request.form['username']

    # di submit.html, kita ingin menampilkan data yang di submit
    # karena disana kita tulis {{ username }}, maka kita tulis 'username'
    return render_template('submit.html', username=submitted_username)


# inisialisasi flask, bawaan framework sepertinya, harus seperti ini
if __name__ == '__main__':
    app.run()