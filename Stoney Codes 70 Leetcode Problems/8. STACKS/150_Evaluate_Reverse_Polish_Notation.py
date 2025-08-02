from typing import List

def evalRPN(tokens: List[str]) -> int:
        stk = []
        for t in tokens:
            if t in '+-*/':
                a, b = stk.pop(), stk.pop()
                if t == '+':
                    stk.append(b + a)
                elif t == '-':
                    stk.append(b - a)
                elif t == '*':
                    stk.append(b * a)
                else:
                    stk.append(int(b / a))
            else:
                stk.append(int(t))
        
        return stk[0]

if __name__ == "__main__":
     tokens = ["2","1","+","3","*"]
     print(evalRPN(tokens))