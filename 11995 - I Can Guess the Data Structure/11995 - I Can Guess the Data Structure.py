from sys import stdin as s
from collections import deque 
import heapq

def main():
    case = s.readline().strip()
    while case:
        lista, cola, prioridad = [], deque(), []
        out, outLista, outCola, outPrioridad = [], [], [], []
        for i in range(int(case)):
            heapq.heapify(prioridad)
            instruction = list(map(int, s.readline().strip().split()))
            if instruction[0] == 1:
                lista.append(instruction[1])
                cola.append(instruction[1])
                heapq.heappush(prioridad, -1 * instruction[1])
            else:
                out.append(instruction[1])
                try:
                    outLista.append(lista.pop())
                    outCola.append(cola.popleft())
                    outPrioridad.append(-1 * heapq.heappop(prioridad))
                except:
                    res = "impossible"
        res = "impossible"
        if out == outLista:
            res = "stack"
        if out == outCola:
            res = "not sure" if res != "impossible" else "queue"
        if out == outPrioridad:
            res = "not sure" if res != "impossible" else "priority queue"
        print(res)
        case = s.readline().strip()
main()