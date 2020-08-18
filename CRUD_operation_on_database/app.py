from flask import *
import pymysql

def database_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='pythondb',
        cursorclass = pymysql.cursors.DictCursor
    )
    return connection

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/Registration')
def Registration_home():
    return render_template('register.html')

@app.route('/register_data' , methods=[ 'POST' ] )
def data_insert( ):
    fn = request.form[ 'fn' ]
    ln = request.form[ 'ln' ]
    un = request.form[ 'un' ]
    pwd = request.form[ 'pwd' ]
    gender = request.form[ 'gender' ]
    city = request.form[ 'city' ]
    add = request.form[ 'address' ]
    hobby = request.form.getlist ( 'hobby' )
    h = "-".join ( hobby )

    connection=database_connection()
    pointer = connection.cursor()

    pointer.execute("INSERT INTO login_data(firstname,lastname,username,password,gender,city,address,hobby) VALUES ('" + fn + "','" + ln + "','" + un + "','" + pwd + "','" + gender + "','" + city + "','" + add + "','" + h + "')" )
    # login_data = table name
    # firstname,lastname,username,password,gender,city,address,hobby = columns name
    connection.commit ( )
    pointer.close ( )
    connection.close ( )

    return redirect(url_for('home')) # home is function

@app.route('/Data')
def data_retrive():
    connection=database_connection()
    pointer =connection.cursor()

    pointer.execute("select * from login_data")
    data=pointer.fetchall()

    connection.commit()
    pointer.close()
    connection.close()
    return render_template('Data.html',data=data)

@app.route ( '/delete_data' , methods=[ 'GET' ] )
def delete():
    id_value = request.args.get('id')
    connection = database_connection()
    point = connection.cursor()

    point.execute("delete from login_data where id=" + id_value)

    connection.commit ( )
    point.close ( )
    connection.close ( )
    return redirect (url_for( 'data_retrive'))

@app.route('/edit_data' , methods=['get'])
def edit_data():
    id_value = request.args.get('id')
    connection = database_connection()
    point = connection.cursor()

    point.execute("select * from login_data where id="+id_value)
    data = point.fetchall()
    print(data[0])
    connection.commit()
    point.close()
    connection.close()
    return render_template('edit_registration.html',data=data[0])

@app.route('/update_registration', methods=['post'])
def update():
    id = request.form['id']
    fn = request.form['fn']
    ln = request.form['ln']
    un = request.form['un']
    pwd = request.form['pwd']
    gender = request.form['gender']
    add = request.form['address']
    city = request.form['city']
    hobby = request.form.getlist('hobby')
    h = "-".join(hobby)

    connection = database_connection()
    pointer = connection.cursor()

    pointer.execute(
        "UPDATE login_data set firstname='" + fn + "' ,lastname='" + ln + "',username='" + un + "',password='" + pwd + "',gender='" + gender + "', city='" + city + "',address='" + add + "',hobby='" + h + "' WHERE id='" + id + "'")
    connection.commit()
    pointer.close()
    connection.close()

    return redirect(url_for('data_retrive'))

if __name__=="__main__":
    app.run(debug=True,threaded=True)