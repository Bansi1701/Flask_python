""" 
path of routing:

RegisterForm.html-------------if username and password correct-----> welcome.html
                        |
                        ------wrong------> RegisterForm.html with error message.
"""  

from flask import *

app = Flask(__name__)


@app.route('/')
def load():
    return render_template('RegisterForm.html')

@app.route('/info', methods=['POST'])
def data():
    fn = request.form[ 'fn' ]
    ln = request.form[ 'ln' ]
    un = request.form[ 'un' ]
    pwd = request.form[ 'pwd' ]

    if un == 'admin' and pwd == 'admin':            # username and password are static.
        return render_template('welcome.html', fn=fn, ln=ln)   # pass fn and ln in welcome.html page
    else:
        str = 'your username or password is wrong.....'
        return render_template('RegisterForm.html', str =str) # pass str in RegisterForm.html


app.run(debug=1)
