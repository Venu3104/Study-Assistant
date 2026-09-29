subjects=[]


def display_menu():
    print("\n===============================")
    print("           STUDY ASSISTANT       ")
    print("===============================")
    print("1. Add Subject")
    print("2. View Subjects")
    print("3. Exit")
    
    
def add_subject():
    subject_name=input("Enter the subject name: ")
    subjects.append(subject_name)
    print(f"{subject_name} added successfully")
    
def view_subjects():
    if not subjects:
        print("No subjects added yet.")
    else:
        print("\n Your Subjects:")
        for index, subject in enumerate(subjects,start=1):
            print(f"{index}. {subject}") 
            
            
while True:
    display_menu()
    choice=input("Enter your choice :")
    
    if choice=="1":
        add_subject()
    elif choice=="2":
        view_subjects()
    elif choice=="3":
        print("Thank you for using the study assistant.")
        break
    else:
        print("Invalid choice. Please try again.")
    



