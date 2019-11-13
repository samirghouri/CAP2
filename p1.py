from flask import Flask, jsonify
myapp = Flask(__name__)

@myapp.route("/")
def main():
    return '''
Main <a href="/add/23/19">add</a>
'''

@myapp.route("/add/<int:a>/<int:b>")
def api_info(a, b):
    return str(a+b)

if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    myapp.run()