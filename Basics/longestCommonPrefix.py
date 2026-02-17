'''
 # @ Create Time: 2025-07-22 14:16:15
 # @ Modified time: 2025-11-17 00:38:59
 '''


def longestCommonPrefix(strs):
    longest_str = ""
    
    if not strs:
        return longest_str

    first_word = strs[0]
    print('first', first_word)

    for i, char in enumerate(first_word): # flower
        print('i', i, char)
        
        for word in strs[1:]:
            
            print('j', word)

            if i >= len(word) or word[i] != char:
                return longest_str
            
        longest_str+=char

    return longest_str

strs = ["dog","racecar","car"]

print(longestCommonPrefix(strs))