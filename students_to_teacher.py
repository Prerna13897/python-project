lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
students = [lloyd, alice, tyler]


# Add your function below!
def average(numbers):
    total = float(sum(numbers))
    avg = (total / len(numbers))
    return avg


def get_average(student):
    homework = float(average(student["homework"]))
    quizzes = float(average(student["quizzes"]))
    tests = float(average(student["tests"]))
    weighted_average = (homework * 0.1) + (quizzes * 0.3) + (tests * 0.6)
    return weighted_average


def get_letter_grade(score):
    if score >= 90:
        print "A"
        return "A"
    elif score >= 80:
        print "B"
        return "B"
    elif score >= 70:
        print "C"
        return "C"
    elif score >= 60:
        print "D"
        return "D"
    else:
        print "F"
        return "F"


print get_letter_grade(get_average(lloyd))


def get_class_average(students):
    results = []
    for student in students:
        get_average(student)
        results.append(get_average(student))
    return average(results)


print get_class_average(students)
print get_letter_grade(average)