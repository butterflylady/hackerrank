from datetime import datetime


def timeConversion(s):
    dt = datetime.strptime(s, "%I:%M:%S%p")
    ans = dt.strftime("%H:%M:%S")
    return ans


if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)
