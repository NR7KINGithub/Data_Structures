def max_power(X, Y):
    dp0 = dpX = dpY = 0
    for x, y in zip(reversed(X), reversed(Y)):
        new_dp0 = max(x + dpX,    y + dpY)
        new_dpX = max(x + dpX,        dpY)
        new_dpY = max(y + dpY,        dpX)
        dp0, dpX, dpY = new_dp0, new_dpX, new_dpY

    return dp0

if __name__ == "__main__":
    X = [4, 1, 1]
    Y = [1, 1, 3]
    print(max_power(X, Y))