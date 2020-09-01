from flask import *
import pymysql

app = Flask(__name__)
app.secret_key = 'jkzdnfknj'
def database_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='pythondb',
        cursorclass = pymysql.cursors.DictCursor
    )
    return connection

@app.route('/')
def home():
    return render_template('Login.html')

@app.route('/Registration')
def registration():
    return render_template('registration_form.html')

@app.route ( '/any' )
def home2():
    return render_template('Login.html')

@app.route('/registration_details',methods=['post'])
def registration_details():
    fn = request.form['fn']
    ln = request.form['ln']
    un = request.form['un']
    pwd = request.form['pwd']

    connection = database_connection()
    pointer = connection.cursor()

    pointer.execute("insert into registration_data(firstname,lastname,username,password) values ('" +fn+ "','" +ln+ "','" +un+ "','" +pwd+ "')")

    connection.commit()
    pointer.close()
    connection.close()

    return redirect(url_for('home'))

@app.route('/login',methods=['post'])
def login():
    un = request.form['un']
    pwd = request.form['pwd']

    connection = database_connection()
    pointer = connection.cursor()

    pointer.execute("select * from registration_data")
    data = pointer.fetchall()
    print(data)
    for dict in data:
        if un==dict['username'] and pwd==dict['password']:
            return render_template('Welcome.html',fn=dict['firstname'],ln=dict['lastname'])

        elif un!=dict['username']:
            continue
        elif un== dict['username'] and pwd!=dict['password']:
            flash('')
            flash('incorrect password...')
            return redirect(url_for('home2'))
    else:
        flash('incorrect username...')
        flash('')
        return redirect(url_for('home2'))


if __name__=="__main__":
    app.run(debug=True,Threaded=True)