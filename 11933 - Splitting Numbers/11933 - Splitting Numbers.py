from sys import stdin as s
def main():
    num = int(s.readline().strip())
    while num:
        binary = format(num, "b")
        cont = 1
        a, b = "", ""
        for i in range(len(binary)-1, -1,-1):
            if binary[i] == "1":
                if cont % 2 != 0: a = "1" + a; b = "0" + b
                else: b = "1" + b; a = "0" + a
                cont += 1
            else: a = "0" + a; b = "0" + b
        print(int(a, 2), int(b, 2))
        num = int(s.readline().strip())
main()
