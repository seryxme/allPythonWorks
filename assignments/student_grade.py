

num_of_students = int(input("How many students do you have?: "))
num_of_subjects = int(input("How many subjects do they offer?: "))

students = []
subjects = []
student_scores = []
student_grades = []

for i in range(num_of_students):
   students.append(input(f"Enter student{i+1} name: "))

for i in range(num_of_subjects):
    subjects.append(input(f"Enter subject{i+1} name: "))

for i in range(num_of_students):
    for j in range(num_of_subjects):
        student_scores.append(int(input(f"Enter {students[i]} scores in {subjects[j]}: ")))
    student_grades.append(student_scores.copy())
    student_scores.clear()

total = []
position = []
for i in range(len(student_grades)):
    total.append(sum(student_grades[i]))

temp = total.copy()
temp.sort(reverse=True)
for i in range(len(total)):
    for j in range(len(temp)):
        if total[i] == temp[j]:
            position.append(j + 1)


print("--------------------------------------------------------------------------------")
print(f"{'STUDENT NAME':^30s}", end="")
for i in range(num_of_subjects):
    print(f"{subjects[i].upper():<10s}", end="")
print(f"{'TOTAL':^7s}{'AVG':^7s}{'POS':^5s}")
print("--------------------------------------------------------------------------------")

for i in range(num_of_students):
    print(f"{i+1:>2d}. {students[i]:<26s}", end="")
    for j in range(num_of_subjects):
        print(f"{student_grades[i][j]:<10d}", end="")
    print(f"{total[i]:^7d}{total[i] / num_of_subjects:^7.2f}{position[i]:^5d}")