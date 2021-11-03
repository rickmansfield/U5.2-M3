def csIsomorphicStrings(a, b):
    max_chars = 256
    m = len(a)
    n = len(b)
    if m != n :
        return False
    marked = [False] * max_chars
    map = [-1] * max_chars
    for i in range(n):
        if map[ord(a[i])] == -1:
            if marked[ord(b[i])] == True:
                return False
            marked[ord(b[i])] = True
            map[ord(a[i])] = b[i]
            
        elif map[ord(a[i])] != b[i]:
            return False
            
    return True