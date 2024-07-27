class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
        self.completed = False


class ToDoList:
    def __init__(self):
        print("Welcome to our to do list application")
        self.tasks = []
        self.main()

    def add_task(self):
        title = input("Enter task title: ")
        priority = input("Enter task priority (H/M/L): ")
        self.tasks.append(Task(title, priority))
        print("Task added successfully!")

    def remove_task(self):
        self.view_tasks()
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            print("Task removed successfully!")
        else:
            print("Invalid task number. Try again.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        print("\n--- Your Tasks ---")
        for i, task in enumerate(self.tasks, start=1):
            status = "✓" if task.completed else " "
            print(f"{i}. [{status}] {task.title} ({task.priority})")

    def save_to_file(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task.title} | {task.priority}\n")

    def main(self):
        while True:
            print("\n--- To-Do List Menu ---")
            print("1. Add a new task")
            print("2. Remove a task")
            print("3. View all tasks")
            print("4. Save tasks to file")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.remove_task()
            elif choice == "3":
                self.view_tasks()
            elif choice == "4":
                self.save_to_file()
                print("Tasks saved to 'tasks.txt'.")
            elif choice == "5":
                print("Thank you for using the to-do list application!")
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    my_todo_list = ToDoList()
