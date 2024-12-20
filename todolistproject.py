# Define a list to store tasks
tasks=[]


# Display the menu and get user input
def display_menu():
    print("\nTo-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    return input("choose an option (1-5):")


# Add a task to the list
def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added!")


# Mark a task as completed
def view_tasks():
    if not self.tasks:
        print("No tasks to display.")
    else:
        print("\nYour To-Do List:")
        task_number=1
        for task in self.tasks:
            status = "Completed" if task["completed"] else "Pending"
            print(f"{idx}. {task['task']} [{status}]")
            task_number += 1


# Mark a task as completed
def mark_task_completed(self):
    self.view_tasks()
    if self.tasks:
            try:
                task_num = int(input("\nEnter the task number to mark as completed: "))
                if 1 <= task_num <= len(self.tasks):
                    self.tasks[task_num - 1]["completed"] = True
                    print(f"Task {task_num} marked as completed!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")


# Delete a task from the list
def delete_task():
    self.view_tasks()
    if self.tasks:
            try:
                task_num = int(input("\nEnter the task number to delete: "))
                if 1 <= task_num <= len(self.tasks):
                    removed_task = self.tasks.pop(task_num - 1)
                    print(f"Task '{removed_task['task']}' deleted!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number.")


# Main loop to keep the program running
while True:
    choice = display_menu()

    if choice == '1':
       add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_task_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting the To-Do Goodbye.")
        break
    else:
        print("Invalid choice, please try again.")