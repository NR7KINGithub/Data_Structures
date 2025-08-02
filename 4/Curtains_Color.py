def colors(s: str, l: int) -> int:
    count = 0
    maxi = 0
    for i in range(len(s)):
        if (i % l == 0):
            maxi = max(count, maxi)
            count = 0

        if (s[i] == "a"):
            count += 1

    if count > maxi:
        maxi = count
    return maxi

if __name__ == "__main__":
    s = "bbbaaababa"
    l = 3
    print(colors(s, l))