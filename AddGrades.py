student_list = []

def create_student():
    name = input('Please enter student name: ')
    student_data = {
        'name': name,
        'marks': []
    }
    return student_data


def add_mark(student, mark):
    student['marks'].append(mark)



def calculate_average_mark(student):
    number = len(student['marks'])
    if number == 0:
        return 0

    total = sum(student['marks'])
    return "{}".format(total/number)


def print_student_details(student):
    print('{} - average mark: {}'.format(student['name'],calculate_average_mark(student)))


def print_students(students):
    for i, student in enumerate(students):
        print('ID: {}'.format(i))
        print_student_details(student)


def menu():
    selection = input("Enter 'p' to print student list, "
                      "'s' to add a new student, "
                      "'a' to add a mark "
                      "or 'q' to exit: ")
    while selection != 'q':
        if selection == 'p':
            print_students(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = int(input('Enter student ID to add a mark to: '))
            student = student_list[student_id]
            new_mark = int(input('Enter new mark to be added: '))
            add_mark(student, new_mark)
        selection = input("Enter 'p' to print student list, "
                          "'s' to add a new student, "
                          "'a' to add a mark or 'q' to exit: ")

menu()

