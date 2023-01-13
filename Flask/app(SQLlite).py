import sqlite3 as sql
from flask import Flask, render_template, request

conn = sql.connect('database.db')
print('Opened database successfully')

conn.execute(
    'CREATE TABLE IF NOT EXISTS students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print('Table created successfully')
conn.close()

''''''

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home(SQLlite).html')

@app.route('/list/')
def list():
    con = sql.connect('database.db')
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute('select * from students')
    
    rows = cur.fetchall()
    return render_template('list.html', rows = rows)

@app.route('/enternew')
def new_student():
    return render_template('student(SQLlite).html')

@app.route('/addrec', methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            name = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']
            
            conn = sql.connect('database.db')
            cur = conn.cursor()
            cur.execute('''INSERT INTO students(name, addr, city, pin) VALUES(?, ?, ?, ?)''', (name, addr, city, pin))
            
            conn.commit()
            msg = 'Record successfully added'
        except:
            conn.rollback()
            msg = 'error in insert operation'
        finally:
            return render_template('result(SQLlite).html', msg = msg)
            con.close()
            
if __name__ == '__main__':
    app.run(debug=True)