# TO  DO  LIST 

WORKPLACE = {
    "Work": [],
    "School": [{"Task": "HOMEWORK", "done": False}],
    "Home": [],
    "Groceries": [],
}

def display_tasks(tasks):
    """Display tasks in a user-friendly format"""
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. {task['Task']} [{status}]")

def addtask():
    """Add a new task to a workplace"""
    print("\nSelect Workplace:")
    print("1 for Work")
    print("2 for School")
    print("3 for Home")
    print("4 for Groceries")
    
    try:
        work_place = int(input("Select your WORKPLACE between [1-4]: "))
    except ValueError:
        print("Please enter a number between 1-4")
        return

    workplace_map = {
        1: "Work",
        2: "School",
        3: "Home",
        4: "Groceries"
    }

    if work_place not in workplace_map:
        print("Invalid choice.")
        return

    workplace = workplace_map[work_place]
    task = input("Enter the task you want to add: ").strip().upper()
    
    if not task:
        print("Task cannot be empty!")
        return

    WORKPLACE[workplace].append({"Task": task, "done": False})
    print(f"\nTask '{task}' added to {workplace}!")
    print(f"Updated {workplace} tasks:")
    display_tasks(WORKPLACE[workplace])

def deletetask():
    """Delete a task from a workplace"""
    print("\nSelect Workplace:")
    print("1 for Work")
    print("2 for School")
    print("3 for Home")
    print("4 for Groceries")

    try:
        work_place = int(input("Select your WORKPLACE between [1-4]: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    workplace_map = {
        1: "Work",
        2: "School",
        3: "Home",
        4: "Groceries"
    }

    if work_place not in workplace_map:
        print("Invalid choice.")
        return

    workplace = workplace_map[work_place]
    tasks = WORKPLACE[workplace]
    
    print(f"\nCurrent {workplace} tasks:")
    display_tasks(tasks)
    
    if not tasks:
        return

    task_to_delete = input("Enter the exact task name you want to delete: ").strip().upper()
    
    deleted = False
    for task in tasks[:]:  # Create a copy to iterate over
        if task["Task"] == task_to_delete:
            tasks.remove(task)
            deleted = True
            break
    
    if deleted:
        print(f"\nTask '{task_to_delete}' removed successfully!")
    else:
        print(f"\nTask '{task_to_delete}' not found. Please check the exact name.")
    
    print(f"Updated {workplace} tasks:")
    display_tasks(tasks)

def viewtask():
    """View tasks in a workplace"""
    print("\nSelect Workplace:")
    print("1 for Work")
    print("2 for School")
    print("3 for Home")
    print("4 for Groceries")

    try:
        work_place = int(input("Select workplace to view [1-4]: "))
    except ValueError:
        print("Please enter a number between 1-4")
        return

    workplace_map = {
        1: "Work",
        2: "School",
        3: "Home",
        4: "Groceries"
    }

    if work_place not in workplace_map:
        print("Invalid choice.")
        return

    workplace = workplace_map[work_place]
    print(f"\nTasks in {workplace}:")
    display_tasks(WORKPLACE[workplace])

def markas_complete():
    """Mark a task as complete"""
    print("\nSelect Workplace:")
    print("1 for Work")
    print("2 for School")
    print("3 for Home")
    print("4 for Groceries")

    try:
        work_place = int(input("Select workplace [1-4]: "))
    except ValueError:
        print("Please enter a number between 1-4")
        return

    workplace_map = {
        1: "Work",
        2: "School",
        3: "Home",
        4: "Groceries"
    }

    if work_place not in workplace_map:
        print("Invalid choice.")
        return

    workplace = workplace_map[work_place]
    tasks = WORKPLACE[workplace]
    
    print(f"\nCurrent {workplace} tasks:")
    display_tasks(tasks)
    
    if not tasks:
        return

    try:
        task_num = int(input("Enter the task number to mark complete: "))
        if task_num < 1 or task_num > len(tasks):
            print("Invalid task number!")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tasks[task_num-1]["done"] = True
    print(f"\nTask '{tasks[task_num-1]['Task']}' marked as complete!")
    print(f"Updated {workplace} tasks:")
    display_tasks(tasks)

def main():
    """Main program loop"""
    print("WELCOME TO TO-DO-LIST MANAGER")
    
    while True:
        print("\nMAIN MENU:")
        print("1. ADD TASK")
        print("2. DELETE TASK")
        print("3. VIEW TASKS")
        print("4. MARK TASK AS COMPLETE")
        print("5. EXIT")

        try:
            choice = int(input("Select option [1-5]: "))
        except ValueError:
            print("Please enter a number between 1-5")
            continue

        if choice == 1:
            addtask()
        elif choice == 2:
            deletetask()
        elif choice == 3:
            viewtask()
        elif choice == 4:
            markas_complete()
        elif choice == 5:
            print("\nThank you for using To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5")

if __name__ == "__main__":
    main()