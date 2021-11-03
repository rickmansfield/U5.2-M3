# print(help(map))
def csIsomorphicStrings(a, b):
    maxCharCapacity = 128
    lenA = len(a)
    lenB = len(b)
    if lenA != lenB:
        return False
    tagged = [False] * maxCharCapacity
    myMap = [-1] * maxCharCapacity
    for i in range(lenB):
        if myMap[ord(a[i])] == -1:
            if tagged[ord(b[i])] == True:
                return False
            tagged[ord(b[i])] = True
            myMap[ord(a[i])] = b[i]
        if myMap[ord(a[i])] !=b[i]:
            return False
    return True

print(csIsomorphicStrings("odd", "egg"))
print(csIsomorphicStrings("foo", "bar"))
print(csIsomorphicStrings("abca", "zbxz"))
print(csIsomorphicStrings("abc", ""))
print(csIsomorphicStrings("$%#", "112"))