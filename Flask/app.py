from datetime import date, timedelta
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/today/') 
def today():
    return f'오늘은 {date.today()}입니다.'

def add7days():
    return f'일주일 뒤는 {date.today() + timedelta(days=7)}입니다.'

app.add_url_rule('/7dayslater/', 
        '', 
        add7days)

if __name__ == '__main__':
    app.run()