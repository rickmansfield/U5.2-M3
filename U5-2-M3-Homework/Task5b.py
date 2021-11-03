"""
create a dictionary to hold the anagram map

iterate over all the words in the strs
    store a sorted version of the word
    check if the sorted word is in the anagrams dictionary
        create an entry in the anagrams dic at the key of the sorted word containing a new list with the current word in it 
othwise 
    append the current word to the list vontained in the anangrams dictiionary at the key of sorted word

create an empty list to populate with the lists of anangramd

iterate over teach value in the anagrams dict
    append the value to the output list
    
return the output in the caller. 

"""
anagrams = {}
def csGroupAnagrams(strs):

    for word in strs:
        sorted_word = "".join(sorted(word))
        
        if sorted_word not in anagrams:
            anagrams[sorted_word] = [word]
        else: 
            anagrams[sorted_word].append(word)
            
    output = []
    for value in anagrams.values():
        output.append(value)
    return output