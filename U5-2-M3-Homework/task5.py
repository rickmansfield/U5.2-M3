import builtins
# print(help(dict))
    # new dictionary initialized from a mapping object's (key, value) pairs
# print(help(tuple))
    #  If no argument is given, the constructor returns an empty tuple.
    #  If iterable is specified the tuple is initialized from iterable's items.
# print(help(sorted)) 
    # returns new sorted list
# print(help(list))
    # If no argument is given, the constructor creates a new empty list.
    # The argument must be an iterable if specified.
# print(help(dict.values))
    #  an object providing a view on D's values


def csGroupAnagrams(strs):
    ricksDiclol = dict()
    for eachWord in strs: 
        itsKey = tuple(sorted(eachWord))
        # print("its Key", itsKey)
        ricksDiclol[itsKey] = ricksDiclol.get(itsKey, []) + [eachWord]
        # print(ricksDiclol[itsKey])
    return list(ricksDiclol.values())
        

print(csGroupAnagrams(["apt","pat","ear","tap","are","arm"])) # [["apt","pat","tap"],["ear","are"],["arm"]]
print(csGroupAnagrams([""])) # [[""]]
print(csGroupAnagrams(["a"])) # [["a"]]