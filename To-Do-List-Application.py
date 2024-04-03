class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class TodoList:
    def __init__(self):
        self.tasks = []

    def adding_task(self, task):
        self.tasks.append(task)
        print(color.BLUE + "Task added successfully." + color.END)

    def deleting_task(self, index):
        try:
            index = int(index)  # Convert index to an integer
            if 1 <= index <= len(self.tasks):
                deleted_task = self.tasks.pop(index - 1)
                print(color.BLUE + "Task deleted successfully." + color.END)
            else:
                print(color.RED + "Enter valid task number." + color.END)
        except ValueError:
            print(color.RED + "Please enter a valid task number." + color.END)

    def marking_task_completed(self, task):
        if task in self.tasks:
            print(color.BLUE + "Task marked as completed." + color.END)
        else:
            print(color.RED + "Enter valid task number." + color.END)

    def list_tasks(self):
        print(color.BLUE + "Your To-Do List:" + color.END)
        for idx, task in enumerate(self.tasks, start=1):
            print(color.CYAN + f"{idx}. {task}" + color.END)


def main():
    todo_list = TodoList()

    while True:
        print(color.DARKCYAN + "\nOptions:" + color.END)
        print(color.PURPLE + "1. Add Task" + color.END)
        print(color.PURPLE + "2. Delete Task" + color.END)
        print(color.PURPLE + "3. Mark Task as Completed" + color.END)
        print(color.PURPLE + "4. List Tasks" + color.END)
        print(color.PURPLE + "5. Exit" + color.END)

        choice = input(color.CYAN + "Enter your choice: " + color.END)

        if choice == '1':
            task = input(color.GREEN + "Enter task to add: " + color.END)
            todo_list.adding_task(task)
        elif choice == '2':
            todo_list.list_tasks()
            task = input(color.GREEN + "Enter task number to delete: " + color.END)
            todo_list.deleting_task(task)
        elif choice == '3':
            task = input(color.GREEN + "Enter task to mark as completed: " + color.END)
            todo_list.marking_task_completed(task)
        elif choice == '4':
            todo_list.list_tasks()
        elif choice == '5':
            print(color.GREEN + "Bye, Have a nice day " + color.END)
            break
        else:
            print(color.RED + "Invalid choice. Please try again." + color.END)


if __name__ == "__main__":
    main()
