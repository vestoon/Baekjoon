credit_sum = 0
grade_sum = 0

for x in range(20):
    subject, credit, grade = input().split()
    credit = float(credit)
    if grade == 'P':
        continue

    credit_sum += credit
    if grade == "A+":
        grade_sum += 4.5*credit
    elif grade == "A0":
        grade_sum += 4.0*credit
    elif grade == "B+":
        grade_sum += 3.5*credit
    elif grade == "B0":
        grade_sum += 3.0*credit
    elif grade == "C+":
        grade_sum += 2.5*credit
    elif grade == "C0":
        grade_sum += 2.0*credit
    elif grade == "D+":
        grade_sum += 1.5*credit
    elif grade == "D0":
        grade_sum += 1.0*credit

print(grade_sum/credit_sum)
