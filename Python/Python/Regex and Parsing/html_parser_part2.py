from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        number_of_lines = len(data.split("\n"))
        if number_of_lines > 1:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        if data.strip():
            print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)


n = int(input())
parser = MyHTMLParser()

parser.feed('\n'.join([input().strip() for _ in range(n)]))
parser.close()
