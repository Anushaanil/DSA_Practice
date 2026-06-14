class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line_words = []
        cur_len = 0
        
        for word in words:
            if cur_len + len(word) + len(line_words) > maxWidth:
                result.append(line_words)    # finalize current line
                line_words = []              # start fresh
                cur_len = 0
            
            # add word into the current line
            line_words.append(word)
            cur_len += len(word)
        
        # after the loop, push the last line
        if line_words:
            result.append(line_words)
        
        for i, line_word in enumerate(result):
            total_spaces_left = (maxWidth - sum(len(word) for word in line_word))
            gaps = len(line_word)-1
            
            if i == len(result)-1 or gaps == 0:
                res = ' '.join(line_word)
                res += ' ' * (maxWidth - len(res))
            
            else:
                spaces = total_spaces_left//gaps
                append_spaces = total_spaces_left%gaps
                
                res = ''
                for j, word in enumerate(line_word):
                        res += word
                        if j < gaps:
                            res+=' '*(spaces + (1 if j< append_spaces else 0))
                
            result[i] = res
            
        return result