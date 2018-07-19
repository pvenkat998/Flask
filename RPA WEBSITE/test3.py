from flask_mysqldb import MySQL
from flask import Flask,render_template

app=Flask(__name__)
app.config['MYSQL_HOST=eigyou_kikaku;host=192.168.5.124;charset=utf8']
app.config['MYSQL_USER=eigyou_kikaku']
app.config['MYSQL_PASSWORD=As6hV2K!k']
app.config['MYSQL_DB=eigyou_kikaku']
mysql = MySQL(app)

@app.route("/profile/<name>")
def profile(name):
    return render_template("db.html", name=name)

if __name__ == "__main__":
        app.run(debug=True)
