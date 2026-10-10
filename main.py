import json

subjects = {}


def save_data():
    with open("subjects.json", "w") as file:
        json.dump(subjects, file, indent=4)


def load_data():
    global subjects

    try:
        with open("subjects.json", "r") as file:
            subjects = json.load(file)
    except FileNotFoundError:
        subjects = {}


load_data()

def find_subject_key(subject_name):
    for subject in subjects:
        if subject_name.lower() == subject.lower():
            return subject
    
    return None

def find_topic_key(subject_name, topic_name):
    for topic in subjects[subject_name]:
        if topic_name.lower() == topic.lower():
            return topic

    return None


def display_menu():
    print("\n===============================")
    print("           STUDY ASSISTANT")
    print("===============================")
    print("1. Add Subject")
    print("2. View Subjects")
    print("3. Add Topic")
    print("4. View Topics")
    print("5. Add Task")
    print("6. View Tasks")
    print("7. Mark as completed")
    print("8. Delete Subject")
    print("9. Delete Topic")
    print("10. Delete Task")
    print("11. View Study Progress")
    print("12. View Subject-wise Progress")
    print("13. Exit")



def add_subject():
    subject_name = input("Enter the subject name: ").strip()

    if subject_name == "":
        print("Subject name cannot be empty.")
        return

    existing_subject = find_subject_key(subject_name)

    if existing_subject is not None:
        print("Subject already exists.")
        return

    subjects[subject_name] = {}
    print(f"{subject_name} added successfully!")


def view_subjects():
    if not subjects:
        print("No subjects added yet.")
        return

    print("\nYour Subjects:")

    for index, subject in enumerate(subjects, start=1):
        print(f"{index}. {subject}")


def add_topic():
    subject_name = input("Enter the subject name to add a topic: ").strip()

    subject_name=find_subject_key(subject_name)
    
    if subject_name is None:
        print("Subject not found. Please add the subject first.")
        return

    topic_name = input("Enter the topic name: ").strip()

    if topic_name == "":
        print("Topic name cannot be empty.")
        return

    # Check for duplicate topic, ignoring case
    for topic in subjects[subject_name]:
        if topic_name.lower() == topic.lower():
            print("Topic already exists in this subject. Please enter a new topic name.")
            return

    subjects[subject_name][topic_name] = []

    print(
        f"Topic '{topic_name}' added to subject "
        f"'{subject_name}' successfully!"
    )


def view_topics():
    subject_name = input("Enter the subject name to view topics: ").strip()

    subject_name=find_subject_key(subject_name)

    if subject_name is None:
        print("Subject not found. Please add the subject first.")
        return

    topics = subjects[subject_name]

    if not topics:
        print(f"No topics have been added for subject '{subject_name}'.")
        return

    print(f"\nTopics for subject '{subject_name}':")

    for index, topic in enumerate(topics, start=1):
        print(f"{index}. {topic}")


def add_task():
    subject_name = input("Enter the subject name to add a task: ").strip()

    subject_name=find_subject_key(subject_name)

    if subject_name is None:
        print("Subject not found. Please add the subject first.")
        return

    topic_name = input("Enter the topic name to add a task: ").strip()

    topic_name = find_topic_key(subject_name, topic_name)

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
            print(
                "Task already exists in the topic. "
                "Please enter a new task name."
            )
            return

    subjects[subject_name][topic_name].append({
        "name": task_name,
        "completed": False
    })

    print(
        f"Task '{task_name}' added to topic '{topic_name}' "
        f"in subject '{subject_name}' successfully"
    )


def view_tasks():
    subject_name = input("Enter the subject name to view tasks: ").strip()

    subject_name = find_subject_key(subject_name)

    if subject_name is None:
        print("Subject not found. Please add the subject first.")
        return

    topics = subjects[subject_name]

    if not topics:
        print(f"No topics have been added for subject '{subject_name}'.")
        return

    print(f"\nTopics for subject '{subject_name}':")

    for index, topic in enumerate(topics, start=1):
        print(f"{index}. {topic}")

        tasks = topics[topic]

        if not tasks:
            print(f"  No tasks have been added for topic '{topic}'.")
        else:
            print(f"  Tasks for topic '{topic}':")

            for task_index, task in enumerate(tasks, start=1):

                if task["completed"]:
                    status = "Completed"
                else:
                    status = "Not Completed"

                print(
                    f"    {task_index}. "
                    f"{task['name']} - {status}"
                )


def mark_task_completed():
    subject_name = input(
        "Enter the subject name: "
    ).strip()

    # Find the actual subject key, ignoring case
    subject_name = find_subject_key(subject_name)

    if subject_name is None:
        print("Subject not found. Please add the subject first.")
        return

    topic_name = input("Enter the topic name: ").strip()

    # Find the actual topic key, ignoring case
    topic_name = find_topic_key(subject_name, topic_name)
    
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


def delete_subject():
    subject_name = input("Enter the subject name to delete: ").strip()

    subject_name = find_subject_key(subject_name)

    if subject_name is None:
        print("Subject not found. Please add the subject first.")
        return

    subjects.pop(subject_name)

    print(
        f"Subject '{subject_name}' and all its topics "
        f"and tasks have been deleted successfully!"
    )


def delete_topic():
    subject_name = input("Enter the subject name to delete a topic: ").strip()

    subject_name = find_subject_key(subject_name)

    if subject_name is None:
        print("Subject not found. Please add the subject first.")
        return

    topic_name = input("Enter the topic name to delete: ").strip()
    
    if topic_name == "":
        print("Topic name cannot be empty.")
        return
    topic_name = find_topic_key(subject_name, topic_name)

    if topic_name is None:
        print("Topic not found. Please add the topic first.")
        return

    subjects[subject_name].pop(topic_name)

    print(
        f"Topic '{topic_name}' and all its tasks have been "
        f"deleted successfully from subject '{subject_name}'!"
    )


def delete_task():
    subject_name = input("Enter the subject name to delete a task: ").strip()

    subject_name = find_subject_key(subject_name)

    if subject_name is None:
        print("Subject not found. Please add the subject first.")
        return


    topic_name = input("Enter the topic name to delete a task: ").strip()

    topic_name = find_topic_key(subject_name, topic_name)

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


def view_study_progress():
    total_subjects = len(subjects)
    total_topics = 0
    total_tasks = 0
    completed_tasks = 0

    for subject in subjects:
        topics = subjects[subject]
        total_topics += len(topics)

        for topic in topics:
            tasks = topics[topic]
            total_tasks += len(tasks)

            for task in tasks:
                if task["completed"]:
                    completed_tasks += 1

    pending_tasks = total_tasks - completed_tasks

    if total_tasks > 0:
        progress_percentage = (completed_tasks / total_tasks) * 100
    else:
        progress_percentage = 0

    print("\n========== STUDY PROGRESS ==========")
    print(f"Total Subjects       : {total_subjects}")
    print(f"Total Topics         : {total_topics}")
    print(f"Total Tasks          : {total_tasks}")
    print(f"Completed Tasks      : {completed_tasks}")
    print(f"Pending Tasks        : {pending_tasks}")
    print(f"Overall Progress     : {progress_percentage:.2f}%")
    print("====================================")
    

def view_subject_progress():
    if not subjects:
        print("\nNo subjects available. Add a subject first.")
        return

    print("\n========== SUBJECT-WISE PROGRESS ==========")

    for subject in subjects:
        topics = subjects[subject]

        total_tasks = 0
        completed_tasks = 0

        # Calculate subject-wise progress
        for topic in topics:
            tasks = topics[topic]

            total_tasks += len(tasks)

            for task in tasks:
                if task["completed"]:
                    completed_tasks += 1

        pending_tasks = total_tasks - completed_tasks

        if total_tasks > 0:
            progress = (completed_tasks / total_tasks) * 100
        else:
            progress = 0

        print(f"\nSubject: {subject}")
        print(f"Total Tasks     : {total_tasks}")
        print(f"Completed Tasks : {completed_tasks}")
        print(f"Pending Tasks   : {pending_tasks}")
        print(f"Progress        : {progress:.2f}%")

        # Calculate topic-wise progress
        print("\n  Topic-wise Progress:")

        if not topics:
            print("  No topics available.")
            continue

        for topic in topics:
            tasks = topics[topic]
            topic_total = len(tasks)
            topic_completed = 0

            for task in tasks:
                if task["completed"]:
                    topic_completed += 1

            if topic_total > 0:
                topic_progress = (
                    topic_completed / topic_total
                ) * 100
            else:
                topic_progress = 0

            print(
                f"  {topic}: "
                f"{topic_completed}/{topic_total} tasks completed "
                f"({topic_progress:.2f}%)"
            )

    print("\n===========================================")

    


while True:
    display_menu()

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_subject()

    elif choice == "2":
        view_subjects()

    elif choice == "3":
        add_topic()

    elif choice == "4":
        view_topics()

    elif choice == "5":
        add_task()

    elif choice == "6":
        view_tasks()

    elif choice == "7":
        mark_task_completed()

    elif choice == "8":
        delete_subject()

    elif choice == "9":
        delete_topic()

    elif choice == "10":
        delete_task()
        
    elif choice == "11":
        view_study_progress()
        
    elif choice == "12":
        view_subject_progress()

    elif choice == "13":
        save_data()
        print("Data saved to subjects.json.")
        print("Thank you for using the study assistant.")
        break

    else:
        print("Invalid choice. Please try again.")
