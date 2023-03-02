from flask import Flask
from dotenv import load_dotenv
import time
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World!'

if __name__ == '__main__':
  app.run()

def decorator_function(function):
  def wrapper_function():
    function()
  return wrapper_function

def delay(function):
  def wrapper():
    time.sleep(2)
    function()
  return wrapper

@delay
def say_hello():
  print('Hello')

@delay
def say_bye():
  print('Bye')


