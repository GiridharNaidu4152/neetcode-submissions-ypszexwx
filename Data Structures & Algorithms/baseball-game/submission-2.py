class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk=[]
        for char in operations:
            if char!="C" and char!="D" and char!="+":
                stk.append(int(char))
            elif char=="C":
                stk.pop()
            elif char=="D":
                stk.append(2*int(stk[-1]))
            elif char=="+":
                stk.append(stk[-1]+stk[-2])
        return sum(stk)            
