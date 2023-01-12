from flask import Flask, make_response, render_template
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('student.html')

@app.route('/cookie')
def cookie():
    res = make_response('<h1>cookie is set</h1>')
    res.set_cookie('foo', 'bar')
    return res

if __name__ == '__main__':
    app.run(debug=True)