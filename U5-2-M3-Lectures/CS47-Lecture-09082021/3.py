mapping = {}
alpha = "abcdefghijklmnopqrstuvwxyz"
for char in alpha:
  mapping[char] = alpha[(alpha.find(char)+ 13) % 26]

print(mapping)