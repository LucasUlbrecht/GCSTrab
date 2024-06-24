# main.py
from controller import Controller

def main():
    controller = Controller()
    
    while True:
        print("1. Create a new issue")
        print("2. Add a comment to an issue")
        print("3. Close an issue")
        print("4. Display all issues")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            controller.create_issue()
        elif choice == '2':
            index = int(input("Enter the index of the issue: "))
            controller.add_comment_to_issue(index)
        elif choice == '3':
            index = int(input("Enter the index of the issue: "))
            controller.close_issue(index)
        elif choice == '4':
            controller.display_all_issues()
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
