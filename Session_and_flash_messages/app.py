"""
path of routing:

Register.html-----(fn2)-----> Login.html-----(fn3)-----if username and password are correct-----> Welcome.html
                                                        |
                                                        ------------------wrong-----------(fn4)-----> Login.html with error
"""


from flask import *

app = Flask ( __name__ )
app.secret_key = 'any'


@app.route ( '/' )
def fn1():
    return render_template ( 'Register.html' )

@app.route ( '/any' )
def fn4():
    return render_template('Login.html')

@app.route ( '/setsession' )
def fn2():
    first_name = request.args.get ( 'fn' )
    last_name = request.args.get ( 'ln' )
    user = request.args.get ( 'un' )
    password = request.args.get ( 'pwd' )

    session['fn'] = first_name
    session['ln'] = last_name
    session['user'] = user
    session['pass'] = password
    return render_template ('Login.html')


@app.route ( '/LoginData' , methods=['POST'])
def fn3():
    id = request.form['un2']
    pwd = request.form['pwd2']

    if id == session['user'] and pwd == session['pass']:
        return render_template ( 'Welcome.html' )
    else:
        flash('incorrect username or password...')
        return redirect(url_for('fn4'))

if __name__ == '__main__':
    app.run ( debug=True,threaded=True)
