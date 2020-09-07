from sys import stdin
from time import time
def dp():
    """Se utiliza dinamica bottom-up para calcular todas las maneras hasta 30000
    La funcion retorna la lista de maneras de obtener el cambio hasta 30000"""
    global lis
    ways = [1 for i in range(30001)]
    for i in range(4):
        for k in range(30001):
            if k >= lis[i]:
                ways[k] += ways[k-lis[i]]
    return ways

def main():
    cases = stdin.readlines()
    global dic,lis
    #dic = {}
    lis = [5,10,25,50]
    ti = time()
    ways = dp()
    tf = time()
    print("EXECUTION TIME: ",tf-ti)
    for i in range(len(cases)):
        case = int(cases[i].strip())
        if ways[case] == 1:
            print("There is only 1 way to produce {} cents change.".format(case))
        else:
            print("There are {} ways to produce {} cents change.".format(ways[case],case))
main()
