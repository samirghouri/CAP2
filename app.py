from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return '''
Main <a href="/add/23/19">add</a>
'''

@app.route("/add/<int:a>/<int:b>")
def api_info(a, b):
    return str(a+b)

if __name__ == '__main__': 
  
    app.run(debug=True, host='0.0.0.0') 
    

    
