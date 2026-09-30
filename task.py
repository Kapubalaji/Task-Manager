import sqlite3
connection = sqlite3.connect("tasks.db")
cursor = connection.cursor()
#cursor.execute0("some SQL here")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id integer primary key,
    title TEXT,
    status TEXT
)
""")

# title = "Learn javascript"
# status = "pending"
# 
# cursor.execute(
# "Insert INTO tasks(title,status) values(?,?)",
#                 (title, status) 
#                 )
# connection.commit()                
cursor.execute("select * from tasks")

cursor.execute("select*from tasks")
tasks = cursor.fetchall()


task_id = 2 
new_status = "completed"

cursor.execute(
    "update tasks set status = ? where id = ?",
    (new_status, task_id)
)

connection.commit()

cursor.execute(
    "select * from tasks"
)

tasks = cursor.fetchall()

for task in tasks:
    print(task[0], task[1], task[2])

task_id = 8
cursor.execute(
"delete from tasks where id = ?",
 (task_id,)
 )
connection.commit()
