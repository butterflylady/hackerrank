def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    stu_score = 0
    kev_score = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kev_score += len(string) - i
        else:
            stu_score += len(string) - i
    if kev_score > stu_score:
        print("Kevin", kev_score)
    elif kev_score < stu_score:
        print("Stuart", stu_score)
    else:
        print("Draw")


s = input()
minion_game(s)
