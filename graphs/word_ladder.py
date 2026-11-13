from collections import deque
class Solution:
    def ladderLengthApproach1(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        q, visited = deque([beginWord]), {beginWord}
        words_len = 1

        if endWord not in wordList:
            return 0

        while q:
            q_len = len(q)

            for i in range(q_len):
                curr_word = q.popleft()

                if curr_word == endWord:
                    return words_len
                
                # discover neighbors
                for word in wordList:
                    count = 0
                    for char in range(len(word)):
                        if word[char]!=curr_word[char]:
                            count+=1

                        if count > 1:
                            break

                    if count == 1 and word not in visited:
                        visited.add(word)
                        q.append(word)
            words_len +=1

        return 0
    
    def ladderLengthApproach2(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        q, visited = deque([beginWord]), {beginWord}
        words_len = 1
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        while q:
            q_len = len(q)

            for i in range(q_len):
                curr_word = q.popleft()

                if curr_word == endWord:
                    return words_len
                
                # discover neighbors
                for j in range(len(curr_word)):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        if curr_word[j] == char:
                            continue

                        mutated = curr_word[:j] + char + curr_word[j+1:]

                        if mutated not in visited and mutated in word_set:
                            visited.add(mutated)
                            q.append(mutated)
            words_len +=1

        return 0
    
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

s = Solution()
ans = s.ladderLengthApproach2(beginWord, endWord, wordList)
print(ans)