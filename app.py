
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello World!'


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/about-css')
def about_css():
    return render_template('about-css.html')


@app.route('/favorite-course')
def favorite_course():
    return render_template('favorite-course.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')


if __name__ == '__main__':
    app.run()
