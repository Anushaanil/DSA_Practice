from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        q, visited = deque([(startGene, 0)]), {startGene}

        while q:
            node, level = q.popleft()

            if node == endGene:
                return level
            
            for gene in bank:
                count = 0
                for char in range(len(gene)):
                    if gene[char]!= node[char]:
                        count+=1

                    if count > 1:
                        break
                    
                if count == 1 and gene not in visited:
                    visited.add(gene)
                    q.append([gene, level + 1])
        return -1