from flask import Flask,request,render_template,redirect,url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Nil_ganu123@'
app.config['MYSQL_DB'] = 'student_lect'

mysql = MySQL(app)

@app.route('/add', methods = ['POST','GET'])
def add_student():
    if request.method == 'POST':
        student_detail = request.form
        name = student_detail['name']
        age = student_detail['age']
        grade = student_detail['grade']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO student(name,age,grade) values(%s,%s,%s)",(name,age,grade))
        cur.connection.commit()
        cur.close()
        return redirect('/')
    
    return render_template('add_student.html')
        
@app.route('/')
def home():
    cur = mysql.connection.cursor()
    result_value = cur.execute("select * from student")
    
    if result_value > 0:
        student_detail = cur.fetchall()
        print(student_detail)
        return render_template('home.html',students=student_detail)
    return render_template('home.html', students=None)


if __name__ == '__main__':
    app.run(debug=True)