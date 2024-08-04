students_grades = [("John", 85), ("Jane", 90), ("Doe", 88)]
sorted_students = sorted(students_grades, key=lambda item: item[1], reverse=True)
print(sorted_students)