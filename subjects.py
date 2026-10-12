def add_subject(subjects):
    subject_name = input("Enter the subject name: ").strip()

    if subject_name == "":
        print("Subject name cannot be empty.")
        return

    existing_subject = find_subject_key(subjects, subject_name)

    if existing_subject is not None:
        print("Subject already exists.")
        return

    subjects[subject_name] = {}
    print(f"{subject_name} added successfully!")


def view_subjects(subjects):
    if not subjects:
        print("No subjects added yet.")
        return

    print("\nYour Subjects:")

    for index, subject in enumerate(subjects, start=1):
        print(f"{index}. {subject}")
        
def delete_subject(subjects):
    subject_name = input("Enter the subject name to delete: ").strip()

    subject_name = find_subject_key(subjects, subject_name)

    if subject_name is None:
        print("Subject not found. Please add the subject first.")
        return

    subjects.pop(subject_name)

    print(
        f"Subject '{subject_name}' and all its topics "
        f"and tasks have been deleted successfully!"
    )
    
def find_subject_key(subjects,subject_name):
    for subject in subjects:
        if subject_name.lower() == subject.lower():
            return subject
    
    return None
        
