mapping = {}
alpha = "abcdefghijklmnopqrstuvwxyz"
for char in alpha:
  mapping[char] = alpha[(alpha.find(char)+ 13) % 26]

def rot13cipher(phrase):
  output = ""
  for char in phrase: 
    if char in mapping:
      output += mapping[char]
    else:
      output += char
  return output
print(rot13cipher(s))