from sys import stdin as s
def binary_search(lis, number):
    bottom = 0
    top = long = len(lis)-1
    ans = ["X", "X"]
    while bottom <= top:
        middle = bottom +  (top-bottom)//2
        if lis[middle] > number:
            ans[1] = str(lis[middle])
            top = middle - 1
        elif lis[middle] < number:
            ans[0] = str(lis[middle])
            bottom = middle + 1
        else:
            if middle != 0:
                ans[0] = str(lis[middle-1])
            if middle != long:
                ans[1] = str(lis[middle+1])
            break
    return ans
def main():
    s.readline().strip() #Number of ladies
    ladies_heights = []
    last = None
    for elem in map(int, s.readline().strip().split()):
        if last != elem:
            last = elem
            ladies_heights.append(elem)
    s.readline().strip() #Number of Luchu's heights
    for heignt in list(map(int,s.readline().strip().split())):
        print(" ".join(binary_search(ladies_heights, heignt)))
main()