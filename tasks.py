from datetime import datetime, date
from subjects import find_subject_key
from topics import find_topic_key


def add_task(subjects):
    subject_name = input("Enter the subject name to add a task: ").strip()
    subject_name = find_subject_key(subjects, subject_name)

    if subject_name is None:
        print("Subject not found. Please add the subject first.")
        return

    topic_name = input("Enter the topic name to add a task: ").strip()
    topic_name = find_topic_key(subjects, subject_name, topic_name)

    if topic_name is None:
        print("Topic not found. Please add the topic first.")
        return

    task_name = input("Enter the task name: ").strip()

    if task_name == "":
        print("Task name cannot be empty.")
        return

    # Check for duplicate task, ignoring case
    for task in subjects[subject_name][topic_name]:
        if task["name"].lower() == task_name.lower():
            print("Task already exists in this topic.")
            return

    # Get and validate priority
    priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()

    if priority not in ["High", "Medium", "Low"]:
        print("Invalid priority. Choose High, Medium, or Low.")
        return

    # Get and validate optional due date
    due_date = input(
        "Enter due date (YYYY-MM-DD), or press Enter to skip: "
    ).strip()

    if due_date:
        try:
            parsed_date = datetime.strptime(
                due_date, "%Y-%m-%d"
            ).date()

            if parsed_date.strftime("%Y-%m-%d") != due_date:
                raise ValueError

        except ValueError:
            print(
                "Invalid date. Use YYYY-MM-DD, "
                "for example 2026-12-25."
            )
            return

    # Save the new task
    new_task = {
        "name": task_name,
        "completed": False,
        "priority": priority,
        "due_date": due_date
    }

    subjects[subject_name][topic_name].append(new_task)

    print(f"Task '{task_name}' added successfully!")
    print(f"Priority: {priority}")

    if due_date:
        print(f"Due date: {due_date}")
    else:
        print("Due date: Not set")




def view_tasks(subjects):
    subject_name = input("Enter the subject name to view tasks: ").strip()

    subject_name = find_subject_key(subjects, subject_name)

    if subject_name is None:
        print("Subject not found. Please add the subject first.")
        return

    topics = subjects[subject_name]

    if not topics:
        print(f"No topics have been added for '{subject_name}'.")
        return

    print(f"\nTasks for subject '{subject_name}':")

    for topic, tasks in topics.items():
        print(f"\nTopic: {topic}")

        if not tasks:
            print("  No tasks added yet.")
            continue

        for index, task in enumerate(tasks, start=1):
            status = (
                "Completed"
                if task["completed"]
                else "Not Completed"
            )

            # Defaults keep older saved tasks compatible
            priority = task.get("priority", "Medium")
            due_date = task.get("due_date", "")

            print(f"  {index}. {task['name']}")
            print(f"     Status   : {status}")
            print(f"     Priority : {priority}")
            print(f"     Due date : {due_date or 'Not set'}")
            

def delete_task(subjects):
    subject_name = input("Enter the subject name to delete a task: ").strip()

    subject_name = find_subject_key(subjects,subject_name)

    if subject_name is None:
        print("Subject not found. Please add the subject first.")
        return


    topic_name = input("Enter the topic name to delete a task: ").strip()

    topic_name = find_topic_key(subjects,subject_name, topic_name)

    if topic_name is None:
        print("Topic not found. Please add the topic first.")
        return

    task_name = input("Enter the task name to delete: ").strip()
    
    if task_name == "":
        print("Task name cannot be empty.")
        return

    tasks = subjects[subject_name][topic_name]

    for task in tasks:
        if task["name"].lower() == task_name.lower():
            tasks.remove(task)

            print(
                f"Task '{task_name}' has been deleted successfully "
                f"from topic '{topic_name}' in subject "
                f"'{subject_name}'!"
            )
            return

    print(
        f"Task '{task_name}' not found in topic '{topic_name}'."
    )
    
    
def view_deadline_tasks(subjects):
    today = date.today()

    overdue_tasks = []
    upcoming_tasks = []

    for subject, topics in subjects.items():
        for topic, tasks in topics.items():
            for task in tasks:
                due_date = task.get("due_date", "")

                # Ignore tasks without a deadline or already completed
                if not due_date or task.get("completed", False):
                    continue

                try:
                    deadline = datetime.strptime(
                        due_date, "%Y-%m-%d"
                    ).date()
                except ValueError:
                    continue

                task_details = (
                    f"{task['name']} | "
                    f"Subject: {subject} | "
                    f"Topic: {topic} | "
                    f"Priority: {task.get('priority', 'Medium')} | "
                    f"Due: {due_date}"
                )

                if deadline < today:
                    overdue_tasks.append((deadline, task_details))
                else:
                    upcoming_tasks.append((deadline, task_details))

    # Sort tasks by their deadline
    overdue_tasks.sort(key=lambda item: item[0])
    upcoming_tasks.sort(key=lambda item: item[0])

    print("\n========== OVERDUE TASKS ==========")

    if overdue_tasks:
        for _, details in overdue_tasks:
            print(details)
    else:
        print("No overdue tasks.")

    print("\n======= UPCOMING / DUE TODAY =======")

    if upcoming_tasks:
        for _, details in upcoming_tasks:
            print(details)
    else:
        print("No upcoming tasks.")

    print("====================================")

    
    
def mark_task_completed(subjects):
    subject_name = input("Enter the subject name: ").strip()

    # Find the actual subject key, ignoring case
    subject_name = find_subject_key(subjects,subject_name)

    if subject_name is None:
        print("Subject not found. Please add the subject first.")
        return

    topic_name = input("Enter the topic name: ").strip()

    # Find the actual topic key, ignoring case
    topic_name = find_topic_key(subjects, subject_name, topic_name)
    
    if topic_name is None:
        print("Topic not found. Please add the topic first.")
        return

    tasks = subjects[subject_name][topic_name]

    if not tasks:
        print("No tasks have been added to this topic.")
        return

    print(f"\nTasks for topic '{topic_name}':")

    for index, task in enumerate(tasks, start=1):

        if task["completed"]:
            status = "Completed"
        else:
            status = "Not Completed"

        print(f"{index}. {task['name']} - {status}")

    try:
        task_number = int(
            input("Enter the task number to mark as completed: ")
        )
    except ValueError:
        print("Please enter a valid task number.")
        return

    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number. Please enter a valid task number.")
        return

    tasks[task_number - 1]["completed"] = True

    print(
        f"Task '{tasks[task_number - 1]['name']}' "
        f"marked as completed!"
    )


def edit_task(subjects):
    subject_name = input("Enter the subject name: ").strip()
    subject_name = find_subject_key(subjects, subject_name)

    if subject_name is None:
        print("Subject not found.")
        return

    topic_name = input("Enter the topic name: ").strip()
    topic_name = find_topic_key(subjects, subject_name, topic_name)

    if topic_name is None:
        print("Topic not found.")
        return

    tasks = subjects[subject_name][topic_name]

    if not tasks:
        print("No tasks available in this topic.")
        return

    print(f"\nTasks in topic '{topic_name}':")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['name']}")

    try:
        task_number = int(input("Enter the task number to edit: "))
    except ValueError:
        print("Please enter a valid task number.")
        return

    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number.")
        return

    selected_task = tasks[task_number - 1]

    while True:
        print("\n========== EDIT TASK ==========")
        print(f"Task: {selected_task['name']}")
        print("1. Rename task")
        print("2. Change priority")
        print("3. Change deadline")
        print("4. Return")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            new_name = input("Enter the new task name: ").strip()

            if not new_name:
                print("Task name cannot be empty.")
                continue

            duplicate = False

            for index, task in enumerate(tasks):
                if (
                    index != task_number - 1
                    and task["name"].lower() == new_name.lower()
                ):
                    duplicate = True
                    break

            if duplicate:
                print("A task with this name already exists.")
                continue

            old_name = selected_task["name"]
            selected_task["name"] = new_name
            print(f"Task renamed from '{old_name}' to '{new_name}'.")

        elif choice == "2":
            priority = input(
                "Enter priority (High/Medium/Low): "
            ).strip().capitalize()

            if priority not in ["High", "Medium", "Low"]:
                print("Invalid priority. Choose High, Medium, or Low.")
                continue

            selected_task["priority"] = priority
            print(f"Priority updated to {priority}.")

        elif choice == "3":
            due_date = input(
                "Enter new deadline (YYYY-MM-DD), "
                "or press Enter to clear it: "
            ).strip()

            if due_date:
                try:
                    parsed_date = datetime.strptime(
                        due_date, "%Y-%m-%d"
                    ).date()

                    if parsed_date.strftime("%Y-%m-%d") != due_date:
                        raise ValueError

                except ValueError:
                    print("Invalid date. Use YYYY-MM-DD.")
                    continue

            selected_task["due_date"] = due_date

            if due_date:
                print(f"Deadline updated to {due_date}.")
            else:
                print("Deadline cleared.")

        elif choice == "4":
            print("Returning from task editing.")
            break

        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")


def sort_tasks(subjects):
    subject_name = input("Enter the subject name: ").strip()
    subject_name = find_subject_key(subjects, subject_name)

    if subject_name is None:
        print("Subject not found.")
        return

    topic_name = input("Enter the topic name: ").strip()
    topic_name = find_topic_key(subjects, subject_name, topic_name)

    if topic_name is None:
        print("Topic not found.")
        return

    tasks = subjects[subject_name][topic_name]

    if not tasks:
        print("No tasks available in this topic.")
        return

    while True:
        print("\n========== SORT TASKS ==========")
        print("1. Sort by name (A-Z)")
        print("2. Sort by priority")
        print("3. Sort by deadline")
        print("4. Sort by completion status")
        print("5. Return")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            sorted_tasks = sorted(
                tasks,
                key=lambda task: task["name"].lower()
            )
            title = "Name (A-Z)"

        elif choice == "2":
            priority_order = {
                "High": 1,
                "Medium": 2,
                "Low": 3
            }

            sorted_tasks = sorted(
                tasks,
                key=lambda task: priority_order.get(
                    task.get("priority", "Medium").capitalize(),
                    2
                )
            )
            title = "Priority (High to Low)"

        elif choice == "3":
            def deadline_key(task):
                due_date = task.get("due_date", "")

                if not due_date:
                    return (1, date.max)

                try:
                    parsed_date = datetime.strptime(
                        due_date, "%Y-%m-%d"
                    ).date()
                    return (0, parsed_date)
                except ValueError:
                    return (1, date.max)

            sorted_tasks = sorted(tasks, key=deadline_key)
            title = "Deadline (Earliest First)"

        elif choice == "4":
            sorted_tasks = sorted(
                tasks,
                key=lambda task: task.get("completed", False)
            )
            title = "Completion Status (Pending First)"

        elif choice == "5":
            print("Returning to the previous menu.")
            break

        else:
            print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")
            continue

        print(f"\nTasks sorted by {title} in '{topic_name}':")

        for index, task in enumerate(sorted_tasks, start=1):
            status = (
                "Completed"
                if task.get("completed", False)
                else "Pending"
            )

            print(f"\n{index}. {task['name']}")
            print(f"   Status   : {status}")
            print(f"   Priority : {task.get('priority', 'Medium')}")
            print(f"   Deadline : {task.get('due_date') or 'Not set'}")
