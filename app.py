from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello World!'


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '_a_main__':
    app.run()