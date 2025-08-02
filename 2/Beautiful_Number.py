from typing import List

def solve(N: int, A:  List[int]) -> int:
    result  = 0
    for i in range(N):
        xor = 0
        for j in range(A[i] + 1):
            xor ^= j
        if xor == 1:
            result += 1

    return result

if __name__ == "__main__":
    N = 3
    A = [1, 2, 3]
    print(solve(N, A))