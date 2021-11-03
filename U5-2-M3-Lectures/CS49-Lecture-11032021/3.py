# lets do some frequency
s = "this is a string of letters to demonstrate a frequencies of letters inside using a hash table data structure"

words = s.split(" ")
# print(words)
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

for word in words:
    if freq[word] == 2:
        print(word)
        break


# lets try some mapping
alpha = "abcdefghijklmnopqrstuvwxyz"
mapping = {}

for char in alpha:
    mapping[char] = alpha[(alpha.find(char) + 13) % 26]


def rot13cipher(phrase):
    output = ""
    for char in phrase:
        if char in mapping:
            output += mapping[char]
        else:
            output += char

    return output


print()
secret = rot13cipher(s)
print(secret)
message = rot13cipher(secret)
print(message)
