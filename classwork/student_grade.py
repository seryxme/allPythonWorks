grade = int(input("Enter student's grade: "))

if grade >= 70:
    print("A")
if 60 <= grade <= 69:
    print("B")
if 50 <= grade <= 59:
    print("C")
if 45 <= grade <= 49:
    print("B")
if 40 <= grade <= 44:
    print("E")
if grade < 40:
    print("F")