import sys
import io

input_data = """\
3
1 1 2 2
1 1 4 2
2 1 4 0
"""

sys.stdin = io.StringIO(input_data)

def solve():
    q = int(input())
    toll = {}
    total_answer = 0

    for _ in range(q):
        typ, x, y, t = map(int, input().split())

        def depth(u):
            return u.bit_length()
        dx, dy = depth(x), depth(y)

        while dx > dy:
            if typ == 1:
                toll[x] = toll.get(x, 0) + t
            else:
                total_answer += toll.get(x, 0)
            x //= 2
            dx -= 1

        while dy > dx:
            if typ == 1:
                toll[y] = toll.get(y, 0) + t
            else:
                total_answer += toll.get(y, 0)
            y //= 2
            dy -= 1

        while x != y:
            if typ == 1:
                toll[x] = toll.get(x, 0) + t
                toll[y] = toll.get(y, 0) + t
            else:
                total_answer += toll.get(x, 0)
                total_answer += toll.get(y, 0)
            x //= 2
            y //= 2

    return total_answer


if __name__ == "__main__":
    print(solve())