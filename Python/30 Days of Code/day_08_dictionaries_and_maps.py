n = int(input())

name_number = [input().split() for _ in range(n)]
phone_book = {k: v for k, v in name_number}
while True:
    name = input().strip()
    try:
        if not name:
            raise ValueError
        else:
            if name in phone_book:
                print('%s=%s' % (name, phone_book[name]))
            else:
                print('Not found')
    except ValueError:
        break
