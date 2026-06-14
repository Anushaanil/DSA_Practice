class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = 0
        citations = sorted(citations, reverse=True)
        for i in range(0, len(citations)):
            if citations[i] < i+1:
                break
            h_index = i+1
        return h_index
            