import os
from datetime import datetime, timedelta

# اسم ملف التخزين
TASKS_FILE = "tasks.txt"

# -------------------------------
# 1. تحميل المهام من الملف
# -------------------------------
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            for line in file:
                # تقسيم كل سطر لمهمة وموعد
                task, due_date = line.strip().split(" | ")
                tasks.append((task, due_date))
    return tasks

# -------------------------------
# 2. حفظ المهام في الملف
# -------------------------------
def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        for task, due_date in tasks:
            file.write(f"{task} | {due_date}\n")

# -------------------------------
# 3. إضافة مهمة جديدة
# -------------------------------
def add_task():
    task = input("Enter the new task: ")
    due_date = input("Enter due date (YYYY-MM-DD HH:MM): ")
    tasks = load_tasks()
    tasks.append((task, due_date))
    save_tasks(tasks)
    print("✅ Task added successfully!\n")

# -------------------------------
# 4. عرض المهام
# -------------------------------
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📂 No tasks found.\n")
    else:
        print("📋 Task List:")
        for i, (task, due_date) in enumerate(tasks, start=1):
            print(f"{i}. {task} (Due: {due_date})")
        print()

# -------------------------------
# 5. تعديل مهمة
# -------------------------------
def edit_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to edit.\n")
        return
    view_tasks()
    try:
        task_num = int(input("Enter the task number to edit: "))
        if 1 <= task_num <= len(tasks):
            new_task = input("Enter the new task description: ")
            new_due = input("Enter the new due date (YYYY-MM-DD HH:MM): ")
            tasks[task_num - 1] = (new_task, new_due)
            save_tasks(tasks)
            print("✅ Task updated successfully!\n")
        else:
            print("❌ Invalid task number.\n")
    except ValueError:
        print("❌ Invalid input.\n")

# -------------------------------
# 6. حذف مهمة
# -------------------------------
def delete_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to delete.\n")
        return
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"✅ Task '{removed_task[0]}' deleted successfully!\n")
        else:
            print("❌ Invalid task number.\n")
    except ValueError:
        print("❌ Invalid input.\n")

# -------------------------------
# 7. التذكير بالمهام القريبة
# -------------------------------
def check_reminders():
    tasks = load_tasks()
    now = datetime.now()
    for task, due_date in tasks:
        try:
            due_datetime = datetime.strptime(due_date, "%Y-%m-%d %H:%M")
            if now <= due_datetime <= now + timedelta(hours=1):
                print(f"⏰ Reminder: '{task}' is due at {due_date}!")
        except ValueError:
            pass

# -------------------------------
# 8. القائمة الرئيسية
# -------------------------------
def main():
    while True:
        print("====== Task Manager ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Check Reminders")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            check_reminders()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
