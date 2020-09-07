def americus(num,lis,value):
    if num == 0:
        return value
    else:
        if num >= lis[0][1] and len(lis)!= 1:
            num -= lis[0][1]
            value += lis[0][0]*lis[0][1]
            return americus(num,lis[1::],value)
        elif num <= lis[0][1] or (num >= lis[0][1] and len(lis)==1):
            value += num * lis[0][0]
            num = 0
            return americus(num,lis[1::],value)
def CWH(num):
    if num <= 200: return num//2
    elif num <= 29900: return 100 + ((num-200)//3)
    elif num <= 4979900: return 10000 + ((num-29900)//5)
    else: return 1000000 + ((num-4979900)//7)

def binary_search(price,low,high,total):
    lis = [[2, 100], [3, 9900], [5, 990000], [7, 0]]
    if low <= high:
        middle = (low+high)//2
        bill_a, bill_b = americus((total-middle),lis,0),americus(middle,lis,0)
        test = bill_a-bill_b
        if test == price:
            return min(bill_a,bill_b)
        elif test < price:
            high = middle
            return binary_search(price,low,high,total)
        elif test > price:
            low = middle
            return binary_search(price,low,high,total)
def main():
    en = [int(i) for i in input().split()]
    while en[0] != 0 and en[1] != 0:
        price = CWH(en[0])
        print(binary_search(en[1],0,price,price))
        en = [int(i) for i in input().split()]
main()