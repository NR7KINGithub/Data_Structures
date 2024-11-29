def myPow(x: float, n: int) -> float:
    ans = 1.0
    nn = n
    if nn < 0:
        nn = -1*nn
    while nn:
        if nn % 2:
            ans = ans*x
            nn = nn-1
        else:
            x = x*x
            nn = nn//2
    if n < 0:
        ans = 1.0/ans
    return ans
    
if __name__ == "__main__":
    print(myPow(2, -1))