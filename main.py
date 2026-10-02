subjects={}


def display_menu():
    print("\n===============================")
    print("           STUDY ASSISTANT       ")
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
    print("11. Exit")


def add_subject():
    subject_name=input("Enter the subject name: ")
    
    if subject_name in subjects:
        print("subject already exists.")
        return
    
    subjects[subject_name] = {}
    
    print(f"{subject_name} added successfully!")
    
def view_subjects():
    if not subjects:
        print("No subjects added yet.")
        return
    
    print("\n Your Subjects:")
    
    for index, subject in enumerate(subjects,start=1):
            print(f"{index}. {subject}") 
            
            
            
def add_topic():
    subject_name=input("Enter the subject name to add a topic: ")
    
    if subject_name not in subjects:
        print("Subject not found. Please add the subject first.")
        return
    
    topic_name=input("Enter the topic name: ")
    
    if topic_name in subjects[subject_name]:
        print("Topic is already exist in this subject, Please enter a new topic name.")
        return
    
    subjects[subject_name][topic_name]=[]
    
    print(f"Topic '{topic_name}' added to subject '{subject_name}' successfully!")
    
    

def view_topics():
    subject_name=input("Enter the subject name to view topics: ")
    
    if subject_name not in subjects:
        print("Subject not found. Please add the subject first.")
        return
    
    for subject, topics in subjects.items():
        
        if subject==subject_name:
            if not topics:
                print(f"No topics have been added for subject '{subject_name}'.")
                return
            
            print(f"\nTopics for subject '{subject_name}':")
            for index, topic in enumerate(topics, start=1):
                print(f"{index}. {topic}")
                
             
            

def add_task():
    subject_name=input("Enter the subject name to add a task: ")
    
    if subject_name not in subjects:
        print("Subject not found. Please add the subject first.")
        return
    
    topic_name=input("Enter the topic name to add a task: ")
    
    if topic_name not in subjects[subject_name]:
        print("Topic not found. Please add the topic first.")
        return
    
    task_name=input("Enter the task name: ")
    
    for task in subjects[subject_name][topic_name]:
        if task["name"] == task_name:
            print("Task already exists in the topic. Please enter a new task name.")
            return
    
    subjects[subject_name][topic_name].append({"name": task_name, "completed": False})
    
    print(f"Task '{task_name}' added to topic '{topic_name}' in subject '{subject_name}' successfully")
    
    


def view_tasks():
    subject_name=input("Enter the subject name to view tasks: ")
    
    if subject_name not in subjects:
        print("Subject not found. Please add the subject first.")
        return
    
    for subject, topics in subjects.items():
        
        if subject==subject_name:
            if not topics:
                print(f"No topics have been added for subject '{subject_name}'.")
                return
            
            print(f"\nTopics for subject '{subject_name}':")
            for index, topic in enumerate(topics, start=1):
                print(f"{index}. {topic}")
                
                tasks=subjects[subject][topic]
                
                if not tasks:
                    print(f"  No tasks have been added for topic '{topic}'.")
                else:
                    print(f"  Tasks for topic '{topic}':")
                    for task_index, task in enumerate(tasks, start=1):
                        status=task["completed"]
                        
                        if status:
                            status="Completed"
                        else:
                            status="Not Completed"
                            
                        print(f"    {task_index}. {task['name']} - {status}")
                        

def mark_task_completed():
    subject_name = input("Enter the subject name: ")

    if subject_name not in subjects:
        print("Subject not found. Please add the subject first.")
        return

    topic_name = input("Enter the topic name: ")

    if topic_name not in subjects[subject_name]:
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
        task_number = int(input("Enter the task number to mark as completed: "))
    except ValueError:
        print("Please enter a valid task number.")
        return
        

    if(task_number<1 or task_number>len(tasks)):
        print("Invalid task number. please enter a valid task number.")
        return
        

    tasks[task_number - 1]["completed"] = True

    print(f"Task '{tasks[task_number - 1]['name']}' marked as completed!")
    
    
    

def delete_subject():
    subject_name= input("Enter the subject name to delete: ")
    if subject_name not in subjects:
        print("Subject not found. Please add the subject first.")
        return
    subjects.pop(subject_name)
    print(f"subject '{subject_name}' and all its topics and tasks have been deleted successfully!")
    
    

def delete_topic():
    subject_name= input("Enter the subject name to delete a topic: ")
    if subject_name not in subjects:
        print("Subject not found. Please add the subject first.")
        return
    topic_name= input("Enter the topic name to delete: ")
    if topic_name not in subjects[subject_name]:
        print("Topic not found. Please add the topic first.")
        return
    subjects[subject_name].pop(topic_name)
    print(f"Topic '{topic_name}' and all its tasks have been deleted successfully from subject '{subject_name}'!")
    
    
def delete_task():
    subject_name= input("Enter the subject name to delete a task: ")
    if subject_name not in subjects:
        print("Subject not found. Please add the subject first.")
        return
    topic_name= input("Enter the topic name to delete a task: ")
    if topic_name not in subjects[subject_name]:
        print("Topic not found. Please add the topic first.")
        return
    task_name= input("Enter the task name to delete: ")
    tasks=subjects[subject_name][topic_name]
    for task in tasks:
        if task["name"]==task_name:
            tasks.remove(task)
            print(f"Task '{task_name}' has been deleted successfully from topic '{topic_name}' in subject '{subject_name}'!")
            return
    print(f"Task '{task_name}' not found in topic '{topic_name}'.")
    
        
    
    
             
            
while True:
    display_menu()
    choice=input("Enter your choice :")
    
    if choice=="1":
        add_subject()
    elif choice=="2":
        view_subjects()
    elif choice=="3":
        add_topic()
    elif choice=="4":
        view_topics()
    elif choice=="5":
        add_task()  
    elif choice=="6":
        view_tasks()
    elif choice=="7":
        mark_task_completed()
    elif choice=="8":
        delete_subject()
    elif choice=="9":
        delete_topic()
    elif choice=="10":
        delete_task()
    elif choice=="11":
        print("Thank you for using the study assistant.")
        break
    else:
        print("Invalid choice. Please try again.")
    



