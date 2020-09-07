from sys import stdin as s


def main():
    flag = True
    string = list(s.readline().strip())
    while string:
        string = list(string)
        for i in range(len(string)):
            if string[i] == '"':
                string[i] = '``' if flag else "''"
                flag = not flag
        print("".join(string))
        string = list(s.readline().strip())


main()
