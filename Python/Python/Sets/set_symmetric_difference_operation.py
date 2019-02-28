n = int(input())
eng = set(map(int, input().split()))
m = int(input())
fr = set(map(int, input().split()))
eng_or_fr = eng.symmetric_difference(fr)  # eng^fr
print(len(eng_or_fr))
