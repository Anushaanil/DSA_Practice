class Solution:
    def calculate(self, s: str) -> int:
        number = 0 # cur number we are dealing with
        res = 0 # cur result
        sign = 1 # starting off with + sign i.e 1, - is -1
        result_stack = [] # holds previous result

        for char in s:
            if char == " ":
                continue

            elif char.isdigit():
                number = (number * 10) + int(char)

            elif char in ["+", "-"]:
                res+=number * sign
                number = 0 # reset as it's used already
                sign = 1 if char == "+" else -1

            elif char == "(":
                result_stack.append(res)
                result_stack.append(sign)
                res = 0
                number = 0 # reset as we just entered in new brackets
                sign = 1

            elif char == ")":
                res+=number * sign
                number = 0 # reset as it's used already

                sign = result_stack.pop()
                res*=sign

                last_res = result_stack.pop()
                res+=last_res

        res+=number*sign
        return res