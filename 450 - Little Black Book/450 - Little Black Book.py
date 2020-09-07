from sys import stdin as s
def main():
    cases = int(s.readline().strip())
    res = []
    guion = "-" * 40
    for i in range(cases):
        dep = s.readline().strip()
        while True:
            var = s.readline().strip().split(",")
            if var == ['']:break
            res.append([var[2],var[1],var[0],var[3],dep,var[4],var[5],var[6]])
    res.sort()
    for keys in res:
        print(guion);print(keys[2],keys[1],keys[0]);print(keys[3])
        print("Department:",keys[4]);print("Home Phone:",keys[5]);print("Work Phone:",keys[6])
        print("Campus Box:",keys[7])
main()