import re

if __name__ == '__main__':
    N = int(input())
    nameList = []
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if re.search(r'([a-z]+)(@gmail.com)$', emailID):
            nameList.append(firstName)
    sortedNameList = sorted(nameList)
    for name in sortedNameList:
        print(name)
