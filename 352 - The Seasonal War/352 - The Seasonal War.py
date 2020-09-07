from sys import stdin as s
x_pos = [-1,0,0,1,-1,1,-1,1]
y_pos = [0,-1,1,0,1,1,-1,-1]
def DFS(i,k):
    global image, visited
    aux = [(i, k)]
    dimension = len(image)
    while len(aux) != 0:
        node = aux.pop()
        for i in range(len(x_pos)):
            temp_x, temp_y = node[0] + x_pos[i], node[1] + y_pos[i]
            if 0 <= temp_x < dimension and 0 <= temp_y < dimension:
                if image[temp_x][temp_y] == "1" and visited[temp_x][temp_y] == False:
                    aux += [(temp_x, temp_y)]
            visited[node[0]][node[1]] = True
    return

def main():
    global image, visited
    dimension = s.readline().strip()
    image_count = 0
    while dimension:
        image_count += 1
        dimension = int(dimension)
        image, visited = [],[]
        for i in range(dimension):
            image += [list(s.readline().strip())]
            visited += [[False for i in range(dimension)]]
        eagle_count = 0
        for i in range(dimension):
            for k in range(dimension):
                if image[i][k] == "1" and visited[i][k] == False: eagle_count += 1; DFS(i,k)
        print("Image number %d contains %d war eagles." % (image_count,eagle_count))
        dimension = s.readline().strip()
main()