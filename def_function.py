# I'm creating a small program that helps us store and grade their subjects..
student_name = input("Enter your name: ")

print(f"Hello, {student_name}!") # To see the user name!

subjects = {} # To store the subjects and marks
total_user_marks = 0

def subject_grades():
    while True:
        subject  = input('Enter subject names and then type exit to finish your input: ')
        if subject.lower() == 'exit':
            break
        else:
            grade = int(input(f'enter your grade for {subject}: '))
            subjects[subject] = grade
    return subjects

def get_details(lavdas):
    global total_user_marks
    for i, j in lavdas.items():
        print(f'{i} : {j}')
        total_user_marks += int(j)
    print(f'Your total marks: {total_user_marks}')

def get_grades(grades):
    for i, j in grades.items():
        if j >= 90:
            print(f'{i}: A+')
        elif 70 < j < 90:
            print(f'{i}:A')
        else:
            print("Fail")

subjects_grades = subject_grades()
users_marks_sheet = get_details(subjects_grades)
get_user_grades = get_grades(subjects_grades)


    

    
