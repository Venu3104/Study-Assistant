def view_study_progress(subjects):
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
    

def view_subject_progress(subjects):
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

  