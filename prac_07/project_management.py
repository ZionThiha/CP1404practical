# project_management.py

from project import Project
import csv
import datetime

def load_projects(filename):
    projects = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            project = Project(row['Name'], row['Start Date'], row['Priority'], row['Cost Estimate'], row['Completion Percentage'])
            projects.append(project)
    return projects

def save_projects(filename, projects):
    with open(filename, 'w', newline='') as file:
        fieldnames = ['Name', 'Start Date', 'Priority', 'Cost Estimate', 'Completion Percentage']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        for project in projects:
            writer.writerow({'Name': project.name,
                             'Start Date': project.start_date.strftime('%d/%m/%Y'),
                             'Priority': project.priority,
                             'Cost Estimate': project.cost_estimate,
                             'Completion Percentage': project.completion_percentage})

# Implement additional functions like display_projects, filter_projects_by_date, add_new_project, update_project

# Assuming you have imported necessary modules and defined the Project class and other functions

def display_projects(projects):
    # Sort projects by priority before displaying
    projects.sort()
    print("Incomplete projects:")
    for project in [p for p in projects if not p.is_complete()]:
        print(project)
    print("\nCompleted projects:")
    for project in [p for p in projects if p.is_complete()]:
        print(project)


def filter_projects_by_date(projects, date):
    filtered_projects = [p for p in projects if p.start_date > date]
    print(f"Projects starting after {date.strftime('%d/%m/%Y')}:")
    for project in filtered_projects:
        print(project)


def add_new_project(projects):
    # Add your implementation for adding a new project
    pass


def update_project(projects):
    # Add your implementation for updating a project
    pass


def main_menu(projects):
    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        choice = input("Choose an option: ").upper()

        if choice == 'L':
            filename = input("Enter filename to load from: ")
            projects = load_projects(filename)
            print(f"Loaded projects from {filename}")
        elif choice == 'S':
            filename = input("Enter filename to save to: ")
            save_projects(filename, projects)
            print(f"Saved projects to {filename}")
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            date_input = input("Enter date (dd/mm/yyyy) to filter projects after: ")
            date = datetime.datetime.strptime(date_input, "%d/%m/%Y").date()
            filter_projects_by_date(projects, date)
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            update_project(projects)
        elif choice == 'Q':
            if input("Save changes to projects.txt? (y/n): ").lower() == 'y':
                save_projects('projects.txt', projects)
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


def main():
    projects = load_projects('projects.txt')
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from projects.txt")
    main_menu(projects)


main()