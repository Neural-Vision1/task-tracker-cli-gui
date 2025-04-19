from main import *
import time
from datetime import datetime, timedelta

conn , cursor = connect_db()

def add_task(priority, category, task, due_date):
    cursor.execute('''
        INSERT INTO Tasks(Priority, Category, Task , Due_Date) VALUES (?,?,?,?)
''', (priority, category, task, due_date))

    conn.commit()
    print('Task added successfulyy')

def view_tasks():
    cursor.execute("SELECT Id, Priority, Category, Task, Completed, Due_Date FROM Tasks")
    tasks = cursor.fetchall()

    print("\n📋 Your To-Do List:\n")
    print(f"{'ID':<5} {'Priority':<10} {'Category':<12} {'Task':<25} {'Status':<12} {'Due Date':<12}")
    print("=" * 80)

    for task in tasks:
        Id, Priority, Category, Task, Completed, Due_Date = task
        status = "Done ✅" if Completed else "Pending..."
        print(f"{Id:<5} {Priority:<10} {Category:<12} {Task:<25} {status:<12} {Due_Date:<12}")

    print("=" * 80)

def get_due_date():
    while True:
        date = input("Enter due date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date, '%Y-%m-%d').date()
            return date
        except ValueError:
            print('Invalid Format of date')

def reminder():
    today = datetime.today().date()
    tomorrow = today + timedelta(days=1)

    cursor.execute('SELECT Task, Due_date FROM Tasks WHERE Due_Date = ?', (tomorrow,))
    task_due_for_tomorrow = cursor.fetchall()

    for task in task_due_for_tomorrow:
        print(f"Reminder : Task '{task[0]}' is due tomorrow ({task[1]})!")

def delete_task():
    view_tasks()
    a = int(input('\nInput the ID of the task you want to delete: '))

    cursor.execute('DELETE FROM Tasks WHERE Id = ?', (a,))
    conn.commit()

    cursor.execute('''
        UPDATE Tasks
        SET Id = Id - 1
        WHERE Id > ?''', (a,))
    
    conn.commit()

def complete():
    view_tasks()
    b = int(input("Enter the Id of task which you've completed: "))

    cursor.execute("UPDATE Tasks SET Completed = 1 WHERE Id = ?", (b,))
    conn.commit()

    print("\n✅ Task marked as Done!")



