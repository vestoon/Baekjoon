import sys
n, m = map(int, sys.stdin.readline().split())
subjects = ('kor', 'eng', 'math', '-')
fruits = ('apple', 'pear', 'orange', '-')
colors = ('red', 'blue', 'green', '-')
questions = []
for s in subjects:
    for f in fruits:
        for c in colors:
            questions.append(s+' '+f+' '+c)
cases = {question: 0 for question in questions}
for person in range(n):
    sub, fruit, color = sys.stdin.readline().split()
    for s in (sub, '-'):
        for f in (fruit, '-'):
            for c in (color, '-'):
                prefer = s+' '+f+' '+c
                cases[prefer] += 1

for question in range(m):
    queary = sys.stdin.readline().rstrip()
    print(cases[queary])
