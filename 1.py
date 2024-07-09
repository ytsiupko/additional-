import csv

with open('students.txt', 'r') as file:
    rows = file.readlines()

    students = {}

    for row in rows:
        name, score = row.strip().split()
        score = float(score)
        students[name] = score
        print(students)

    total_score = sum(students.values())
    average_score = total_score / len(students)

    print(f"The average score of the students is: {average_score:}")

with open('results.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'score'])
    writer.writerows(students.items())
    writer.writerow(['average score', average_score])