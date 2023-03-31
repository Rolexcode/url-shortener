from flask import Flask, render_template, redirect, request
import string
import random

app = Flask(__name__)

url_map = {}

def generate_short_url():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['url']
    short_url = generate_short_url()
    url_map[short_url] = long_url
    return render_template('shorten.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_short_url(short_url):
    long_url = url_map.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return 'Invalid URL'

if __name__ == '__main__':
    app.run(debug=True)
