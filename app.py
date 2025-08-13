from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",         # your MySQL username
    password="Rowdy@26", # your MySQL password
    database="student_management" # your database name
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student')
def student_page():
    return render_template('student.html')

@app.route('/course')
def course_page():
    return render_template('course.html')

@app.route('/enrollment')
def enrollment_page():
    return render_template('enrollment.html')

@app.route('/student', methods=['POST'])
def add_student():
    fname = request.form['fname']
    lname = request.form['lname']
    dob = request.form['dob']
    gender = request.form['gender']
    email = request.form['email']
    phone_no = request.form['phone']
    address = request.form['address']
    join_date = request.form['join_date']
    course_id = request.form['course_id']
    status = request.form['status']

    query = """INSERT INTO students (first_name, last_name, DOB , gender, email, phone_no , address, enrollment_date, course_id, student_status)
               VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute(query, (fname, lname, dob, gender, email, phone_no, address, join_date, course_id, status))
    db.commit()
    return redirect('/student')

@app.route('/course', methods=['POST'])
def add_course():
    name = request.form['course_name']
    desc = request.form['description']
    duration = request.form['duration']
    fee = request.form['fee']

    query = """INSERT INTO courses (course_name, course_description, course_duration, course_fee)
               VALUES (%s,%s,%s,%s)"""
    cursor.execute(query, (name, desc, duration, fee))
    db.commit()
    return redirect('/course')

@app.route('/enrollment', methods=['POST'])
def add_enrollment():
    student_id = request.form['student_id']
    course_id = request.form['course_id']
    enroll_date = request.form['enroll_date']
    semester = request.form['semester']
    status = request.form['status']

    query = """INSERT INTO enrollments (student_id, course_id, enrollment_date, semester, student_status)
               VALUES (%s,%s,%s,%s,%s)"""
    cursor.execute(query, (student_id, course_id, enroll_date, semester, status))
    db.commit()
    return redirect('/enrollment')

if __name__ == '__main__':
    app.run(debug=True)
