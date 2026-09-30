from flask import Flask,jsonify,request,render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/tasks", methods=["GET", "POST"])
def tasks():

    if request.method == "POST":
        data = request.get_json()

        title = data["title"]
        status = data["status"]

        connection = sqlite3.connect("tasks.db")
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO tasks (title, status) VALUES (?, ?)",
            (title, status)
        )

        connection.commit()

        return jsonify({"message": "Task Created"})

    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    task_list = []

    for task in tasks:
        task_list.append({
            "id": task[0],
            "title": task[1],
            "status": task[2]
        })

    return jsonify(task_list)

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()

    new_status = data["status"]
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()

    cursor.execute(
        "update tasks set status = ? where id = ?",
        (new_status, task_id)
    )
    connection.commit()
    return jsonify({"message": "Task Updated"})

@app.route("/tasks/<int:task_id>", methods =["DELETE"])
def delete_task(task_id):

    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()

    cursor.execute(
        "delete from tasks where id = ?",
        (task_id,)
    )    
    connection.commit()
    return jsonify({"message":"Task Deleted"})
    
# @app.route("/hello")
# def hello():
#     return "Hello Balaji"
