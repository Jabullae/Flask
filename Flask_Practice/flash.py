from flask import Flask, flash, redirect, render_template, request, url_for
app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/')
def index():
    return render_template('index(flash).html')

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    error = None
    
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
            request.form['password'] != 'admin':
                error = 'Invalid username or passward. Please try again!'
        else:
            flash('성공적으로 로그인되었습니다!')
            return redirect(url_for('index'))
        
    return render_template('login(flash).html', error = error)

if __name__ == '__main__':
    app.run(debug=True)