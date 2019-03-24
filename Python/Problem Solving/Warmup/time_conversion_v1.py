def timeConversion(s):
    timeList = s.split(":")
    if timeList[2][-2:] == "PM" and int(timeList[0]) != 12:
        return str(int(timeList[0]) + 12) + ":" + timeList[1] + ":" + timeList[2][0:2]
    elif timeList[2][-2:] == "AM" and int(timeList[0]) == 12:
        return "00" + ":" + timeList[1] + ":" + timeList[2][0:2]
    else:
        return timeList[0] + ":" + timeList[1] + ":" + timeList[2][0:2]


if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)
