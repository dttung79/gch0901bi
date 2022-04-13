from statistics import mean

students = {}

def print_menu():
    print('1. Enter new student')
    print('2. Print all students')
    print('3. Find best student, mean GPA')
    print('4. Search student')
    print('5. Edit student')
    print('6. Delete student')


def enter_student():
    name = input('Enter student name: ')
    gpa = float(input('Enter student GPA: '))
    if name in students:
        print('Student already exists') 
    else:
        students[name] = gpa
        print('Student added')

def print_students():
    for name, gpa in students.items():
        print('Student name: ', name)
        print('GPA: ', gpa)

def find_best_students():
    best_std = max(students, key=students.get)
    mean_gpa = sum(students.values()) / len(students)
    print('Mean GPA:', mean_gpa)
    print('Best student: {0}, GPA: {1}'.format(best_std, students[best_std]))

def search_students():
    name = input('Enter student name to search: ')
    if name in students:
        print('Student: {0}, GPA: {1}'.format(name, students[name])) 
    else:
        print('Student not found')

def edit_students():
    name = input('Enter student name to edit: ')
    if name in students:
        gpa = float(input('Enter new GPA: '))
        students[name] = gpa
        print('Student edited')
    else:
        print('Student not found')

def delete_students():
    name = input('Enter student name to delete: ')
    if name in students:
        del students[name]
        print('Student deleted')
    else:
        print('Student not found')
        
while True:
    print_menu()
    choice = int(input('Your choice: '))
    if choice == 1:
        enter_student()
    elif choice == 2:
        print_students()
    elif choice == 3:
        find_best_students()
    elif choice == 4:
        search_students()
    elif choice == 5:
        edit_students()
    elif choice == 6:
        delete_students()
    elif choice == 0:
        print('Goodbye!')
        break
    else:
        print('Invalid choice!')



