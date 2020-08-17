
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

    if un == 'admin' and pwd == 'admin':
        return render_template('welcome.html', fn=fn, ln=ln)
    else:
        str = 'your username or password is wrong.....'
        return render_template('RegisterForm.html', str =str, un=un, pwd=pwd, )


app.run(debug=1)
