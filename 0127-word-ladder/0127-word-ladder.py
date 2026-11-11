class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
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