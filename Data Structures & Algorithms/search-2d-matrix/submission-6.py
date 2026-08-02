class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col=len(matrix),len(matrix[0])
        top,bottom=0,row-1
        while top<=bottom:
            ROW=(top+bottom)//2
            if matrix[ROW][-1]<target:
                top=ROW+1
            elif matrix[ROW][0]>target:
                bottom=ROW-1
            else:
                break
        if not(top<=bottom):
            return False
        ROW=(top+bottom)//2
        l,r=0,col-1
        while l<=r:
            m=(l+r)//2
            if matrix[ROW][m]<target:
                l=m+1
            elif matrix[ROW][m]>target:
                r=m-1
            else:
                return True
        return False




        