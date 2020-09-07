from sys import stdin as s


def main():
    dic = {0:"",1:"1\n"}
    for i in range(2,10):dic[i] = dic[i-1] + str(i)*i + "\n"
    cases = int(s.readline().strip())
    while cases:
        input()
        amplitude = int(s.readline().strip());frequency = int(s.readline().strip())
        if amplitude == 0: res = "\n" * (frequency - 2)
        else: res = ((dic[amplitude].strip() + dic[amplitude-1][::-1] + "\n\n" ) * frequency).strip()
        print(res + "\n") if cases > 1 else print(res)
        cases -=1
main()

