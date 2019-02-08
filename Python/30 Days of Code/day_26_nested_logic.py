returned_date = list(map(int, input().strip().split()))
expected_date = list(map(int, input().strip().split()))

fine = 0

if returned_date[2] > expected_date[2]:
    fine = 10000
elif returned_date[2] == expected_date[2]:
    if returned_date[1] > expected_date[1]:
        fine = 500 * (returned_date[1] - expected_date[1])
    elif returned_date[1] == expected_date[1]:
        if returned_date[0] > expected_date[0]:
            fine = 15 * (returned_date[0] - expected_date[0])
print(fine)
