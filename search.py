from datetime import date, datetime

def search_tasks(subjects):
    search_name = input("Enter the task name to search: ").strip()

    if search_name == "":
        print("Task name cannot be empty.")
        return

    found = False

    for subject_name, topics in subjects.items():
        for topic_name, tasks in topics.items():
            for task in tasks:
                if search_name.lower() in task["name"].lower():
                    if not found:
                        print("\n========== SEARCH RESULTS ==========")

                    found = True

                    status = (
                        "Completed"
                        if task.get("completed", False)
                        else "Not Completed"
                    )

                    priority = task.get("priority", "Medium")
                    due_date = task.get("due_date") or "Not set"

                    print(f"\nTask     : {task['name']}")
                    print(f"Subject  : {subject_name}")
                    print(f"Topic    : {topic_name}")
                    print(f"Status   : {status}")
                    print(f"Priority : {priority}")
                    print(f"Due date : {due_date}")

    if found:
        print("\n====================================")
    else:
        print("No matching tasks found.")



def filter_tasks_by_priority(subjects):
    priority_filter = input(
        "Enter priority to filter (High/Medium/Low): "
    ).strip().lower()

    if priority_filter not in ["high", "medium", "low"]:
        print("Invalid priority. Choose High, Medium, or Low.")
        return

    found = False

    for subject_name, topics in subjects.items():
        for topic_name, tasks in topics.items():
            for task in tasks:
                priority = task.get("priority", "Medium")

                if priority.lower() == priority_filter:
                    if not found:
                        print("\n========== FILTERED TASKS ==========")

                    found = True

                    status = (
                        "Completed"
                        if task.get("completed", False)
                        else "Not Completed"
                    )

                    due_date = task.get("due_date") or "Not set"

                    print(f"\nTask     : {task['name']}")
                    print(f"Subject  : {subject_name}")
                    print(f"Topic    : {topic_name}")
                    print(f"Status   : {status}")
                    print(f"Priority : {priority}")
                    print(f"Due date : {due_date}")

    if found:
        print("\n====================================")
    else:
        print(f"No tasks found with {priority_filter.title()} priority.")



def search_and_filter_menu(subjects):
    while True:
        print("1. Search tasks by name")
        print("2. Filter tasks by priority")
        print("3. Filter by completion status")
        print("4. Filter by deadline")
        print("5. Back to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            search_tasks(subjects)
        elif choice == "2":
            filter_tasks_by_priority(subjects)
        elif choice == "3":
            filter_tasks_by_status(subjects)
        elif choice == "4":
            filter_tasks_by_deadline(subjects)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")



def filter_tasks_by_status(subjects):
    status_filter = input(
        "Show completed or pending tasks? "
    ).strip().lower()

    if status_filter not in ["completed", "pending"]:
        print("Invalid status. Enter Completed or Pending.")
        return

    expected_status = status_filter == "completed"
    found = False

    for subject_name, topics in subjects.items():
        for topic_name, tasks in topics.items():
            for task in tasks:
                is_completed = task.get("completed", False)

                if is_completed == expected_status:
                    if not found:
                        print("\n========== FILTERED TASKS ==========")

                    found = True

                    print(f"\nTask     : {task['name']}")
                    print(f"Subject  : {subject_name}")
                    print(f"Topic    : {topic_name}")
                    print(
                        "Status   : "
                        + ("Completed" if is_completed else "Not Completed")
                    )
                    print(
                        f"Priority : {task.get('priority', 'Medium')}"
                    )
                    print(
                        f"Due date : {task.get('due_date') or 'Not set'}"
                    )

    if found:
        print("\n====================================")
    else:
        print(f"No {status_filter} tasks found.")
        

def filter_tasks_by_deadline(subjects):
    print("\n===== FILTER TASKS BY DEADLINE =====")
    print("1. Overdue tasks")
    print("2. Tasks due today")
    print("3. Upcoming tasks")
    
    choice = input("Enter your choice: ").strip()

    if choice not in ["1", "2", "3"]:
        print("Invalid choice. Please select 1, 2, or 3.")
        return

    today = date.today()
    days = None

    if choice == "3":
        try:
            days = int(input("Show tasks due within how many days? ").strip())

            if days < 0:
                print("Number of days cannot be negative.")
                return

        except ValueError:
            print("Please enter a valid whole number.")
            return

    found = False

    for subject_name, topics in subjects.items():
        for topic_name, tasks in topics.items():
            for task in tasks:
                # Ignore completed tasks and tasks without a deadline
                if task.get("completed", False):
                    continue

                due_date = task.get("due_date")

                if not due_date:
                    continue

                try:
                    deadline = datetime.strptime(
                        due_date, "%Y-%m-%d"
                    ).date()
                except ValueError:
                    continue

                if choice == "1":
                    matches = deadline < today
                elif choice == "2":
                    matches = deadline == today
                else:
                    matches = today < deadline <= today.replace(
                        day=today.day
                    ) if False else today < deadline <= (
                        today + __import__("datetime").timedelta(days=days)
                    )

                if matches:
                    if not found:
                        print("\n========== DEADLINE RESULTS ==========")

                    found = True

                    print(f"\nTask     : {task['name']}")
                    print(f"Subject  : {subject_name}")
                    print(f"Topic    : {topic_name}")
                    print(f"Priority : {task.get('priority', 'Medium')}")
                    print(f"Due date : {due_date}")

    if not found:
        messages = {
            "1": "No overdue tasks found.",
            "2": "No tasks are due today.",
            "3": f"No pending tasks due within the next {days} days."
        }
        print(messages[choice])
    else:
        print("\n======================================")
