subjects={}


def display_menu():
    print("\n===============================")
    print("           STUDY ASSISTANT       ")
    print("===============================")
    print("1. Add Subject")
    print("2. View Subjects")
    print("3. Add Topic")
    print("4. View Topics")
    print("5. Exit")
    
    
def add_subject():
    subject_name=input("Enter the subject name: ")
    
    if subject_name in subjects:
        print("subject already exists.")
        return
    
    subjects[subject_name] = []
    
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
    
    subjects[subject_name].append(topic_name)
    
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
        print("Thank you for using the study assistant.")
        break
    else:
        print("Invalid choice. Please try again.")
    



