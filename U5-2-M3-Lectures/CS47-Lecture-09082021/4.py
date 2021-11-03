"""
You are given a non-empty list of words.
Write a function that returns the *k* most frequent elements.
The list that you return should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower alphabetical
order should come first.
Example 1:
```plaintext
Input:
words = ["lambda", "school", "rules", "lambda", "school", "rocks"]
k = 2
Output:
["lambda", "school"]
Explanation:
"lambda" and "school" are the two most frequent words.
```
Example 2:
```plaintext
Input:
words = ["the", "sky", "is", "cloudy", "the", "the", "the", "cloudy", "is", "is"]
k = 4
Output:
["the", "is", "cloudy", "sky"]
Explanation:
"the", "is", "cloudy", and "sky" are the four most frequent words. The words
are sorted from highest frequency to lowest.
```
Notes:
- `k` is always valid: `1 <= k <= number of unique elements.
- words in the input list only contain lowercase letters.
```
["the", "sky", "is", "cloudy", "the", "the", "the", "cloudy", "is", "is"]
freq = {"the": 4, "sky": 1, "is": 3, "cloudy": 2} sort this based on the values
res = ["the", "is", "cloudy", "sky"]
res[:k]


# get the freq of each word
# sort the dictionary besed on keys (maybe use a lambda)
# encapsulate this sorted dictionary inside another function to sort it alpha?
# then slice the results to constrain to k
"""


def top_k_frequent(words, k):
    """
    Input:
    words -> List[str]
    k -> int
    Output:
    List[str]
    """
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    sorted_data = sorted(frequency, key=lambda word: (-frequency[word], word))

    return sorted_data[:k]


# Tests
print(top_k_frequent(["the", "sky", "is", "cloudy", "the", "the", "the", "cloudy", "is", "is"], 4)) # ['the', 'is', 'cloudy', 'sky']
print(top_k_frequent(["lambda", "school", "rules", "lambda", "school", "rocks"], 2)) #['lambda', 'school']
# 

