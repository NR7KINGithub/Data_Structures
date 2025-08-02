def nearestMeetingCell(n, edges, c1, c2):
    def get_distance(start):
        dist = [-1] * n
        visited = [False] * n
        node = start
        distance = 0

        while node != -1 and not visited[node]:
            dist[node] = distance
            visited[node] = True
            node = edges[node]
            distance += 1

        return dist
    
    dist1 = get_distance(c1)
    dist2 = get_distance(c2)

    min_dist = float('inf')
    meeting_cell = -1

    for i in range(n):
        if dist1[i] != -1 and dist2[i] != -1:
            max_dist = max(dist1[i], dist2[i])

            if max_dist < min_dist:
                min_dist = max_dist
                meeting_cell = i

    return meeting_cell

n = 23
edges = [4, 1, 4, 1, 3, 8, 8, 8, 0, 8, 14, 9, 15, 11, -1, 10, 15, 22, 22, 22, 22, 22, 21]
c1 = 9
c2 = 2
print(nearestMeetingCell(n, edges, c1, c2))