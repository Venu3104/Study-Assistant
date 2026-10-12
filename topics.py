from subjects import find_subject_key

def add_topic(subjects):
    subject_name = input("Enter the subject name to add a topic: ").strip()

    subject_name=find_subject_key(subjects,subject_name)
    
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


def view_topics(subjects):
    subject_name = input("Enter the subject name to view topics: ").strip()

    subject_name=find_subject_key(subjects,subject_name)

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
        

def delete_topic(subjects):
    subject_name = input("Enter the subject name to delete a topic: ").strip()

    subject_name = find_subject_key(subjects, subject_name)

    if subject_name is None:
        print("Subject not found. Please add the subject first.")
        return

    topic_name = input("Enter the topic name to delete: ").strip()
    
    if topic_name == "":
        print("Topic name cannot be empty.")
        return
    topic_name = find_topic_key(subjects, subject_name, topic_name)

    if topic_name is None:
        print("Topic not found. Please add the topic first.")
        return

    subjects[subject_name].pop(topic_name)

    print(
        f"Topic '{topic_name}' and all its tasks have been "
        f"deleted successfully from subject '{subject_name}'!"
    )

def find_topic_key(subjects, subject_name, topic_name):
    for topic in subjects[subject_name]:
        if topic_name.lower() == topic.lower():
            return topic

    return None