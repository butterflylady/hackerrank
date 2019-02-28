from datetime import datetime as dt


def time_delta(t1, t2):
    format = "%a %d %b %Y %H:%M:%S %z"
    delta_sec = int(abs((dt.strptime(t1, format) - dt.strptime(t2, format)).total_seconds()))
    return str(delta_sec)


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(delta)
