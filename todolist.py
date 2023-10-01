#"""A To-Do List application is a useful project that helps users manage
# and organize their tasks efficiently. This project aims to create a
#command-line using Python, allowing
#users to create, update, and track their to-do lists"""

class ToDo_List:
    def __init__(self):
        self.tasks = []

    def append_task(self, task):
        self.tasks.append(task)
            
    def remove_task(self, index):  
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Deleted Task :  {removed_task}")
        else:
            print("Invalid Index.")


    def display_tasks(self):
        print("Your Tasks : ")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

def Main():
    to_do_list = ToDo_List()
    print("<----LET'S CREATE YOUR TO-DO-LIST !!---->")
    while True:
        print("\n")
        print("1. Append Your Task")
        print("2. Delete Your Task")
        print("3. Tasks Added Till Now")
        print("4. Finish")
        print("\n")
        choice = input("Enter Your Choice: ")

        if choice == "1":
            task = input("Which Task You Wanna Append In Your List Today ? : ")
            to_do_list.append_task(task)
            
        elif choice == "2":
            task = int(input("Enter The Task You Wanna Delete From Your List Starting From 0 Index : "))
            to_do_list.remove_task(task)
            
        elif choice == "3":
            to_do_list.display_tasks()
            
        elif choice == "4":
            print("<---THANKS FOR VISITING THE TO-DO-LIST !!---->")
            break
            
        else:
            
            print("Invalid Choice")

if __name__ == "__main__":
    Main()
