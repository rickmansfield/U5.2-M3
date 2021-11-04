
def csWordPattern(pattern, a):
    # print(a.split())
    words = a.split()
    # print("words split", words)
    
    if len(words) != len(pattern):
        return False
    char_to_word = dict()
    
    for i in range(len(pattern)):
        char = pattern[i]
        word = words[i]
        
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            if word in char_to_word.values():
                return False
            
            char_to_word[char] = word
    return True



print(csWordPattern("abba", "lambda school school lambda"))
print(csWordPattern("abba", "lambda school school coding"))
print(csWordPattern("aaaa", "lambda school school lambda"))
print(csWordPattern("abba", "lambda lambda lambda lambda"))