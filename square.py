from flask import Flask
import pygame 
from pygame.locals import *
from sys import exit
from random import *
import multiprocessing
import time
import source
import os

app = Flask(__name__)
IMG_FOLDER = os.path.join('static')

app.config['UPLOAD_FOLDER'] = IMG_FOLDER
@app.route('/')
def run_script():
    #file = open(r'C:\Users\KASHIF\Desktop\website\squares\source.py', 'r').read()
    #exec(file,globals())
    source.main()
    return "done"

def Display_IMG():
    Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'squares.png')
    return render_template("index.html", user_image=Flask_Logo)

if __name__ == "__main__":
    app.run(debug=True)
