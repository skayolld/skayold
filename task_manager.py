while True:
    print("\nWelcome to your Personal Task Manager 📝")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Edit a task")
    print("4. Delete a task")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")
    
    if choice == "1":
        task = input("Enter the new task: ")
        due_date = input ("Enter due date (YYYY-MM-DD HH:MM): ")
        with open("tasks.txt", "a", encoding="utf-8") as file:
            file.write(f"{task} | {due_date}\n")
        print("✅ Task added successfully!")
    elif choice == "2":
        try:
            with open("tasks.txt", "r", encoding="utf-8") as file:
                tasks = file.readlines()
                if tasks:
                    print("\n📋 Task List:")
                    for i, t in enumerate(tasks, start=1):
                        task_name, due = t.strip().split(" | ")
                        print (f"{i}. {task_name} (due : {due})")
                else:
                    print("No tasks found.")
        except FileNotFoundError:
            print("No task file exists yet.")
    elif choice == "3":
        try:
            with open("tasks.txt", "r", encoding="utf-8") as file:
                tasks = file.readlines()
            if tasks:
                print("\n📋 Task List:")
                for i, t in enumerate(tasks, start=1):
                    print(f"{i}. {t.strip()}")
                task_num = int(input("Enter the task number to edit: "))
                if 1 <= task_num <= len(tasks):
                    new_task = input("Enter the new task description: ")
                    tasks[task_num - 1] = new_task + "\n"
                    with open("tasks.txt", "w", encoding="utf-8") as file:
                        file.writelines(tasks)
                    print("✅ Task updated successfully!")
                else:
                    print("❌ Invalid task number.")
            else:
                print("No tasks to edit.")
        except FileNotFoundError:
            print("No task file exists yet.")
    elif choice == "4":
        try:
            with open("tasks.txt", "r", encoding="utf-8") as file:
                tasks = file.readlines()
            if tasks:
                print("\n📋 Task List:")
                for i, t in enumerate(tasks, start=1):
                    print(f"{i}. {t.strip()}")
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    with open("tasks.txt", "w", encoding="utf-8") as file:
                        file.writelines(tasks)
                    print(f"✅ Task '{removed_task.strip()}' deleted successfully!")
                else:
                    print("❌ Invalid task number.")
            else:
                print("No tasks to delete.")
        except FileNotFoundError:
            print("No task file exists yet.")
    elif choice == "5":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice, please enter a number from 1 to 5.")


