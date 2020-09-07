from sys import stdin as s
def main():
    dic = {0:[0,1],1:[2]}
    n = 2
    while n <= 14:
        dic[n] = [dic[n-2][-1]+dic[n-1][0],2*dic[n-1][-1]]
        n+=1
    ways = [0 for i in range(10002)]
    ways[2],i,n = 1,3,2
    while i!= 10001:
        if i <= dic[n][-1]:ways[i] = n
        else:n+=1;ways[i] = n
        i+=1
    num = int(s.readline().strip())
    cont = 1
    res = ""
    while num > -1:
        res+="Case {}: {}\n".format(cont,ways[num])
        cont+=1
        num = int(s.readline().strip())
    print(res.strip())
main()
