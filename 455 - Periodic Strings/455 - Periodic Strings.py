from sys import stdin as s


def main():
    cases = int(s.readline().strip())
    while cases:
        input()
        cont = 1
        string = s.readline().strip()
        period = string[0]
        i = 1
        while i < len(string):
            if period != string[i:i + len(period)]:
                period = period * cont + string[i]
                if len(period) > len(string) - i:
                    period = string
                    break
                cont = 1
                i += 1
            else:
                cont += 1
                i += len(period)
        print(len(period))
        if cases != 1:
            print("")
        cases -= 1


main()
