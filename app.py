
# A very simple Flask Hello World app for you to get started with...

from flask import Flask,render_template, request
#import mysql.connector
# import reconocimiento as rc

app = Flask(__name__)


# try:
#     conn = mysql.connector.connect(
#     host="hendrickc.mysql.pythonanywhere-services.com",
#     user="hendrickc",
#     password="MusicaDatabas3",
#     database="hendrickc$music_db"
#     )
#     message = 'Conexión establecida'
#     mycursor = conn.cursor()

# except mysql.connector.Error as e:
#     myresult = ["#"]
#     message = 'No se logró establecer la conexión'

# def add_student(est_nombre, est_usuario, est_contra):
#     query = "INSERT INTO music_estudiante (est_nombre, est_usuario, est_contra) VALUES (%s, %s, %s);"
#     values = (est_nombre, est_usuario, est_contra)
#     mycursor.execute(query, values)
#     conn.commit()

# def authenticate_user(username, password):
#     query = "SELECT * FROM music_estudiante WHERE est_usuario = %s AND est_contra = %s"
#     values = (username, password)
#     mycursor.execute(query, values)
#     user = mycursor.fetchone()
#     return user is not None

@app.route('/')
def index():
    if request.method == 'POST':
        est_nombre = request.form['est_nombre']
        est_usuario = request.form['est_usuario']
        est_contra = request.form['est_contra']
    #     add_student(est_nombre, est_usuario, est_contra)
    # mycursor.execute("SELECT * FROM music_estudiante")
    # myresult = mycursor.fetchall()
    return render_template('intro.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if authenticate_user(username, password):
#             # Authentication successful, redirect to some other page
#             return render_template('intro.html')
#         else:
#             # Authentication failed, show error message or redirect back to login page
#             return render_template('login.html', message='Invalid username or password')
#     else:
#         return render_template('login.html')

@app.route('/intro')
def intro():
    # rc.main()
    return render_template('intro.html')

@app.route('/detalle')
def detalle():
    return render_template('coursedetails.html')

@app.route('/courses')
def menu():
    # try:
    #     conn = mysql.connector.connect(
    #         host="hendrickc.mysql.pythonanywhere-services.com",
    #         user="hendrickc",
    #         password="MusicaDatabas3",
    #         database="hendrickc$music_db"
    #     )
    #     mycursor = conn.cursor(dictionary=True)
    #     mycursor.execute("SELECT leccion_nombre FROM music_leccion INNER JOIN music_curso ON music_leccion.leccion_id = music_curso.leccion_id")
    #     lecciones = mycursor.fetchall()
    #     conn.close()
    # except mysql.connector.Error as e:
    #     lecciones = []


    return render_template('courses.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/adminDashboard')
def adminDash():
    return render_template('adminDashboard.html')

@app.route('/adminCourses')
def adminCour():
    return render_template('coursesAdmin.html')