from sys import stdin as s

"""
    |_|_|_|      |_|_|_|     |_|x|x|
    |_|_|_|_|  = |_|_|_|x| + |_|_|x|x|
    |_|_|_|_|    |_|_|_|x|   |_|_|x|x| 
"""
def fracturedBoard(n):
    global second
    if n not in second:
        second[n] = fullBoard(n-1) + fracturedBoard(n-2)
    return second[n]

"""
    |_|_|_|_|    |_|_|x|x|   |_|_|x|x|   |_|_|_|x|
    |_|_|_|_|  = |_|_|x|x| + |_|_|_|x| + |_|_|_|x|
    |_|_|_|_|    |_|_|x|x|   |_|_|_|x|   |_|_|x|x|
"""
def fullBoard(n):
    global first
    if n not in first:
       first[n] =  fullBoard(n-2) + 2 * fracturedBoard(n-1)
    return first[n]

def main():
    global first, second
    first = {0 : 1, 1: 0}
    second = {0 : 0, 1 :1}
    n = int(s.readline().strip())
    while n != - 1:
        print(fullBoard(n))
        n = int(s.readline().strip())
main()