from statistics import mean


students = {}

while True:
    print('1. Enter new student')
    print('2. Print all students')
    print('3. Find best student, mean GPA')
    print('4. Search student')
    print('5. Edit student')
    print('6. Delete student')

    choice = int(input('Your choice: '))
    if choice == 1:
        name = input('Enter student name: ')
        gpa = float(input('Enter student GPA: '))
        students[name] = gpa # check if name is already in students
    elif choice == 2:
        print(students)
    elif choice == 3:
        best_std = max(students, key=students.get)
        mean_gpa = sum(students.values()) / len(students)
        print('Mean GPA:', mean_gpa)
        print('Best student: {0}, GPA: {1}'.format(best_std, students[best_std]))
    elif choice == 4:
        name = input('Enter student name to search: ')
        print('Student: {0}, GPA: {1}'.format(name, students[name])) # should check if name is not in students
    elif choice == 5:
        name = input('Enter student name to edit: ')
        gpa = float(input('Enter student new GPA: '))
        students[name] = gpa
        print('Edit success')
    elif choice == 6:
        name = input('Enter student name to delete: ')
        students.pop(name)
        print('Delete success')
    elif choice == 0:
        print('Goodbye!')
        break
    else:
        print('Invalid choice!')



