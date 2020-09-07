from sys import stdin as s
def main():
    mile, juice = {}, {}
    num_m, num_j, value_m, value_j = 30, 60, 10, 15
    for i in range(1,2001):
        if i == num_m: num_m += 30; value_m += 10
        if i == num_j: num_j += 60; value_j += 15
        mile[i] = value_m; juice[i] = value_j
    cases = int(s.readline().strip())
    cont = 1
    for i in range(cases):
        cont_m, cont_j = 0, 0
        s.readline().strip()
        calls = list(map(int, s.readline().strip().split()))
        for call in calls:
            cont_m += mile[call]
            cont_j += juice[call]
        if cont_m > cont_j: print("Case {}: {}".format(cont, "Juice "+str(cont_j)))
        elif cont_j > cont_m: print("Case {}: {}".format(cont, "Mile "+str(cont_m)))
        else:print("Case {}: {}".format(cont, "Mile Juice "+str(cont_m)))
        cont += 1
main()