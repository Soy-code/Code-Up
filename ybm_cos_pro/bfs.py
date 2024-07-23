def solution(maps):
    n = len(maps)
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    h = [ -1, -1, 0, 1, 1, 1, 0, -1 ]
    v = [ 0, 1, 1, 1, 0, -1, -1, -1 ]
    q = []
    visited[0][0] = 0
    q.append([0,0])
    while len(q) > 0:
        temp = q[0]
        q.pop(0)
        cur_x = temp[0]
        cur_y = temp[1]
        cur_dist = visited[cur_x][cur_y]
        if cur_x == n - 1 and cur_y == n - 1:
            return cur_dist
        for i in range(8):
            nx = cur_x + h[i]
            ny = cur_y + v[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n and maps[nx][ny] < maps[cur_x][cur_y] and visited[nx][ny] == -1:
                q.append([nx, ny])
                visited[nx][ny] = cur_dist + 1
    return -1

print(solution([[10, 11, 8, 4, 2], [9, 8, 7, 6, 7], [9, 7, 6, 5, 4], [3, 8, 9, 2, 3], [5, 2, 7, 5, 1]]))