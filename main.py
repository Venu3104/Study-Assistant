from datetime import datetime, date
from progress import view_study_progress,view_subject_progress
from storage import save_data,load_data
from subjects import(add_subject,view_subjects,delete_subject,find_subject_key)
from topics import(add_topic,view_topics,delete_topic,find_topic_key)
from tasks import(add_task,view_tasks,mark_task_completed,view_deadline_tasks,delete_task,edit_task)
from search import filter_tasks_by_status, search_and_filter_menu

subjects = load_data()


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
    print("13. View Overdue/Upcoming Tasks")
    print("14. Search Tasks by Name")
    print("15. Edit Task")
    print("16. Exit")  


while True:
    display_menu()

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_subject(subjects)

    elif choice == "2":
        view_subjects(subjects)

    elif choice == "3":
        add_topic(subjects)

    elif choice == "4":
        view_topics(subjects)

    elif choice == "5":
        add_task(subjects)

    elif choice == "6":
        view_tasks(subjects)

    elif choice == "7":
        mark_task_completed(subjects)

    elif choice == "8":
        delete_subject(subjects)

    elif choice == "9":
        delete_topic(subjects)

    elif choice == "10":
        delete_task(subjects)
        
    elif choice == "11":
        view_study_progress(subjects)
        
    elif choice == "12":
        view_subject_progress(subjects)
        
    elif choice == "13":
        view_deadline_tasks(subjects)

    elif choice == "14":
        search_and_filter_menu(subjects)    

    elif choice == "15":
        edit_task(subjects)
        save_data(subjects)

    elif choice == "16":
        save_data(subjects)
        print("Thank you for using the study assistant.")
        break

    else:
        print("Invalid choice. Please try again.")

