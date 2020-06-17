class Solution(object):
    def convert1(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s)<=numRows or numRows==1:
            return s
        numRow=2*numRows-2
        if len(s)<numRow:
            numCols=len(s)//numRows+len(s)%numRows
        elif (len(s)%numRow)//numRows==0:
            numCols=(len(s)//numRow)*(numRows-1)+int(len(s)%numRow!=0)
        else:
            numCols = (len(s) // numRow) * (numRows - 1) + (len(s) % numRow )%numRows+1
        res_list=[[0]*numCols for i in range(numRows)]
        t=0
        for i in range(len(s)):
            col_index=i//numRow+t
            row_index=i%numRow
            if row_index<numRows:
                res_list[row_index][col_index]=s[i]
            else:
                res_list[numRow-row_index][col_index+1]=s[i]
                t=t+1
        res=''
        for i in range(numRows):
            for j in range(numCols):
                if res_list[i][j]!=0:
                    res=res+res_list[i][j]
        return res

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) < numRows or numRows == 1:
            return s
        dp = [''] * numRows
        index = 0
        step = 1
        for i in s:
            dp[index] += i
            index += step
            if index == numRows - 1:
                step = -1
            if index == 0:
                step = 1
        return ''.join(dp)
Solution().convert("PAYPALISHIRING",5)