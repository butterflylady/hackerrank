class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        mean = sum(self.scores) / len(self.scores)
        char = ""
        if mean >= 90:
            char = "O"
        elif mean >= 80:
            char = "E"
        elif mean >= 70:
            char = "A"
        elif mean >= 55:
            char = "P"
        elif mean >= 40:
            char = "D"
        else:
            char = "T"
        return char


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
