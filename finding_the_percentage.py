#Problem link : https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true

def find_average(value):
    sm = 0
    for i in value:
        sm += i
    return sm/(len(value))

n = int(input())
student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

for key,value in student_marks.items():
    if key == query_name:
        average_score = find_average(value)
        print(f"{average_score:.2f}")
        break
    else:
        continue
