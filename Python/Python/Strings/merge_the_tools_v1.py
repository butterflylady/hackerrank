from collections import OrderedDict

def merge_the_tools(string, k):
    for x in range(0,len(string),k):
        print(''.join(list(OrderedDict.fromkeys(string[x:x+k]))))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)