class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]
        for A in tokens:
            if A!="+" and A!="-" and A!="*" and A!="/":
                stk.append(int(A))
            else:
                b=int(stk.pop())
                a=int(stk.pop())
                if A=="+":
                    stk.append(a+b)
                elif A=="-":
                    stk.append(a-b)
                elif A=="*":
                    stk.append(a*b)
                elif A=="/":
                    stk.append(int(a/b))
        return stk[0]