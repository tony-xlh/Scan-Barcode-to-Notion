from flask import Flask, request, send_file, render_template
from PIL import Image
import base64
from io import BytesIO
import base64
import os
import time
import json
import requests
app = Flask(__name__, template_folder='.', static_url_path='/', static_folder='./')

@app.route('/')
def main():
    return render_template(
        'index.html'
    )
    
@app.route('/notion', methods=['POST'])
def send_to_notion():
    if request.method == 'POST':
        data = request.get_json()
        if 'base64' in data:
            print(data)
    else:
        return "Method not allowed", 400
        
@app.route('/book', methods=['GET'])
def get_book_info():
    ISBN = request.args.get('isbn', '')
    if ISBN != '':
        URL = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'+ISBN
        r = requests.get(URL)
        return r.text
    else:
        return "No ISBN specified", 400

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 8888, ssl_context='adhoc')
   