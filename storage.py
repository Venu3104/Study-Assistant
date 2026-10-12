import json

def save_data(subjects):
    with open("subjects.json", "w") as file:
        json.dump(subjects, file, indent=4)

    print("Data saved to subjects.json.")


def load_data():
    try:
        with open("subjects.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {}
