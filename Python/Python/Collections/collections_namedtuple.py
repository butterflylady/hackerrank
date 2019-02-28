from collections import namedtuple

n = int(input())
columns = input().split()
Student = namedtuple('Student', columns)
tot_grade = 0
for i in range(n):
    stud = Student(*input().split())
    tot_grade += int(stud.MARKS)
print('{:.2f}'.format(tot_grade / n))
