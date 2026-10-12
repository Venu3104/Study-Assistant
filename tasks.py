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

