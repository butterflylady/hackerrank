student_score = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    student_score.append([name, score])
score_set = set([lst[1] for lst in student_score])
second_min_val = sorted(list(score_set))[1]
second_stud_val = [lst for lst in student_score if lst[1] == second_min_val]
second_stud_val.sort(key=lambda x: x[0])
print("\n".join([x[0] for x in second_stud_val]))
