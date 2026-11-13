from collections import deque
class Solution:
    def minMutationApproach1(self, startGene: str, endGene: str, bank: list[str]) -> int:
        visited = {startGene}
        q = deque([(startGene, 0)])

        while q:
            node, level = q.popleft()

            if node == endGene:
                return level
            
            for gene in bank:
                count = 0
                for char in range(len(gene)):
                    if gene[char]!=node[char]:
                        count+=1

                    if count > 1:
                        break

                if count == 1 and gene not in visited:
                    visited.add(gene)
                    q.append([gene, level+1])

        return -1

    def minMutationApproach2(self, startGene: str, endGene: str, bank: list[str]) -> int:
        visited = {startGene}
        q = deque([startGene])
        mutations = 0
        bank_set = set(bank)

        while q:
            q_len = len(q)
            for i in range(q_len):
                current_gene = q.popleft()

                if current_gene == endGene:
                    return mutations
                
                for j in range(len(current_gene)):
                    for char in "ACGT":
                        if current_gene[j] == char:
                            continue

                        nextgene = list(current_gene)
                        nextgene[j] = char
                        mutated = "".join(nextgene)

                        if mutated not in visited and mutated in bank_set:
                            visited.add(mutated)
                            q.append(mutated)
            mutations+=1
        return -1

startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

s = Solution()
ans = s.minMutationApproach2(startGene, endGene, bank)
print(ans)