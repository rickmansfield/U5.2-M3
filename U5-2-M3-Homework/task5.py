import builtins
# print(help(dict))
# print(help({}))
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
# print(help(dict.get))
    # Return the value for key if key is in the dictionary, else default.
# print(help(""))
    # returns a huge list of possibilities including "".join


def csGroupAnagrams(strs):
    dict1 = dict()
    for eachWord in strs: 
        itsKey = tuple(sorted(eachWord))
        # print("its Key", itsKey)
        dict1[itsKey] = dict1.get(itsKey, []) + [eachWord]
        # print(dict1[itsKey])
    return list(dict1.values())
        

print(csGroupAnagrams(["apt","pat","ear","tap","are","arm"])) # [["apt","pat","tap"],["ear","are"],["arm"]]
# print(csGroupAnagrams([""])) # [[""]]
# print(csGroupAnagrams(["a"])) # [["a"]]