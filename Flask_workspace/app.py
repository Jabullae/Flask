from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def showImg():
    return render_template('showImg.html', image_file = 'img/knn.png')

if __name__ == '__main__':
    app.run(debug=True)