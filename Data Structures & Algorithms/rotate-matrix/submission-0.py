class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        arr=[]
        for i in range(len(matrix)):
            temp=[]
            for j in range(1,len(matrix)+1):
                temp.append(matrix[-j][i])
            arr.append(temp)
        matrix[:]=arr