maths = 89
science = 92
english = 85
computers = 90
social_studies = 88

def total_marks(maths, science, english, computers, social_studies):
    total = maths + science + english + computers + social_studies
    print("Total marks: ", total)
    return total

def average_marks(total, number_of_subjects):
    average = total/number_of_subjects
    print("Average marks: ", average)
    return average

def grade(average):
    
    if average >= 90:
        print("A")
        return "A"
    elif average >= 80:
        print("B")
        return "B"
    elif average >= 70:
        print("C")
        return "C"
    elif average >= 60:
        print("D")
        return "D"      
    else:
        print("F")
        return "F"

def pass_fail(average):
    if average >= 40:
        print("Pass")
        return "Pass"
    else:
        print("Fail")
        return "Fail"
    

total = total_marks(maths, science, english, computers, social_studies)
average = average_marks(total, 5)   
grade_marks = grade(average)
pass_fail_decision = pass_fail(average)