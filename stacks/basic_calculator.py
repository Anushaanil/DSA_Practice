class Solution:
    def calculate(self, s: str) -> int:
        operators = {"+", "-"}
        output_stack = []
        s = list(s)
        print(s)

        for ele in s:
            
            if ele == " ":
                continue

            elif ele == "(": # (1+(4+5+2
                output_stack.append(ele)
            
            elif ele in operators:
                output_stack.append(ele)

            elif ele.isdigit():
                output_stack.append(int(ele))

            elif ele == ")":
                while output_stack[-1]!="(":
                    right_operand = output_stack.pop()
                    op = output_stack.pop()
                    left_operand = output_stack.pop()
                    
                    if op == "+":
                        output_stack.append(left_operand + right_operand)
                    else:
                        output_stack.append(left_operand - right_operand)

                output_stack.pop()

        # Evaluate whatever remains outside parentheses
        while len(output_stack) > 1:
            right = output_stack.pop()
            op = output_stack.pop()
            left = output_stack.pop()

            if op == "+":
                output_stack.append(left + right)
            else:
                output_stack.append(left - right)

        return output_stack[-1]


class Solution:
    def calculate(self, s: str) -> int:
        result_stack = []
        res = 0
        number = 0
        sign = 1

        # s = list(s)
        # s = "(1+(4+5-2)-3)+(6+8)"

        for char in s:
            print('\n')
            print('char', char)
            if char == " ":
                continue
            elif char == "+":
                res+=number*sign
                print('res at +', res)
                number=0
                sign = 1

            elif char == "-":
                res+=number*sign
                print('res at -', res)
                number=0
                sign = -1
            
            elif char == "(":
                result_stack.append(res)
                result_stack.append(sign)
                res=0
                number=0
                sign=1
                print('result stack at (', result_stack)
            
            elif char == ")":
                res+=number*sign
                number = 0
                print('result_stack at )', result_stack)

                sign = result_stack.pop()
                res*=sign

                last_res = result_stack.pop()
                res+=last_res
                print('cur sign', sign)
                print('num', number)
                print('res', res)
                
            else:
                print('number, char, res before', number, char, res)
                number = (number*10)+int(char)
                
                print('cur sign', sign)
                print('num', number)
                print('res', res)
        
        res+=number*sign
        
        return res

problem = Solution()
# Example 1:

# Input: s = "1 + 1"
# Output: 2
# Example 2:

# Input: s = " 2-1 + 2 "
# Output: 3
# Example 3:

# Input: s = "(1+(4+5-2)-3)+(6+8)"
# Output: 23
s = "1-(     -2)"
# ans = 19
print(problem.calculate(s))