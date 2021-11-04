import builtins
# print(help(dict))
# print(help(dict.values))
print(help(range))

def csWordPattern(pattern, a):
    convertStrToWords = a.split(" ")
    # print("Words Split Up", convertStrToWords)
    
    if not len(convertStrToWords) == len(pattern):
        return False
    mappedDict = dict()
    # print("Mapped Dictionary:", mappedDict)
    
    for eachChar in range(len(convertStrToWords)):
        if pattern[eachChar] not in mappedDict:
            if convertStrToWords[eachChar] not in mappedDict.values():
                # print("mappedDict Values", mappedDict.values())
                mappedDict[pattern[eachChar]] = convertStrToWords[eachChar]
            else:
                return False
        else:
            if not mappedDict[pattern[eachChar]] == convertStrToWords[eachChar]:
                return False
    return True

print(csWordPattern("abba", "lambda school school lambda"))
print(csWordPattern("abba", "lambda school school coding"))
print(csWordPattern("aaaa", "lambda school school lambda"))
print(csWordPattern("abba", "lambda lambda lambda lambda"))