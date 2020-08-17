""" first we install flask
	open cmd
	type : pip install flask
"""

# First we imported the Flask class from flask library
from flask import Flask    

# Next we create an instance of this class
app = Flask(__name__)     
""" The argument is the name of the application’s module or package 
If you are using a single module (as in this example), you should use __name__
for more information : https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-applicatio """

# We then use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
def hello_world():
    return 'Hello, World!'

app.run(debug=True)
# our program is Running on http://127.0.0.1:5000/