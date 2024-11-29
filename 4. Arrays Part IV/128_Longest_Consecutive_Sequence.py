def longestConsecutiveSequence(arr):
    n = len(arr)
    if n == 0:
         return 0
    st = set()
    longest = 1
    #put all the array elements into set
    for i in range(n):
        st.add(arr[i])
    #Find the longest sequence
    for j in st:
        if j-1 not in st:
            cnt = 1
            x = j
            while x+1 in st:
                cnt += 1
                x +=1
            longest = max(cnt, longest)
    return longest

arr = [100, 200, 1, 2, 3, 4]
print(longestConsecutiveSequence(arr))