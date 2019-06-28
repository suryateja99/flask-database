from flask import Flask, render_template
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']


mysql = MySQL(app)

@app.route("/", methods=['GET','POST'])
def hello():

    if request.method =='POST':
        cur = mysql.connection.cursor()
        result = cur.execute("SELECt * FROM data") 
        if result > 0:
            data = cur.fetchall()
    return render_template('home.html', data1= data)




if __name__ == "__main__":
    app.run(debug=1)