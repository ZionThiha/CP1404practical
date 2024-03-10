FILENAME = "subject_data.txt"

def main():
    data = get_data()
    display_subject_details(data)
def get_data():
    """Read data from the file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_data = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subject_data.append(parts)
    input_file.close()
    return subject_data

def display_subject_details(data):
    """Display the subject details."""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()