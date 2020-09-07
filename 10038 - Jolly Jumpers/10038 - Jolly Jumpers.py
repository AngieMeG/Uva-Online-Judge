from sys import stdin as s


def main():
    input = s.readline().strip().split()
    while input:
        dic = {}
        cont = int(input[0])-1
        for i in range(1, len(input)-1):
            temp = abs(int(input[i]) - int(input[i+1]))
            if temp not in dic and 1 <= temp <= int(input[0]) - 1:
                dic[temp] = True; cont -= 1
        print("Jolly") if not cont else print("Not jolly")
        input = s.readline().strip().split()


main()
