from collections import defaultdict

def the_kingdoms_rebellion(n, data):
    parent = [0] * (n + 1)
    respect = [0] * (n + 1)
    children = defaultdict(list)

    for i in range(1, n + 1):
        p, r = data[i - 1]
        parent[i] = p
        respect[i] = r
        if p != -1:
            children[p].append(i)

    result = []

    while True:
        found = False
        for i in range(1, n + 1):
            if parent[i] == -1 or respect[i] == 0:
                continue

            has_loyal_child = any(respect[child] == 0 for child in children[i])

            if not has_loyal_child:
                found = True
                result.append(i)

                for child in children[i]:
                    parent[child] = parent[i]
                    children[parent[i]].append(child)

                children[parent[i]].remove(i)
                children[i] = []
                parent[i] = -1
                break

        if not found:
            break

    return result if result else [-1]


n = 6
data = [
  (-1, 0),  # 1 (King)
  (1, 1),   # 2 (rebellious)
  (1, 1),   # 3 (rebellious)
  (3, 1),   # 4 (rebellious)
  (3, 0),   # 5 (loyal)
  (3, 0),   # 6 (loyal)
]
output = the_kingdoms_rebellion(n, data)
print(*output)