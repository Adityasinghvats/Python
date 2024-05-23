import sqlite3

conn = sqlite3.connect('task_todo.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL,
               priority TEXT NOT NULL
    )
''')

def list_task():
    cursor.execute("SELECT * FROM tasks")
    for row in cursor.fetchall():
        print(row)

def add_task(name, time, priority):
    cursor.execute("INSERT INTO tasks (name, time, priority) VALUES (?, ?, ?)", (name, time, priority))
    conn.commit()

def update_task(choice_task,new_name,new_time,new_priority):
    cursor.execute("UPDATE tasks SET name = ?, time = ?, priority = ? WHERE id = ?",(new_name, new_time, new_priority, choice_task))
    conn.commit()

def delete_task(task_id):
    cursor.execute("DELETE FROM tasks where id = ?",(task_id,))
    conn.commit()

def main():
    while True:
        print("\nToDo List for Productivity!!!")
        print(100*'*')
        print("1. List Tasks")
        print("2. Add Tasks")
        print("3. Update Tasks")
        print("4. Delete Tasks")
        print("5. Exit app")
        choice = input("Enter what you would like to do: ")
        print('*'*100)
        match choice:
            case '1':
                list_task()

            case '2':
                name = input("Enter task to add: ")
                time = input("Enter the deadline: ")
                priority = input("Enter the importance of task: ")
                add_task(name, time, priority)

            case '3':
                choice_task = input("Which task do you want to update: ")
                new_name = input("Enter new task to add: ")
                new_time = input("Enter updated the deadline: ")
                new_priority = input("Enter the importance of task: ")
                update_task(choice_task, new_name, new_time, new_priority)

            case '4':
                task_id = input("Enter the task to delete: ")
                delete_task(task_id)

            case '5':
                break

            case __:
                print("Enter valid choice")

    conn.close()

if __name__ == "__main__":
    main()