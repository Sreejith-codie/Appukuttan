from database import cursor, conn

def add_task(user_id, task):
    cursor.execute("INSERT INTO tasks (user_id, task) VALUES (?, ?)", (user_id, task))
    conn.commit()

def get_tasks(user_id):
    cursor.execute("SELECT id, task FROM tasks WHERE user_id=?", (user_id,))
    return cursor.fetchall()

def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()